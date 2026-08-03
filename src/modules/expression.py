from calc_pkg.expression import compilate
from calc_pkg import nodes
import config# noqa: F401



def main():
    print("Ввидите выражение:", end="\n\t")
    user_expression = input()
    result = ""
    while user_expression:
        result_lexer = compilate.Lexer(
            str(result)+user_expression
        )
        result_parser = compilate.Parser(
            result_lexer
        )
        result = compilate.Evalator(
            result_parser
        )
        result = result.score()
        print("\n\t", result, sep="", end="")
        user_expression = input()
    system()
    print("\nОтвет:", result)



if __name__ == "__main__":
    system = nodes.System()
    system.terminal_clear()
    main()