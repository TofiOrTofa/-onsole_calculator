from typing import TYPE_CHECKING, Generic
from abc import ABC, abstractmethod
from dataclasses import dataclass
if TYPE_CHECKING:
    from typing import (
            Callable, Self,
            TypeAlias, TypeVar,
            TypedDict,
            Optional, Literal,
            List, Dict,
            Any)
    from typing import TypeAlias as TA
    T_cls = TypeVar("T_cls", bound=type)


@dataclass
class AbstractToken(ABC):
    kind: type
    value: str



class AbstractOperand(ABC):

    @abstractmethod
    def __init__(self) -> None: ...

    @abstractmethod
    def __add__(self) -> None: ...

    @abstractmethod
    def __sub__(self, other: 'Self') -> 'Self': ...

    @abstractmethod
    def __mul__(self, other: 'Self') -> 'Self': ...

    @abstractmethod
    def __truediv__(self, other: 'Self') -> 'Self': ...


class AbstractMathType(ABC):
    _instance: 'Optional[Self]'
    _data: 'Dict[str, Any]'#TO_DO: нужно избавиться от Any

    @abstractmethod
    def __contains__(self, symbol: str) -> bool: ...

    @abstractmethod
    def __new__(cls) -> Self: ...

class AbstractOneReleaseAbstract(AbstractMathType, ABC):

    @abstractmethod
    def __call__(self,
                 source: 'Optional[str]'
                 ) -> 'Callable[[T_cls], T_cls]': ...


