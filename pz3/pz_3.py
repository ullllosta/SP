# -*- coding: cp1251 -*-
from math import factorial

import time
import numpy
import threading
from threading import *
print(" �������� �����: 4 � 7")
def cal_factor(num):
    print(' 1.��������� ��������� �������� �����')
 
    for n in ar_one:
        
        outcome = numpy.math.factorial(n)

      
        with open('factorial.txt','w+',encoding='utf-8')as file:

            file.write(f"���������: {outcome}\n")
        time.sleep(0.3)
        print(f' ��������� :  {outcome}')
        
def cal_step(num):
    print(' 2.��������� ����� N � ������� N �������� �����')
    for n in ar_one:

        outcome2 = n**n
        with open('stepen.txt','w+',encoding='utf-8')as file:
            file.write(f"�������   : {outcome2}\n")
        time.sleep(0.32)
        print(f' �������   : {outcome2}')

with open('result.txt', 'w+', encoding='windows-1251') as fil:
    f1 = open('factorial.txt','r')
    f2 = open('stepen.txt','r')
    print( f1.read(), '\n', f2.read(), '\n', file=fil)


ar_one = [4] # ������ ������
ar_two = [7] # ������ ������


t = time.time() # ��������� ������ ������� ��� ���������� �������

th1 = threading.Thread(target=cal_factor, args=(ar_one, ))
th2 = threading.Thread(target=cal_step, args=(ar_one, ))

th1.start()
th2.start()

th1.join()
th2.join()
print(" ����� �����, ���������� ��������, ���������� :", time.time() - t)
print(" ����� 1 � ����� 2 ��������� ���� ������.")