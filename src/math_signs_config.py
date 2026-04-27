from calc_pkg import nodes


signs = nodes.MathSigns()


@signs("+", 1)
class Sum(nodes.MathSignsAbstract):
    def score(self):
        return self._fo.score() + self._so.score()
@signs("-", 1)
class Difference(nodes.MathSignsAbstract):
    def score(self)->object:
        return self._fo.score() - self._so.score()
@signs("*", 2)
class Product(nodes.MathSignsAbstract):
    def score(self):
        return self._fo.score() * self._so.score()
@signs("/", 2)
class Quotient(nodes.MathSignsAbstract):
    def score(self):
        return self._fo.score() / self._so.score()
@signs("%", 2)
class Ratio(nodes.MathSignsAbstract):
    def score(self):
        result = self._fo.score() / self._so.score()
        return result * nodes.ReducedFraction(100, 1)