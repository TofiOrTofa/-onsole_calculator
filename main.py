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
    def __init__(self, mathematical_sd, expression):
        self.numbers : set
        self.expression : str
        self.expression_list : list
        self.SaveExpression : tuple         
        self.mathematical_sd : dict[str:list(class_sing_calculator, int)]
        self.TwoExpression : tuple(str, ...)
        self.TwoExpression_start : int
        self.backets : list#наличие скобок в примере
        self.answer : int or float
        self.sorterMathSing : list

        self.mathematical_sd = mathematical_sd
        #mathematical_sings:dict[str:list(str, int)]={}#значимость:[класс, знак]
        self.numbers = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
        self.expression = expression
        self.expression_list=list()
        self.backets = []

    def main(self):
        print("start -------------")
        self.compilateList()
        print("self.backets", self.backets)
        while self.backets:
            self.backetsResult = score_expression(
                self.mathematical_sd,
                self.expression_list[self.backets[0]][1:-1]
            ).main()
            self.replacementBacketExpression()
            print("self.backetsResult", self.backetsResult)
        while len(self.expression_list) != 1:
            self.findTwoExpression()
            self.scoreTwoExpression()
            self.removeTwoExpression()
        print("self.expression_list", self.expression_list)
        print("end ---------------------")
        return self.expression_list[0]


    def findTwoExpression(self):
        a=1
        for i in range(len(self.expression_list)):
            print(f"self.expression_list[{i}]", self.expression_list[i])
            if self.expression_list[i] in self.mathematical_sd:
                testImportanceMathSing = (
                    self.mathematical_sd[self.expression_list[i]][1] == a
                )
            else: testImportanceMathSing = False

            if testImportanceMathSing:
                self.TwoExpression = (
                    self.expression_list[i-1:i+2]
                )
                self.TwoExpression_start = i - 1
                return 0
        print("aaa")


    def scoreTwoExpression(self):
        self.answer=self.mathematical_sd[self.TwoExpression[1]][0].score(
            self.mathematical_sd[self.TwoExpression[1]][0].compilate(
                self.TwoExpression[0], self.TwoExpression[2]
            )
        )
        print(self.answer)


    def removeTwoExpression(self):
        del self.expression_list[
            self.TwoExpression_start+1:self.TwoExpression_start+3
        ]
        self.expression_list[self.TwoExpression_start] = self.answer
        print(self.expression_list)
    def replacementBacketExpression(self):
        self.expression_list[
            self.backets[0]
        ] = self.backetsResult
        del self.backets[0]
        print("self.expression_list", self.expression_list)

    @staticmethod
    def noneMathSing(breakMathSing): 
        print("\n\t",
            "символ", 
            "\"%s\"" % breakMathSing,
            "неизвестен",
            sep=" "
        )
        exit()


    def compilateList(self):
        #                                                                        flag == 0 - скобочное вырожение
        #                                                                        flag == 1 - цифра
        #                                                                        flag == 2 - плавающая точка
        #                                                                        flag == 4 - математический знак
        flag = 0
        count = 0
        while count < len(self.expression):
            if self.expression[count] in self.numbers:#                          числа
                if not flag or flag == 4:
                    self.expression_list.append(
                        self.expression[count]
                    ); flag = 1
                elif flag: 
                    self.expression_list[-1] += self.expression[count] 
            elif (#                                                              плавающие точки
                self.expression[count] == "." or 
                self.expression[count] == ","
            ):  self.expression_list[-1] += self.expression[count]; flag = 2
            elif self.expression[count] == "(": #                                скобки
                self.expression_list.append(self.expression[count])
                while self.expression[count] != ")": 
                    count += 1
                    self.expression_list[-1] += self.expression[count]
                flag = 0
                self.backets.append(len(self.expression_list) - 1)
            elif self.expression[count] in mathematical_sd:#                     математические знаки
                if flag in (0, 1): 
                    self.expression_list.append(self.expression[count])
                else: self.expression_list[-1] += self.expression[count]
                flag = 4
            else: self.noneMathSing(self.expression[count])
            count += 1
def request_expression():
    return input("Введите выражение: ").strip()





def connection_json():
    with open('back/history.json', 'r', encoding='utf-8') as f:
        history = json.load(f)

def manu():
    a = 0
    while a > 3 or a <= 0:
        print("""
выбирите действие>-----------------------------
                  1.решить выражение
                  2.построить график по функции
                  3.история действий
                  4.выход """)
        userChoice=int(input("цифра: "))
        if userChoice in (1, 2, 3): return userChoice
        elif userChoice == 4: return exit()
        else:
            system()
            print("вы ошиблись")
def main():
    choice = manu()
    if choice == 1:
        #здесь можно вызывать функцию для добавления новых математических символов
        add_mathematical_sd("+", sum_calculate(), 1)
        add_mathematical_sd("-", subtraction_calculate(), 1)

        result = score_expression(mathematical_sd, request_expression()).main()
    

if __name__=='__main__':
    mathematical_sd:dict[str:tuple()]={}
    system()
    main()
