

class Expression:
    def __init__(self,
        signs           : object,
        user_expression : str
    ):#>--------------------<#
        self._signs = signs
        self._expression = user_expression
    

    def score(self): ...
