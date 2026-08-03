from typing import Protocol, TYPE_CHECKING
from dataclasses import dataclass
if TYPE_CHECKING:
    from typing import (
            Callable, Self,
            TypeAlias, TypeVar,
            TypedDict,
            Optional, Literal,
            List, Dict,
            final,
            Any)



    class UnaryModes(TypedDict, total=False):
        prefix: 'UnarySign'
        postfix: 'UnarySign'

    class SignMap(TypedDict, total=False):
        binary: 'BinarySign'
        unary: 'UnaryModes'


    T_cls = TypeVar("T_cls", bound=type)


    C: TypeAlias = 'Constant'
    T: TypeAlias = 'Token'
    RF: TypeAlias = 'ReducedFraction'

    BS: TypeAlias = 'BinarySign'
    US: TypeAlias = 'UnarySign'
    SM: TypeAlias = 'SignMap'



@dataclass(frozen=True)
class Token:
    kind: type
    value: str


# протоколы>--------------------
class Operand(Protocol):

    def __init__(self) -> None: ...
    def __add__(self, other: 'Self') -> 'Self': ...
    def __sub__(self, other: 'Self') -> 'Self': ...
    def __mul__(self, other: 'Self') -> 'Self': ...
    def __truediv__(self, other: 'Self') -> 'Self': ...


class TypeElement(Protocol):

    def __init__(self) -> None: ...

    def score(self) -> 'Operand': ...

class SignsElement:
    _first_operand: 'TypeElement'
    _second_operand: 'TypeElement'

    def __init__(self,
                 first_operand: 'TypeElement',
                 second_operand: 'TypeElement'
                 ) -> None:
        self._first_operand = first_operand
        self._second_operand = second_operand


class MathType(Protocol):
    _data: 'Dict[str, Any]'#TO_DO: нужно исбавиться от Any

    def __contains__(self, symbol: str) -> bool:
        return symbol in self._data

    def __init__(self) -> None: ...

class OneReleaseType(MathType, Protocol):

    def __call__(self, source: str) -> 'Callable[[T_cls], T_cls]': ...

# >--------------------------------------


def system_terminal_clear() -> None:
    print("\033[H\033[2J", end="")


# типы AST дерева>-----------------------


@dataclass( frozen = True )
class BaseSign:
    symbol: str
    obj_name: type

@dataclass( frozen = True )
class BinarySign(BaseSign):
    priority: int

@dataclass( frozen = True )
class UnarySign(BaseSign):
    position: Literal["prefix", "postfix"]




@final
class Signs:
    _data: 'Dict[str, SM]'

    def __init__(self) -> None:
        self._data = {}

    def binary(self,
               source: str,
               priority: int = 0
               ) -> 'Callable[[T_cls], T_cls]':
        def decorator(cls: 'T_cls') -> 'T_cls':
            if source not in self._data:
                self._data[source] = {}
            self._data[source]["binary"] = BinarySign(
                    symbol = source,
                    obj_name = cls,
                    priority = priority)
            return cls
        return decorator

    def unary(self,
              source: str,
              position: Literal["prefix", "postfix"]
              ) -> Callable[[T_cls], T_cls]:
        def decorator(cls: T_cls) -> T_cls:
            if source not in self._data:
                self._data[source] = {}
            if "unary" not in self._data[source]:
                self._data[source]["unary"] = {}
            self._data[source]["unary"][position] = UnarySign(
                    symbol = source,
                    obj_name = cls,
                    position = position)
            return cls
        return decorator

    def get_map(self, symbol: str) -> Optional[SignMap]:
        return self._data.get(symbol)


@final
class Brackets:

    _data: 'Dict[str, Any]'#TO_DO
    _open: 'List[str]'
    _close: 'List[str]'

    def __init__(self) -> None:
        self._data = {}
        self._open = []
        self._close = []

    def __call__(self, source: str) -> 'Callable[[T_cls], T_cls]':
        def decorator(cls: 'T_cls') -> 'T_cls':
            self._data[source] = {
                "obj_name": cls
            }
            return cls
        if len(source.split()) == 2:
            return decorator
        raise ValueError(f"\
                Backets settings\
                - принимаются только два символа\
                разделённых пробелом!\n\
                Вы ввели: {source}\
                            ")
    def get_role(self, symbol: str) -> str:
        if symbol in self._open:
            return "open"
        elif symbol in self._close:
            return "close"
        else:
            raise TypeError(f"{symbol} - не является скобкой")


