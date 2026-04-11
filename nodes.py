from abc import ABC, abstractmethod

# абстрактные классы>--------------------
class Operand(ABC):
    @abstractmethod
    def __init__(self): ...
    @abstractmethod
    def __add__(self, other): ...
    @abstractmethod
    def __sub__(self, other): ...
    @abstractmethod
    def __mul__(self, other): ...
    @abstractmethod
    def __truediv__(self, other): ...
    @abstractmethod
    def score(self): ...
class MathSigns(ABC):
    @abstractmethod
    def __init__ (self,
        first_operand  : object,
        second_operand : object
    ): ...
    @abstractmethod
    def score(self): ...

class MathSignsInfo:
    def __init__(self):
        self._signs : dict[
            str : tuple(
                object,# объект знака
                int# значимость знака
            )
        ]
        self._importance : list[
            int,# минимальное значение
            int# максимальное значение
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
            if importance > self._importance["max"]:
                self._importance["max"] = importance
            elif importance < self._importance["min"]:
                self._importance["min"] = importance
        else: 
            self._importance["min"] = importance
            self._importance["max"] = importance 


    def get_class(self, symbol:str) -> type:
        return self._signs[symbol][0]
    def get_importance(self, symbol:str) -> int:
        return self._signs[symbol][1]
    def get_min_importance(self) -> int:
        return self._importance["min"]
    def get_max_importance(self) -> int:
        return self._importance["max"]
    def availability_test(self, symbol:str) -> bool:
        return symbol in self._signs


class Constant(Operand):
    def __init__(self, source:str):
        self._content = content
    def score(self) -> ReducedFraction:

        float_content = self._content.replace(",", ".")
        index = self.float_content.find(".")

        if index != -1:
            quantity = len(self._content) - index

            numerator = int(float_content.replace(".", ""))
            denominator = 10 ** quantity
            return ReducedFraction(numerator, denominator)
        return ReducedFraction(int(self._content))
# матиматические типы данных>--------------------
class Fraction(Operand):
    def __init__(self,
        numerator : Constant,
        denominator : Constant = 1
    ):#>--------------------<#
        self._n : Constant = numerator
        self._d : Constant = denominator
    def __add__(self, other:object) -> Fraction:# сложение
        new_n = self._n * other._d + other._n * self._d
        new_d = self._d * other._d
        return Fraction(new_n, new_d)
    def __sub__(self, other:object) -> Fraction:# вычетание
        new_n = self._n * other._d - other._n * self._d
        new_d = self._d * other._d
        return Fraction(new_n, new_d)
    def __mul__(self, other:object) -> Fraction:# умножение
        new_n = self._n * other._n
        new_d = self._d * other._d
        return Fraction(new_n, new_d)
    def __truediv__(self, other:object) -> Fraction:# деление
        new_n = self._n * other._d
        new_d = self._d * other._n
        return Fraction(new_n, new_d)
    def score(self): 
        return ReducedFraction(
            self._n.score(),
            self._d.score()
        )
class ReducedFraction(Operand, Fraction):
    def __init__(self, n:int, d:int):
        gcp : int = self._find_gcp(n, d)
        self._n : int = n // gcp
        self._d : int = n // gcp
    def _find_gcp(self, nr:int, dr:int) -> int, int:
        gcd1 : int = nr
        gcd2 : int = dr
        while gcd2 > 0:
            tmp = gcd1 % gcd2
            gcd1, gcd2 = gcd2, tmp
        return nr


# объекты мат. знаков>--------------------
class Sum(MathSigns):
    def __init__(self,
        first_operand  : object,
        second_operand : object
    ):#>--------------------<#
        self._fo : object = first_operand
        self._so : object = second_operand
    def score(self):
        return self._fo.score() + self._so.score()
class Difference(MathSigns):
    def __init__(self,
        first_operand  : object,
        second_operand : object
    ):#>--------------------<#
        self._fo : object
        self._so : object
    def score(self):
        return self._fo.score() - self._so.score()
class Product(MathSigns):
    def __init__(self,
        first_operand  : object,
        second_operand : object
    ):#>--------------------<#
        self._fo : object
        self._so : object
    def score(self):
        return self._fo.score() * self._so.score()
class Quotient(MathSigns):
    def __init__(self,
        first_operand  : object,
        second_operand : object
    ):#>--------------------<#
        self._fo : object
        self._so : object
    def score(self):
        return self._fo.score() / self._so.score()
class Ratio(MathSigns):
    def __init__(self,
        first_operand  : object,
        second_operand : object
    ):#>--------------------<#
        self._fo : object
        self._so : object
    def score(self):
        result = self._fo.score() / self._so.score()
        return result * ReducedFraction(100)