#!/usr/bin/env -S python3 -u
"""-onsole colculator"""

from abc import ABC, abstractmethod
import json
import subprocess
import os

class abstract_calculator(ABC):

    @abstractmethod
    def score(self): ...

def add_mathematical_sd(math_sing:str, class_math_sing, math_significance:int):#это функция для добавления новых математисестких символов
    mathematical_sd[math_sing]=(class_math_sing, math_significance)


# функции математических действий>---------------------------------------------
class sum_calculate(abstract_calculator):
    def score(self, num_first, num_second):
        return num_first+num_second
class subtraction_calculate(abstract_calculator):
    def score(self, num_first, num_second):
        return num_first-num_second



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

class score_expression:
    def __init__(self, mathematical_sd):
        self.numbers : set
        self.expression : str
        self.expression_list : list
        self.Bexpression_start : int
        self.Bexpression_end : int
        self.Bexpression_len : int
        self.Bexpression_list : list           
        self.mathematical_sd : dict[str:list(class_sing_calculator, int)] = mathematical_sd
        self.two_expression : tuple(str, ...)

        #mathematical_sings:dict[str:list(str, int)]={}#знак:[класс, значимость]
        self.numbers=('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
        self.expression=input("Введите выражение: ").strip()
        self.expression_list=list()

        self.compilate_list()
        self.find_and_compilate_backets_expression()
        self.find_two_expression()
        self.score_two_expression()


    def find_and_compilate_backets_expression(self):
        for i in range(len(self.expression_list)):
            if self.expression_list[i]=="(": self.Bexpression_start=i
            elif self.expression_list[i]==")":
                self.Bexpression_end=i
                self.Bexpression_len=self.Bexpression_end-self.Bexpression_start+1
                #ответ поставится на место первой скобки, а остольное удалится, можно будет сделать ещё, что бы проверялось есть ли после скобки и до скобки цифра, и если есть, то пишется умножение
                self.Bexpression_list=self.expression_list[self.Bexpression_start+1:self.Bexpression_end]
                print(self.Bexpression_list)

                #нужно дописать, что бы функция вызывала функцию с решением,
                #которая будет решать пример в скобках как обычный и возвращать ответ ввиде числа
                  #(можно будет сделать, что бы она отправляла каждое действие в историю для функции развёрнутой истории), 
                
                #потом мы заменяем пример вместе со скобками из обычного примера на полученное число 
                #после, когда эта функция будет подходить к концу,
                #она должна проверять остались ли ещё скобки в примере, и если остались, то она 
                #два варианта:
                  #в первом он должен вызвать сам себя сделав что-то типо рекурсии.
                  #а во втором он должен вернуть какое-нибудь число, или строку, обозначающую, что его надо вызвать повторно

    def find_two_expression(self):
        a=1
        for i in range(len(self.Bexpression_list)):
            if self.Bexpression_list[i] in self.mathematical_sd and self.mathematical_sd[self.Bexpression_list[i]][1]==a:
                self.two_expression:tuple(str, ...)=(self.Bexpression_list[i-1:i+2])
                return
    def score_two_expression(self):
        #print(self.mathematical_sd[self.two_expression[1]][0](int(self.two_expression[0]), int(self.two_expression[2])))
        print(self.two_expression[0], self.two_expression[2])
        print(self.mathematical_sd[self.two_expression[1]][0].score(int(self.two_expression[0]), int(self.two_expression[2])))
    def compilate_list(self):
        a=0
        for i in self.expression:
            if i in self.numbers:
                if not a or a==3: self.expression_list.append(i); a=1
                elif a: self.expression_list[-1]+=i
            elif i=="(" or i==")": self.expression_list.append(i); a=3
            else:
                if a: self.expression_list.append(i); a=0
                else: self.expression_list[-1]+=i
        print(self.expression_list)





def connection_json():
    with open('back/history.json', 'r', encoding='utf-8') as f:
        history = json.load(f)

def manu():
    a=0
    print("""
        выбирите действие:
            1.решить выражение
            2.построить график по функции
            3.история действий
            4.выход
          цифра:""", end=" ")
    while a>3 or a<=0:
        a=int(input())
        if a==1 or a==2 or a==3: return a
        elif a==4: return exit
        else:
            print("""
        вы ошиблись выберите ещё раз:
            1.решить выражение
            2.построить график по функции
            3.история действий
            4.выход
        цифра:""", end=" ")
def main():
    choice=manu()
    if choice == 1:
        #здесь можно вызывать функцию для добавления новых математических символов
        add_mathematical_sd("+", sum_calculate(), 1)

        score_expression(mathematical_sd)
    

if __name__=='__main__':
    mathematical_sd:dict[str:tuple()]={}
    system()
    main()
