"""module - example compiler"""
from typing import Final

from calc_pkg import nodes

NUMBERS: Final = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

class Expression:
    """object - compiler expression in object tree

    attributes:
        _signs (object): save dictionary math signs 
        _expression (object): math object tree
    """
    def __init__(self, signs:object, user_expression:str):
        """
        args:
            signs (object): dictionary object for calculator characters
            user_expression (str): raw example entered by the user
        """
        self._signs = signs
        self._expression = self._compilate(user_expression)

    def _compilate(self, expression:str):
        """compiler expression in object tree

        The compiler leaning on importance math symbols when compiling
        expression into a tree of objects that are ready calculations

        Args:
            expression (str): raw example entered by the user

        Returns:
            nodes.Constant: if example is number
            object: object math sign branching into two subexpressions
        
        Raises:
            UndoundLocalError: when finding an unknown symbol
        """

        min_importance:int = self._signs.get_max_importance()

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
            if char == '(':
                depth += 1
            elif char == ')':
                depth -= 1
            if not depth:
                if char in NUMBERS:
                    continue
                else:
                    if self._signs.availability_test(char):
                        char_importance = self._signs.get_importance(char)
                        if char_importance<min_importance:
                            min_importance = char_importance

        depth = 0

        for char_index, char in enumerate(expression[::-1]):
            if char in NUMBERS:
                continue

            elif char == '(':
                depth -= 1
                continue
            elif char == ')':
                depth += 1
                continue

            if depth == 0:
                char_importance = self._signs.get_importance(char)
                if char_importance == min_importance :
                    sign_class:type = self._signs.get_class(char)
                    return sign_class(
                        self._compilate(expression[:-char_index-1]),
                        self._compilate(expression[-char_index:])
                    )
        return nodes.Constant(expression)


    def score(self):
        """launch of the solition

        Returns:
            node.ReducedFraction
        """
        return self._expression.score()
