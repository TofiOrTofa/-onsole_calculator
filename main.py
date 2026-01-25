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

def add_mathematical_sd(math_sing:str, class_math_sing, math_significance:int):#это функция для добавления новых математисестких символов
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
class sum_calculate(abstract_calculator, compilate_string):#класс для сложения чисел
    def compilate(self, num_first, num_second):
        return super().compilate_sif(num_first, num_second)
    def score(self, nums):
        return str(nums[0]+nums[1])
class subtraction_calculate(abstract_calculator, compilate_string):#класс для вычитания чисел
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
        self.mathematical_sd : dict[str:list(class_sing_calculator, int)] = mathematical_sd
        self.TwoExpression : tuple(str, ...)
        self.TwoExpression_start : int
        self.backets : bool#наличие скобок в примере
        self.answer : int or float

        #mathematical_sings:dict[str:list(str, int)]={}#знак:[класс, значимость]
        self.numbers={'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
        self.expression=input("Введите выражение: ").strip()
        self.expression_list=list()
        self.TimeExpression_list=list()

        self.compilate_list() 
        self.find_Bexpression()
        if self.backets: 
            self.SaveExpression=tuple(self.expression_list)
            self.compilate_Bexpression()
        else:
            self.backets=False
            self.TimeExpression_list=self.expression_list
            self.TimeExpression_start=0
        while len(self.TimeExpression_list)!=1:
            self.find_TwoExpression()
            self.score_TwoExpression()
            self.rm_TwoExpression()
        print(self.expression_list)


    def find_Bexpression(self):
        if "(" in self.expression_list:
            self.TimeExpression_start=self.expression_list.index("(")
            self.TimeExpression_end=self.expression_list.index(")")
            self.backets=True
        else: self.backets=False
        #for i in range(len(self.expression_list)):
        #    if self.expression_list[i]=="(": self.TimeExpression_start=i
        #    elif self.expression_list[i]==")":
        #        self.TimeExpression_end=i
        #        #ответ поставится на место первой скобки, а остольное удалится, можно будет сделать ещё, что бы проверялось есть ли после скобки и до скобки цифра, и если есть, то пишется умножение
        #        return
                #print(self.TimeExpression_list)

                #нужно дописать, что бы функция вызывала функцию с решением,
                #которая будет решать пример в скобках как обычный и возвращать ответ ввиде числа
                  #(можно будет сделать, что бы она отправляла каждое действие в историю для функции развёрнутой истории), 
                
                #потом мы заменяем пример вместе со скобками из обычного примера на полученное число 
                #после, когда эта функция будет подходить к концу,
                #она должна проверять остались ли ещё скобки в примере, и если остались, то она 
                #два варианта:
                  #в первом он должен вызвать сам себя сделав что-то типо рекурсии.
                  #а во втором он должен вернуть какое-нибудь число, или строку, обозначающую, что его надо вызвать повторно
    def compilate_Bexpression(self):
        self.TimeExpression_list=self.expression_list[self.TimeExpression_start+1:self.TimeExpression_end]
    def rm_Bexpression(self): ...

    def find_TwoExpression(self):
        a=1
        for i in range(len(self.TimeExpression_list)):
            if self.TimeExpression_list[i] in self.mathematical_sd and self.mathematical_sd[self.TimeExpression_list[i]][1]==a:
                self.TwoExpression:tuple(str, ...)=(self.TimeExpression_list[i-1:i+2])
                self.TwoExpression_start=i-1
                return
    def score_TwoExpression(self):
        #print(self.TwoExpression[0], self.TwoExpression[2])
        #print(self.mathematical_sd[self.TwoExpression[1]][0].compilate(self.TwoExpression[0], self.TwoExpression[2]))
        self.answer=self.mathematical_sd[self.TwoExpression[1]][0].score(self.mathematical_sd[self.TwoExpression[1]][0].compilate(self.TwoExpression[0], self.TwoExpression[2]))
        print(self.answer)
    def rm_TwoExpression(self):
        del self.TimeExpression_list[self.TwoExpression_start+1:self.TwoExpression_start+3]
        self.TimeExpression_list[self.TwoExpression_start]=self.answer
        print(self.TimeExpression_list)
    def compilate_list(self):
        a=0
        for i in self.expression:
            if i in self.numbers:
                if not a or a==3: self.expression_list.append(i); a=1
                elif a: self.expression_list[-1]+=i
            elif i=="(" or i==")": self.expression_list.append(i); a=3
            elif i=="." or i==",": self.expression_list[-1]+=i; a=4
            else:
                if not a or a==4: self.expression_list[-1]+=i
                else: self.expression_list.append(i); a=0






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
        a=int(input("цифра: "))
        if a==1 or a==2 or a==3: return a
        elif a==4: return exit
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
