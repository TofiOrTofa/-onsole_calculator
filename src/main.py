#!/usr/bin/env -S python3 -u
"""-onsole colculator"""

import subprocess
import os

from calc_pkg.expression import parser
from math_signs_config import signs


def system():
    #очистка терминала>----------------
    if os.name == "nt":
        command='cls'
    else:
        command='clear'
    subprocess.run([command], check=False)
    #>---------------------------------
def menu():
    a=0
    while a>3 or a<=0:
        print("""
выбирите действие>-----------------------------
                  1.решить выражение
                  2.построить график по функции
                  3.история действий
                  4.выход """)
        userChoice=int(input("цифра: "))
        if userChoice in (1, 2, 3):
            return userChoice
        elif userChoice==4:
            return exit()
        else:
            system()
            print("вы ошиблись")
def main():
    choice=menu()
    if choice == 1:
        print("Ввидите выражение:", end="\n\t")
        user_expression = input()
        result = ""
        while user_expression:
            expression_objects = parser.Expression(
                signs,
                str(result)+user_expression
            )
            result = expression_objects.score()
            print("\n\t", result, sep="", end="")
            user_expression = input()
        system()
        print("\nОтвет:", result)


if __name__=='__main__':
    system()
    main()
