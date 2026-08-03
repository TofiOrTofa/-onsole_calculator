from typing import (
    TypedDict, List,
    TypeVar
)

T_cls = TypeVar("T_cls", bound=type)

# 1. Описываем точную структуру для min и max словарей
class ImportanceNode(TypedDict):
    priority: int
    symbols: List[str]

# 2. Описываем структуру основного словаря _importance
class ImportanceDict(TypedDict):
    min: ImportanceNode | None
    max: ImportanceNode | None

