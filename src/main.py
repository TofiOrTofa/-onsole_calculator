#!/usr/bin/env -S python3 -u
"""-onsole colculator"""

import subprocess
import os

from calc_pkg import parser
from calc_pkg import nodes


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
        math_signs = nodes.MathSigns()
        #вызыов функции для добавления новых математических символов
        math_signs.add("+", nodes.Sum, 1)
        math_signs.add("-", nodes.Difference, 1)
        math_signs.add("*", nodes.Product, 2)
        math_signs.add("/", nodes.Quotient, 2)
        math_signs.add("%", nodes.Ratio, 2)

        expression_objects = parser.Expression(
            math_signs,
            input("Введите выражение: ")
        )
        result = expression_objects.score()
        print("Ответ:", result)


if __name__=='__main__':
    system()
    main()
