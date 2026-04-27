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
    def __init__(self, first_operand: object, second_operand: object) -> None:
        self._fo = first_operand
        self._so = second_operand
    @abstractmethod
    def score(self) -> object: ...


class Token:
    def __init__(self, kind: str, value: str) -> None:
        self._kind = kind
        self._value = value

    def kind(self) -> str:
        return self._kind
    def value(self) -> str:
        return self._value


class Importance:
    def __init__(self, data: dict) -> None:
        self._source = data
        self._data = sorted(set(var for var in data.values()))
    
    def __len__(self) -> int:
        return len(self._data)
    def __getitem__(self, value) -> (list or int) or None:
        if value.isdigit():
            priority: int = value
            if priority in self._data:
                symbols = []
                for key, value in self._source.items():
                    print(key)
                    print(value)
                    if value["priority"] == priority:
                        symbols.append(key)
                return symbols
            else:
                return None
        else:
            symbol: str = value
            if symbol in self._source:
                return self._source[symbol]["priority"]
            else:
                return None
        
    def floor(self) -> int:
        return self._data[0]
    def ceiling(self) -> int:
        return self._data[-1]

    def append(self, priority: int) -> None:
        if priority in self._data:
            return
        else:
            self._data.append(priority)
            self._data = sorted(self._data)

class MathSigns:
    def __init__(self) -> None:

        self._data = {}
        self.importance = Importance(self)

    def __call__(self, symbol: str, priority: int) -> type or None:
        def decorator(math_object: type):
            self[symbol] = {
                "obj_name": math_object,
                "priority": priority
            }
            self.importance.append(priority)
            return math_object
        return decorator

    def __getitem__(self, symbol: str)->type or None:
        if symbol in self._data:
            return self._data[symbol]
        else:
            return None
    def __setitem__(self, symbol: str, value: dict) -> None:
        if symbol in self._data:
            return
        else:
            test = ("obj_name" in value) and ("priority" in value)
            if isinstance(value, dict) and test:
                self._data[symbol] = value
    def __iter__(self):
        return iter(self._data)

    def values(self) -> list:
        priority = []
        for info in self._data.values():
            priority.append(info)
        return priority
    def item(self):
        return self._data.items()

    def availability_test(self, symbol: str) -> bool:
        return symbol in self._data

class MathTypes:
    def __init__(self) -> None:

        self._data = {}

    def __call__(self, symbol: str):
        def decorator(math_type):
            self._data[symbol] = math_type
            return math_type
        return decorator


class Constant:
    def __init__(self, source: str) -> None:
        self._content = source or '0'
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
    def __init__(self, n: int, d: int) -> None:
        gcp = self._find_gcp(n, d)
        self._n = n // gcp
        self._d = d // gcp

    def __str__(self) -> str:
        result = f"{self._n}/{self._d}"
        if self._n % self._d == 0:
            result = f"{self._n}"
        elif len(str(self._n % self._d)) < 10:
            result += f" ({self._n / self._d})"
        return  result
        
    def __add__(self, other: object) -> ReducedFraction:# сложение
        new_n = self._n * other._d + other._n * self._d
        new_d = self._d * other._d
        return ReducedFraction(new_n, new_d)
    def __sub__(self, other: object) -> ReducedFraction:# вычетание
        new_n = self._n * other._d - other._n * self._d
        new_d = self._d * other._d
        return ReducedFraction(new_n, new_d)
    def __mul__(self, other: object) -> ReducedFraction:# умножение
        new_n = self._n * other._n
        new_d = self._d * other._d
        return ReducedFraction(new_n, new_d)
    def __truediv__(self, other: object) -> ReducedFraction:# деление
        new_n = self._n * other._d
        new_d = self._d * other._n
        return ReducedFraction(new_n, new_d)


    def _find_gcp(self, nr: int, dr: int) -> int:
        gcd1 = nr
        gcd2 = dr
        while gcd2 > 0:
            tmp = gcd1 % gcd2
            gcd1, gcd2 = gcd2, tmp
        return gcd1