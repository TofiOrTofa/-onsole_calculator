from abc import ABC, abstractmethod
import json
import subprocess
import os

class abstract_calculator(ABC):
    @abstractmethod
    def __init__(self): ...

    @abstractmethod
    def score(self): ...

# математическе действия>---------------------------------------------
class sum_calculate(abstract_calculator): ...
class subtraction_calculate(abstract_calculator): ...

#главная часть>-------------------------------------------------------

def append_mathematical_sings(): ...



def system():
    #очистка терминала>----------------
    if os.name == "nt":
        command=['cls']
    else:
        command=['clear']
    subprocess.run(command, shell=True)
    #>---------------------------------

def choice_expression(numbers):
    def compilate_list(expression, numbers):
        expression_list=list()
        a=0
        for i in expression:
            if i in numbers:
                if not a: expression_list.append(i); a=1
                elif a: expression_list[-1]+=a
            else:
                if a: a=0
                expression_list.append(i)
        print(expression_list)
        return expression_list
    def find_two_expression(mathematical_sings, expression_list):
        backets=False
        pass#недоделанно
    
    mathematical_sings:dict[str:list(str, int)]={}#функция:[знак, значимость]
    print("Введите выражение: ", end=" ")
    expression=input().strip()
    expression_list=compilate_list(expression, numbers)
    find_two_expression(mathematical_sings, expression_list)



def manu():
    a=0
    print("""
        выбирите действие:
            1.решить выражение
            2.построить график по функции
            3.история действий
          цифра:""", end=" ")
    while a>3 or a<=0:
        a=int(input())
        if a==1 or a==2 or a==3: return a
        else:
            print("""
        вы ошиблись выберите ещё раз:
            1.решить выражение
            2.построить график по функции
            3.история действий
        цифра:""", end=" ")
def main():
    numbers=('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
    choice=manu()
    if choice == 1:
        choice_expression(numbers)
    

if __name__=='__main__':
    system()
    main()