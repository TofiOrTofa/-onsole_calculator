from dataclasses import dataclass, asdict

@dataclass( frozen = True )
class Result:
    state: bool
    value: str

@dataclass( frozen = True )
class Menu:

    @property
    @staticmethod
    def expression(user_expression: str) -> str: ...

    @property
    @staticmethod
    def history() -> str: ...


def print_menu() -> List[str]:
    user_choice = []
    for option in asdict(Menu).keys():

def check_choice(user_choice) -> str:
    match user_choice:
        case 1:
            return "expression"
        case 2:
            return ""
        case 3:
            return "history"
        case 4:
            return "exit"
        case _:
            raise KeyError(f"получен ключь {user_choice}\n\
                ожидался от 1 до 4")

def show_and() -> str:
    print("""
выбирите действие>-----------------------------
                  1.решить выражение
                  2.построить график по функции
                  3.история действий
                  4.выход """)
    user_choice=input("цифра: ")
    return check_choice(user_choice)
