from abc import ABC, abstractmethod
import json

class abstract_calculator(ABC):
    @abstractmethod
    def __init__(self): ...

    @abstractmethod
    def score(self): ...

# математическе действия>---------------------------------------------
class sum_calculate(abstract_calculator): ...

#главная часть>-------------------------------------------------------

def append_mathematical_sings(): ...

def compilate_list(expression, mathematical_sings, numbers):
    expression_list=list("")
    a=1
    for i in expression:
        if i in numbers and not a: expression_list[-1]+=i
        else:
            expression_list.append(i)
            if not a: a=1
            else: a=0
    print(expression_list)

def main():
    numbers=('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
    print("""
          выбирите действие:
            1.решить выражение
            2.построить график по функции
            3.история действий
          цифра:""", end=" ")
    a=int(input())
    if a==1:
        mathematical_sings:dict[str:list(str, int)]={}
        print("Введите выражение: ", end=" ")
        expression=input().strip()
        compilate_list(expression, mathematical_sings, numbers)
        
    elif a==2: ...
    elif a==3: ...

if __name__=='__main__':
    main()