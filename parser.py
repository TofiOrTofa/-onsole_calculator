from nodes import *

class Expression:
    def __init__(self, signs:object, user_expression:str):
        self._signs = signs
        self._expression = self._compilate(user_expression)
    
    def _compilate(self, expression:str):
        min_sign:str; min_importance:int
        max_sign:str; max_importance:int
        numbers:tuple
        depth:int
        
        depth = 0
        for char in expression[:-1]+' ':
            if char == '(': depth += 1
            elif char == ')': depth -= 1
            if not depth: break
        else: expression = expression[1:-1]

        min_sign = self._signs.get_min()#min_sign
        min_importance = self._signs.get_importance(min_sign)

        max_sign = self._signs.get_max()
        max_importance = self._signs.get_importance(max_sign)

        numbers = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        depth = 0
        for char_index in range(len(expression)):
            if expression[char_index] in numbers:
                continue

            elif expression[char_index] == '(': depth += 1; continue
            elif expression[char_index] == ')': depth -= 1; continue

            if not depth:
                for importance in range(min_importance, max_importance+1):
                    symbols = self._signs.get_symbol(importance)
                    for symbol in symbols:
                        if expression[char_index]==symbol:
                            sign_class:type = self._signs.get_class(symbol)
                            return sign_class(
                                self._compilate(expression[:char_index]),
                                self._compilate(expression[char_index+1:])
                            )
        return Constant(expression)
                
        
        
        for importance in range(min_sign_importance, max_sign_importance+1):
            symbols = self._signs.get_symbol(importance)
            for symbol in symbols:
                if (sign_index := expression.find(symbol)) != -1:
                    sign_class:type = self._signs.get_class(symbol)
                    return sign_class(
                        self._compilate(expression[:sign_index]),
                        self._compilate(expression[sign_index+1:])
                    )
        else:
            return Constant(expression)


    def score(self):
        return self._expression.score()
