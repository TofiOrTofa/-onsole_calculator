from calc_pkg import nodes


signs_type = nodes.Signs()


@signs_type("+", 1)
class Sum(nodes.MathSignsAbstract):
    _fo: nodes.Constant
    _so: nodes.Constant

    def score(self) -> nodes.ReducedFraction:
        return self._fo.score() + self._so.score()

@signs_type("-", 1)
class Difference(nodes.MathSignsAbstract):
    def score(self) -> nodes.ReducedFraction:
        return self._fo.score() - self._so.score()

@signs_type("*", 2)
class Product(nodes.MathSignsAbstract):
    def score(self) -> nodes.ReducedFraction:
        return self._fo.score() * self._so.score()

@signs_type("/", 2)
class Quotient(nodes.MathSignsAbstract):
    def score(self) -> nodes.ReducedFraction:
        return self._fo.score() / self._so.score()

@signs_type("%", 2)
class Ratio(nodes.MathSignsAbstract):
    def score(self) -> nodes.ReducedFraction:
        result: nodes.ReducedFraction = self._fo.score() / self._so.score()
        return result * nodes.ReducedFraction(100, 1)

