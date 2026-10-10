"""module - example compiler"""

from types import TYPE_CHECKER
from dataclasses import asdict
from calc_pkg import nodes
if TYPE_CHECKER:
    from typing import (
            Dict, List,
            Any,
            Optional,
            TypeAlias)

    T: TypeAlias = 'nodes.Token'
    TC: TypeAlias = 'nodes.TokenTypes'


class Lexer:
    _types: 'TC'
    _expression: str


    def __init__(self, user_expression: str, token_context: 'TC') -> None:
        self._types = token_context
        self._expression = user_expression

    def tokenize(self) -> 'List[T]':
        tokens = []
        value = ''
        for char in self._expression:
            char_type = self.test(char)
            if char_type is "numbers":
                value += char
            else:
                tokens.append(
                    nodes.Token(
                        kind = char_type,
                        value = char))
        return tokens

    def test(self, char: str) -> type:
        if char in self._types.numbers:
            return self._types.numbers
        else:
            for key, val in asdict(self._types).items():
                if char in val:
                    return var
            else:
                return nodes.Error


class PrioritySearcher:
    _types: 'TC'

    def __init__(self) -> None:
        self._types = nodes.token_types

    def min(self, expression: 'List[T]', brackets_role_test):
        depth = 0
        for token in expression:
            if token.kind == "brackets":
                depth = brackets_role_test(token, depth)
            elif token.kind == "sign": ...#TO_DO

class Parser:
    _types: 'TC'
    _priority: 'PrioritySearcher'
    _expression: 'List[T]'

    def __init__(self, expression: 'List[T]') -> None:
        self._types = nodes.token_types
        self._expression = expression
        self._priority = PrioritySearcher()

    def __call__(self) -> object:
        depth = 0
        min_priority = self.search_min_priority()
        for token in self._expression:
            if token.kind is nodes.Brackets:
                depth = self.brackets_role_test(token, depth)
        if not depth:
            except(...)#TO_DO: нужно написать нормальную ошибку
        for token in self._expression:


    def brackets_role_test(self, token, depth):
        type_brackets = self._brackets.get_role(token)
        if type_brackets == "open":
            depth += 1
        elif type_brackets == "close":
            depth -=1
        return depth


class Evalator: ...
