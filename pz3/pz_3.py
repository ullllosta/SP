# -*- coding: cp1251 -*-
from math import factorial

import time
import numpy
import threading
from threading import *
print(" Заданные числа: 4 и 7")
def cal_factor(num):
    print(' 1.Вычислить факториал заданных чисел')
 
    for n in ar_one:
        
        outcome = numpy.math.factorial(n)

      
        with open('factorial.txt','w+',encoding='utf-8')as file:

            file.write(f"Факториал: {outcome}\n")
        time.sleep(0.3)
        print(f' Факториал :  {outcome}')
        
def cal_step(num):
    print(' 2.Вычислить число N в степени N заданных чисел')
    for n in ar_one:

        outcome2 = n**n
        with open('stepen.txt','w+',encoding='utf-8')as file:
            file.write(f"Степень   : {outcome2}\n")
        time.sleep(0.32)
        print(f' Степень   : {outcome2}')

with open('result.txt', 'w+', encoding='windows-1251') as fil:
    f1 = open('factorial.txt','r')
    f2 = open('stepen.txt','r')
    print( f1.read(), '\n', f2.read(), '\n', file=fil)


ar_one = [4] # данный массив
ar_two = [7] # данный массив


t = time.time() # получиние общего времени для выполнения функций

th1 = threading.Thread(target=cal_factor, args=(ar_one, ))
th2 = threading.Thread(target=cal_step, args=(ar_one, ))

th1.start()
th2.start()

th1.join()
th2.join()
print(" Общее время, занимаемое потоками, составляет :", time.time() - t)
print(" Поток 1 и поток 2 завершили свою работу.")