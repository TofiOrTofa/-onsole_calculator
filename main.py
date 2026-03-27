#!/usr/bin/env -S python3 -u
"""-onsole colculator"""

from abc import ABC, abstractmethod
import json
import subprocess
import os

class abstract_calculator(ABC):

    @abstractmethod
    def compilate(self): ...

    @abstractmethod
    def score(self): ...

def add_mathematical_sd(math_sing:str, class_math_sing, math_significance:int):
    #это функция для добавления новых математисестких символов
    mathematical_sd[math_sing]=(class_math_sing, math_significance)

# классы радители классов математических действий>----------------------------

class compilate_string:
    """функция для изменения вида переменных"""
    def compilate_sif(self, str_first, str_second):
        """меняет вид двух переменных из str в int или float"""
        if "." in str_first:
            str_first=float(str_first)
        else:
            str_first=int(str_first)
        if "." in str_second:
            str_second=float(str_second)
        else:
            str_second=int(str_second)
        #print(str_first, str_second)
        return str_first, str_second
        


# классы математических действий>---------------------------------------------
class sum_calculate(abstract_calculator, compilate_string):
    #класс для сложения чисел
    def compilate(self, num_first, num_second):
        return super().compilate_sif(num_first, num_second)
    def score(self, nums):
        return str(nums[0]+nums[1])
class subtraction_calculate(abstract_calculator, compilate_string):
    #класс для вычитания чисел
    def compilate(self, num_first, num_second):           
        return super().compilate_sif(num_first, num_second)
    def score(self, nums):
        return str(nums[0]-nums[1])



#главная часть>-------------------------------------------------------


def system():
    #очистка терминала>----------------
    if os.name == "nt":
        command=['cls']
    else:
        command=['clear']
    subprocess.run(command, shell=True)
    #>---------------------------------

class compilates:
    def __init__(self): ...

class score_expression:
    def __init__(self, mathematical_sd):
        self.numbers : set
        self.expression : str
        self.expression_list : list
        self.SaveExpression : tuple
        self.TimeExpression_list : list
        self.TimeExpression_start : int
        self.TimeExpression_end : int          
        self.mathematical_sd : dict[str:list(class_sing_calculator, int)]
        self.TwoExpression : tuple(str, ...)
        self.TwoExpression_start : int
        self.backets : bool#наличие скобок в примере
        self.answer : int or float
        self.sorterMathSing : list

        self.mathematical_sd = mathematical_sd
        #mathematical_sings:dict[str:list(str, int)]={}#значимость:[класс, знак]
        self.numbers={'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
        self.expression=input("Введите выражение: ").strip()
        self.expression_list=list()
        self.TimeExpression_list=list()
        self.main()

    def main(self):
        self.compilateList() 
        self.findBacketsExpression()
        if self.backets: 
            self.SaveExpression=tuple(self.expression_list)
            self.compilateBacketsExpression()
        else:
            self.backets=False
            self.TimeExpression_list=self.expression_list
            self.TimeExpression_start=0
        while len(self.TimeExpression_list)!=1:
            self.findTwoExpression()
            self.scoreTwoExpression()
            self.removeTwoExpression()
        print(self.expression_list)

    def sortMathSingByImportance(): ...


    def compilateBacketsExpression(self):
        self.TimeExpression_list=self.expression_list[
            self.TimeExpression_start+1:self.TimeExpression_end
        ]


    def findBacketsExpression(self):
        if "(" in self.expression_list:
            self.TimeExpression_start=self.expression_list.index("(")
            self.TimeExpression_end=self.expression_list.index(")")
            self.backets=True
        else: self.backets=False
    def findTwoExpression(self):
        a=1
        for i in range(len(self.TimeExpression_list)):
            
            if self.TimeExpression_list[i] in self.mathematical_sd:
                testImportanceMathSing=(
                    self.mathematical_sd[self.TimeExpression_list[i]][1] == a
                )
            else: testImportanceMathSing = False

            if testImportanceMathSing:
                self.TwoExpression:tuple(str, ...)=(
                    self.TimeExpression_list[i-1:i+2]
                )
                self.TwoExpression_start=i-1
                return 0
        return 1#вернёт 0 если найдёт выражения со скобками


    def scoreTwoExpression(self):
        self.answer=self.mathematical_sd[self.TwoExpression[1]][0].score(
            self.mathematical_sd[self.TwoExpression[1]][0].compilate(
                self.TwoExpression[0], self.TwoExpression[2]
            )
        )
        print(self.answer)


    def removeTwoExpression(self):
        del self.TimeExpression_list[
            self.TwoExpression_start+1:self.TwoExpression_start+3
        ]
        self.TimeExpression_list[self.TwoExpression_start]=self.answer
        print(self.TimeExpression_list)
    def removeBacketsExpression(self): ...

    @staticmethod
    def noneMathSing(breakMathSing): 
        print("\n\t",
            "символ", 
            f"'{breakMathSing}'",
            "неизвестен",
            sep=" "
        )
        exit()


    def compilateList(self):
        # a==0 - если только что была цыфра, обозначает математический знак
        # a==1 - если только что был знак, обозначает цифру
        # a==3 - обозначает скобку, что было до: не важно
        # a==4 - обозначает плавающую точку у числа, что было до: не важно
        a=0
        for i in self.expression:
            if i in self.numbers:
                if not a or a==3: self.expression_list.append(i); a=1
                elif a: self.expression_list[-1]+=i
            elif i=="(" or i==")": self.expression_list.append(i); a=3
            elif i=="." or i==",": self.expression_list[-1]+=i; a=4
            else:
                if i in self.mathematical_sd:
                    if not a or a==4: self.expression_list[-1]+=i
                    else: self.expression_list.append(i); a=0
                else: self.noneMathSing(i)






def connection_json():
    with open('back/history.json', 'r', encoding='utf-8') as f:
        history = json.load(f)

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
        #здесь можно вызывать функцию для добавления новых математических символов
        add_mathematical_sd("+", sum_calculate(), 1)
        add_mathematical_sd("-", subtraction_calculate(), 1)

        score_expression(mathematical_sd)
    

if __name__=='__main__':
    mathematical_sd:dict[str:tuple()]={}
    system()
    main()
