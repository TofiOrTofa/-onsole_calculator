#!/usr/bin/env -S python3 -u
"""-onsole colculator"""

from parser import *
import subprocess
import os


def system():
    #очистка терминала>----------------
    if os.name == "nt":
        command=['cls']
    else:
        command=['clear']
    subprocess.run(command, shell=True)
    #>---------------------------------
def manu():
    a=0
    while a>3 or a<=0:
        print("""
выбирите действие>-----------------------------
                  1.решить выражение
                  2.построить график по функции
                  3.история действий
                  4.выход """)
        userChoice=int(input("цифра: "))
        if userChoice in (1, 2, 3): return userChoice
        elif userChoice==4: return exit()
        else:
            system()
            print("вы ошиблись")
def main():
    choice=manu()
    if choice == 1:
        math_signs = MathSignsInfo()
        #вызыов функции для добавления новых математических символов
        math_signs.add("+", Sum, 1)
        math_signs.add("-", Difference, 1)
        math_signs.add("*", Product, 2)
        math_signs.add("/", Quotient, 2)
        math_signs.add("%", Ratio, 2)

        expression_objects = Expression(
            math_signs,
            input("Введите выражение: ")
        )
        result = expression_objects.score()
        print("Ответ:", result)
    

if __name__=='__main__':
    system()
    main()
