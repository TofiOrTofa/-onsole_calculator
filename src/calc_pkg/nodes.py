from __future__ import annotations
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

class MathSigns:
    def __init__(self)->None:
        self._signs_info : dict[
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
        self._signs_info = {}
        self._signs_name = set()
        self._signs_importance = list()
    def add(self, symbol:str, importance:int, class_name:type=None):
        def decorator(math_object):
            self._signs_info[symbol] = (math_object, importance)
            self._signs_name.add(symbol)
            self._signs_importance.append(importance)

            self._signs_importance.sort()
            return math_object
        
        if class_name is not None:
            decorator(class_name)
        else:
            return decorator
        

            

    def get_class(self, symbol:str) -> type:
        return self._signs_info[symbol][0]

    def get_importance(self, symbol:str) -> int:
        return self._signs_info[symbol][1]
    def get_min_importance(self) -> int:
        return self._signs_importance[0]
    def get_max_importance(self) -> int:
        return self._signs_importance[-1]

    def get_symbol(self, importance:int):
        symbols = list()
        for key, value in self._signs_info.items():
            key:str
            value:tuple[type, int]
            if importance == value[1]:
                symbols.append(key)
        return symbols
    def get_min_symbol(self):
        return self.get_symbol(self._signs_importance[0])
    def get_max_symbol(self):
        return self.get_symbol(self._signs_importance)
        
    def availability_test(self, symbol:str) -> bool:
        return symbol in self._signs_info


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
class ReducedFraction(Operand):
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
        
    def __add__(self, other:object) -> ReducedFraction:# сложение
        new_n = self._n * other._d + other._n * self._d
        new_d = self._d * other._d
        return ReducedFraction(new_n, new_d)
    def __sub__(self, other:object) -> ReducedFraction:# вычетание
        new_n = self._n * other._d - other._n * self._d
        new_d = self._d * other._d
        return ReducedFraction(new_n, new_d)
    def __mul__(self, other:object) -> ReducedFraction:# умножение
        new_n = self._n * other._n
        new_d = self._d * other._d
        return ReducedFraction(new_n, new_d)
    def __truediv__(self, other:object) -> ReducedFraction:# деление
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