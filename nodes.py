from abc import ABC, abstractmethod

# абстрактные классы>--------------------
class Operand(ABC):
    @abstractmethod
    def __init__(self)->None: ...
    @abstractmethod
    def __add__(self, other): ...
    @abstractmethod
    def __sub__(self, other): ...
    @abstractmethod
    def __mul__(self, other): ...
    @abstractmethod
    def __truediv__(self, other): ...
class MathSignsAbstract(ABC):
    @abstractmethod
    def __init__ (self, first_operand:object, second_operand:object)->None: ...
    @abstractmethod
    def score(self)->object: ...

class MathSignsInfo:
    def __init__(self)->None:
        self._signs : dict[
            str : tuple(
                object,# объект знака
                int# значимость знака
            )
        ]
        self._importance : dict[
            str : str,# минимальное значение
            str : str# максимальное значение
        ]
        
        self._importance = {
            "min" : None,
            "max" : None
        }
        self._signs = {}
    def add(self,
        symbol     : str,
        name       : type,
        importance : int
    ):#>--------------------<#
        self._signs[symbol] = (name, importance)
        if not (
            self._importance["min"] is None or
            self._importance["max"] is None
        ):#>--------------------<#
            if importance > self.get_importance(self._importance["max"]):
                self._importance["max"] = symbol
            elif importance < self.get_importance(self._importance["min"]):
                self._importance["min"] = symbol
        else: 
            self._importance["min"] = symbol
            self._importance["max"] = symbol

            

    def get_class(self, symbol:str) -> type:
        return self._signs[symbol][0]
    def get_importance(self, symbol:str) -> int:
        return self._signs[symbol][1]
    def get_min(self) -> str:
        return self._importance["min"]
    def get_max(self) -> str:
        return self._importance["max"]
    def get_symbol(self, importance:int):
        key : str; value : tuple[type, int]
        symbols = list()
        for key, value in self._signs.items():
            if importance == value[1]:
                symbols.append(key)
        return symbols
    def availability_test(self, symbol:str) -> bool:
        return symbol in self._signs


class Constant:
    def __init__(self, source:str):
        self._content = source
    def score(self) -> ReducedFraction:

        float_content = self._content.replace(",", ".")
        index = float_content.find(".")

        if index != -1:
            quantity = len(self._content) - index

            numerator = int(float_content.replace(".", ""))
            denominator = 10 ** (quantity-1)
            return ReducedFraction(numerator, denominator)
        return ReducedFraction(int(self._content), 1)
# матиматические типы данных>--------------------
class Fraction():
    def __init__(self,
        numerator : Constant,
        denominator : Constant = 1
    ):#>--------------------<#
        self._n : Constant = numerator
        self._d : Constant = denominator
    def score(self): 
        return ReducedFraction(
            self._n.score(),
            self._d.score()
        )
class ReducedFraction(Operand, Fraction):
    def __init__(self, n:int, d:int)->None:
        gcp : int = self._find_gcp(n, d)
        self._n : int = n // gcp
        self._d : int = d // gcp

    def __str__(self)->str:
        result:str
        result:str = f"{self._n}/{self._d}"
        if self._n % self._d == 0:
            result = f"{self._n}"
        elif len(str(self._n % self._d)) < 10:
            result += f" ({self._n / self._d})"
        return  result
        
    def __add__(self, other:object) -> Fraction:# сложение
        new_n = self._n * other._d + other._n * self._d
        new_d = self._d * other._d
        return ReducedFraction(new_n, new_d)
    def __sub__(self, other:object) -> Fraction:# вычетание
        new_n = self._n * other._d - other._n * self._d
        new_d = self._d * other._d
        return ReducedFraction(new_n, new_d)
    def __mul__(self, other:object) -> Fraction:# умножение
        new_n = self._n * other._n
        new_d = self._d * other._d
        return ReducedFraction(new_n, new_d)
    def __truediv__(self, other:object) -> Fraction:# деление
        new_n = self._n * other._d
        new_d = self._d * other._n
        return ReducedFraction(new_n, new_d)


    def _find_gcp(self, nr:int, dr:int) -> int:
        gcd1 : int = nr
        gcd2 : int = dr
        while gcd2 > 0:
            tmp = gcd1 % gcd2
            gcd1, gcd2 = gcd2, tmp
        return gcd1


# объекты мат. знаков>--------------------
class Sum(MathSignsAbstract):
    def __init__(self, first_operand:object, second_operand:object)->None:
        self._fo : object = first_operand
        self._so : object = second_operand
    def score(self):
        return self._fo.score() + self._so.score()
class Difference(MathSignsAbstract):
    def __init__(self, first_operand:object, second_operand:object)->None:
        self._fo = first_operand
        self._so = second_operand
    def score(self)->object:
        return self._fo.score() - self._so.score()
class Product(MathSignsAbstract):
    def __init__(self,
        first_operand  : object,
        second_operand : object
    ):#>--------------------<#
        self._fo : object = first_operand
        self._so : object = second_operand
    def score(self):
        return self._fo.score() * self._so.score()
class Quotient(MathSignsAbstract):
    def __init__(self,
        first_operand  : object,
        second_operand : object
    ):#>--------------------<#
        self._fo : object = first_operand
        self._so : object = second_operand
    def score(self):
        return self._fo.score() / self._so.score()
class Ratio(MathSignsAbstract):
    def __init__(self,
        first_operand  : object,
        second_operand : object
    ):#>--------------------<#
        self._fo : object = first_operand
        self._so : object = second_operand
    def score(self):
        result = self._fo.score() / self._so.score()
        return result * ReducedFraction(100, 1)