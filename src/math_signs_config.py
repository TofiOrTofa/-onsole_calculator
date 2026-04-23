from calc_pkg import nodes


signs = nodes.MathSigns()


@signs.add("+", 1)
class Sum(nodes.MathSignsAbstract):
    def __init__(self, first_operand:object, second_operand:object)->None:
        self._fo : object = first_operand
        self._so : object = second_operand
    def score(self):
        return self._fo.score() + self._so.score()
@signs.add("-", 1)
class Difference(nodes.MathSignsAbstract):
    def __init__(self, first_operand:object, second_operand:object)->None:
        self._fo = first_operand
        self._so = second_operand
    def score(self)->object:
        return self._fo.score() - self._so.score()
@signs.add("*", 2)
class Product(nodes.MathSignsAbstract):
    def __init__(self,
        first_operand  : object,
        second_operand : object
    ):#>--------------------<#
        self._fo : object = first_operand
        self._so : object = second_operand
    def score(self):
        return self._fo.score() * self._so.score()
@signs.add("/", 2)
class Quotient(nodes.MathSignsAbstract):
    def __init__(self,
        first_operand  : object,
        second_operand : object
    ):#>--------------------<#
        self._fo : object = first_operand
        self._so : object = second_operand
    def score(self):
        return self._fo.score() / self._so.score()
@signs.add("%", 2)
class Ratio(nodes.MathSignsAbstract):
    def __init__(self,
        first_operand  : object,
        second_operand : object
    ):#>--------------------<#
        self._fo : object = first_operand
        self._so : object = second_operand
    def score(self):
        result = self._fo.score() / self._so.score()
        return result * nodes.ReducedFraction(100, 1)