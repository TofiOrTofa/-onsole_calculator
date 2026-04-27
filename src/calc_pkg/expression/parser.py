"""module - example compiler"""

from calc_pkg import nodes



#class Lexer:
#    """
#    names data tokens:
#        1. SignsType
#        2. NumberType
#        3. BacketType
#    """
#    def __init__(self, signs: object) -> None:
#        self._signs = signs
#
#    def tokenize(self, expression: str) -> list[nodes.Token]:
#        tokens = []
#        index = 0
#        while index < len(expression):
#            if nodes.SignsType.test_in(expression[index]):
#                tokens.append(
#                    nodes.Token(
#                        kind = "Signs",
#                        value = expression[index]
#                    )
#                )
#            else:
#                return 1, expression[index]
#class Parser: ...
#class Evalator: ...


class Expression:
    def __init__(self, signs:object, user_expression:str):
        self._signs = signs
        self._expression = self._compilate(user_expression)

    def _compilate(self, expression:str)->object:

        expression = expression.strip(" ")
        min_importance:int = self._signs.importance.ceiling()

        depth = 0
        for char_index, char in enumerate(expression):
            if char == '(':
                depth += 1
            elif char == ')' and char_index != len(expression)-1:
                depth -= 1
            if not depth:
                break
        else:
            expression = expression[1:-1]

        depth = 0
        for char in expression:
            if char.isdigit():
                continue

            if char == '(':
                depth += 1
            elif char == ')':
                depth -= 1

            if not depth:
                if self._signs.availability_test(char):
                    char_importance = self._signs.importance[char]
                    if char_importance < min_importance:
                        min_importance = char_importance
                else:
                    continue

        depth = 0

        for char_index, char in enumerate(expression[::-1]):
            if char.isdigit():
                continue

            elif char == '(':
                depth -= 1
                continue
            elif char == ')':
                depth += 1
                continue

            if depth == 0:
                char_importance = self._signs.importance[char]
                if char_importance == min_importance :
                    sign_class:type = self._signs[char]["obj_name"]
                    return sign_class(
                        self._compilate(expression[:-char_index-1]),
                        self._compilate(expression[-char_index:])
                    )
        return nodes.Constant(expression)


    def score(self):
        return self._expression.score()