@final
class Numbers:
    _data: 'Dict[str, type]'

    def __init__(self) -> None:
        self._data = {}

    def __contains__(self, symbol: str) -> bool:
        for data_symbol in self._data:
            if data_symbol in symbol:
                return True
        return False

    def __call__(self) -> 'Callable[[T_cls], T_cls]':
        def decorator(cls: 'T_cls') -> 'T_cls':
            self._data["default"] = cls
            return cls
        return decorator


@final
class Error:
    _source: str

    def __init__(self, symbol: str) -> None:
        self._source = symbol
    def __str__(self) -> str:
        return self._source
# >--------------------------------------


@dataclass( frozen = True )
class TokenContext:
    signs: 'Signs'
    numbers: 'Numbers'
    brackets: 'Brackets'

@dataclass( frozen = True )
class TokenTypes(TokenContext):
    SIGNS_KIND: type
    NUMBERS_KIND: type
    BRACKETS_KIND: type

token_types = TokenTypes(
    signs=Signs(),
    numbers=Numbers(),
    brackets=Brackets(),

    SIGNS_KIND=Signs,
    NUMBERS_KIND=Numbers,
    BRACKETS_KIND=Brackets
)


@final
class Constant:
    _content: 'Optional[str]'

    def __init__(self, symbol: str) -> None:
        self._content = symbol or None

    def score(self) -> 'Optional[RF]':
        if self._content:
            float_content = self._content.replace(",", ".")
            index = float_content.find(".")
            if index != -1:
                quantity = len(self._content) - index
                numerator = int(float_content.replace(".", ""))
                denominator = 10 ** (quantity-1)
                return ReducedFraction(numerator, denominator)
            return ReducedFraction(int(self._content))
        return None

# общие типы чисел>----------------------
@final
class ReducedFraction:
    _numerator: int
    _denominator: int

    def __init__(self,
                 numerator: int,
                 denominator: Optional[int] = None
                 ) -> None:
        if not denominator:
            denominator = 1
        elif denominator == 0:
            raise ZeroDivisionError("знаменатель не может быть нулём")
        gcp = self._find_gcp(numerator, denominator)
        self._numerator = numerator // gcp
        self._denominator = denominator // gcp

    def __str__(self) -> str:
        result = f"{self._numerator}/{self._denominator}"
        if self._numerator % self._denominator == 0:
            result = f"{self._numerator}"
        elif len(str(self._numerator % self._denominator)) < 10:
            result += f" ({self._numerator / self._denominator})"
        return result

    def __add__(self, other: 'Self') -> 'Self':
        """сложение"""
        new_numerator: int = (
                self.get_numerator * other.get_denominator +
                other.get_numerator * self.get_denominator)
        new_denominator: int = self.get_denominator * other.get_denominator
        return ReducedFraction(new_numerator, new_denominator)
    def __sub__(self, other: 'Self') -> 'Self':
        """вычитание"""
        new_numerator: int = (
                self.get_numerator * other.get_denominator -
                other.get_numerator * self.get_denominator)
        new_denominator: int = self.get_denominator * other.get_denominator
        return ReducedFraction(new_numerator, new_denominator)
    def __mul__(self, other: 'Self') -> 'Self':
        """умножение"""
        new_numerator: int = self.get_numerator * other.get_numerator
        new_denominator: int = self.get_denominator * other.get_denominator
        return ReducedFraction(new_numerator, new_denominator)
    def __truediv__(self, other: 'Self') -> 'Self':
        """деление"""
        new_numerator: int = self.get_numerator * other.get_denominator
        new_denominator: int = self.get_denominator * other.get_numerator
        return ReducedFraction(new_numerator, new_denominator)


    @property
    def get_numerator(self) -> int:
        return self._numerator
    @property
    def get_denominator(self) -> int:
        if not self._denominator:
            return 1
        return self._denominator


    def _find_gcp(self, nr: int, dr: int) -> int:
        gcd1 = abs(nr)
        gcd2 = abs(dr)
        while gcd2 > 0:
            tmp = gcd1 % gcd2
            gcd1, gcd2 = gcd2, tmp
        return gcd1
