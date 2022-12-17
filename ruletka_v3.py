import random 
import os
from time import sleep 
import sys
from pom import *
import re



v=1
x,x5,x1,x2,h=0,0,0,0,0
#x1,x2,x3,x4,x5,x6,x7,v=0,0,0,0,0,0,0,0
while x==0:
    clr()
    nachalo(v,h)
    v=1
    r=input()
    mat(r)
    try:
        r=int(r)
    except:
        continue
    if not ((r>0) and (r<3)) or ((r>10) and (r<13)):
        continue
    clr()
    if r == 1:
        x7=0 
        while x7==0 :
            x6=0 
            #print(x1,x2,x3,x4,x5,x6,x7,v)
            while x6==0 :
                r=1
                vibor(x1,x2)
                test_rul()
                pobeda()
                x6=-1
                print('Нажмите ENTER чтобы продолжить')
                input()
            vsio_menu()
    elif r==2 :
        x=1
        with open('titry.txt') as tit:
            print(tit.read())
    elif r==11 or r==12:
        x7=0
        if r==11:
            print('этот режим недоделан и имеет множество недостатков')
            sleep(4)
            clr()
            print('приятной игры')
            sleep(1)
        while x7==0:
            x6=0
            while x6==0:
                r=1
                vibor()
                if n==2:
                    o=0
                ril_rul()
                pobeda()
                print('Нажмите ENTER чтобы продолжить')
                input()
                break
            
            x3=0
            r=0
            v=0
            while x3 ==0:
                clr()
                if v==1:
                    print('1. Начать заново\n2. выйти в главное меню')
                else:
                    h='1. Начать заново\n2. выйти в главное меню'
                    for i in h:
                        print(i, end='')
                        sys.stdout.flush()
                        sleep(0.05)
                    print()
                    v=1
                try:
                    r=int(input())
                except:
                    continue
                if r==1:
                    v1=0
                    podmenu1(v1)
                elif r ==2:
                    v1=0
                    podmenu3(v1)
                else:
                    continue
    else:
        continue
