import random 
import os
from time import sleep 
import sys
import re

a=[1,2,3,4,5,6,7,8]
x1,x2,x3,x4,x5,x6,x7,v=0,0,0,0,0,0,0,0

def clr():
    os.system('cls' if os.name == 'nt' else 'clear')


def nachalo(v,h):
    
    h1='txt Edition v3.0 Beta'
    if v==1:
        print( '\n'*5, ' '*13,' ДОБРО ПОЖАЛОВАТЬ В РУССКУЮ РУЛЕТКУ\n',' '*22,h1,'\n1. начать\n2. закончить')
    else:
        h='\n'*4
        print(h)
        print(' '*15,end='')
        h=' ДОБРО ПОЖАЛОВАТЬ В РУССКУЮ РУЛЕТКУ'
        for i in h:
            print(i, end='')
            sys.stdout.flush()
            sleep(0.05)
        print()
        print(' '*22,end='')
        for i in h1:
            print(i, end='')
            sys.stdout.flush()
            sleep(0.05)
        h='\n1. начать\n2. закончить'
        for i in h:
            print(i, end='')
            sys.stdout.flush()
            sleep(0.05)
        print()


def mat(zte):
    if len(zte)>3:
        slo=r'(Блядь|пиздец|нахуй|нахер|нахрен|пизду|долбаеб|сука)'
        if re.search(slo, zte):
            raise NameError("мат запрещён")


def znachen():
    global o
    if n==2: o=1
    elif n==3: o=-2
    elif n==4: o=-5
    elif n==5: o=-9
    elif n==6: o=-14
    elif n==7: o=-20
    elif n==8: o=-27


def podschot():
    global s
    s=[]
    for i in range(n):
        s.insert(i,i+1)

def igrocy(x1):
    global n
    while x1==0:
        
        clr()
        n=input('Ввидите количество игроков:')
        mat(n)
        try: n=int(n)
        except: continue
        if not (n>1) and (n<9): continue
        else: break
        
        
def imena(x2):
    global a
    clr()
    while x2==0:
        print('Ввидите имена:')
        for i in range(1,n+1):
            m=str(input(str(i)+' игрок: '))
            mat(m)
            if m=='':
                m=str(i)
            a[i-1]=m
        x2=1

def vibor(x1,x2):
    igrocy(x1)
    znachen()
    podschot()
    imena(x2)
    
def test_rul():
    global a1
    a1=a
    n1=n
    r = 1
    kr=1
    clr()

    s=[]
    for i in range(n):
        s.insert(i,i+1)

    while n1>0:
        g=random.randint(1,8)
        #print(g)
        print('')
        print(r,'раунд')
        while g>n1:
            print("\n",kr,'круг')
            
            for i in range(n1):
                print(' ' ,a1[i],'жив')
            g-=n1
            kr+=1
            #print(s)
            #print(g)
        print('\n',kr,'круг')
        
        for i in range(n1):
            if g==s[i]:
                print(' ',a1[i],'убит')
                s[i]=-1
                kr=0
                break 
            elif s[i]==-1: continue
            else: print(' ',a1[i],'жив')
        
        a2=[]
        for i in range(n1):
            if not s[i]==-1:
                a2.append(a1[i])
        a1=a2
        n1-=1
        kr+=1
        r+=1
        s=[]
        for i in range(n1):
            s.insert(i,i+1)
        if n1==1:
            break
        #print(a1,s)

def pobeda():
    print('\n'*3)
    print('!!!! ПОБЕДИТЕЛЬ !!!!')
    print(a1[0])



v1=1
def menu(v):
    clr()
    if v==1:
        print('1. Начать заново\n2. изменить режим\n3. выйти в главное меню')
    else:
        h='1. Начать заново\n2. изменить режим\n3. выйти в главное меню'
        for i in h:
            print(i, end='')
            sys.stdout.flush()
            sleep(0.05)
        print()
        v=1
        
        
        #111
def podmenu1(v1):
    global x1,x2,x3,x5,x6,r1
    while True:
        clr()
        if v1==1:
            print('1. Изменить имена\n2. Изменить количество игроков (имена изменятся также)\n3. ничего не изменять\n4. назад')
        else:
            h= '1. Изменить имена\n2. Изменить количество игроков (имена изменятся также)\n3. ничего не изменять\n4. назад'
            for i in h:
                print(i, end='')
                sys.stdout.flush()
                sleep(0.05)
            print()
            v1=1
        
        r1=input()
        mat(r1)
        try: r1=int(r1)
        except: continue
        if (r1<1) and (r1>4): continue
        
        if r1 == 1:
            x1,x2,x3,x6=1,0,1,0
            break
        elif r1 == 2:
            x1,x2,x3,x6=0,0,1,0
            break
        elif r1 == 3:
            x1,x2,x3,x5,x6=1,1,1,1,0
            break
        elif r1 == 4:
            x3,x6 = 0,0
            break
        else:
            continue
            
            #222
def podmenu2(v1):
    global x1,x2,x3,x5,x6,r1
    while True:
        clr()
        if v1==1:
            print('1. Изменить имена\n2. Изменить количество игроков (имена изменятся также)\n3. ничего не изменять\n4. назад')
        else:
            h= '1. Изменить имена\n2. Изменить количество игроков (имена изменятся также)\n3. ничего не изменять\n4. назад'
            for i in h:
                print(i, end='')
                sys.stdout.flush()
                sleep(0.05)
            print()
            v1=1
        
        r1=input()
        mat(r1)
        try: r1=int(r1)
        except: continue
        if (r1<1) and (r1>4): continue
        
        if r1 == 1: 
            x1,x2,x3,x5,x6=1,0,1,0,0
            break
        elif r1 == 2:
            x1,x2,x3,x5,x6=0,0,1,0,0
            break
        elif r1 == 3: 
            x1,x2,x3,x5,x6=1,1,1,0,0
            break
        elif r1 == 4: 
            x3,x5,x6=0,0,0
            break
        else:
            continue
        
        
        
        #3333
def podmenu3(v1):
    global x1,x2,x3,x4,x5,x6,x7,v,r2
    while True:
        clr()
        if v1==1: 
            print('Количество игроков и имена удалятся \nПродолжить?',end='')
        else: 
            h="Количество игроков и имена удалятся \nПродолжить?"
            for i in h: 
                print(i, end='') 
                sys.stdout.flush() 
                sleep(0.05)
        print()
        print('1. да\n2. нет')
        v1=1
        r2=int(input())
        mat(r2)
        try: r2=int(r2)
        except: continue
        if (r2<1) and (r2>2): continue
        
        if r2 == 1:
            x1,x2,x3,x5,x6,x7 = 0,0,1,0,0,1
            v=0 
            break
        elif r2 == 2: 
            x4,x6,x7 = 1,0,1
            break


def vsio_menu():
    x3=0 
    r=0 
    v=0
    r1,r2=0,0
    while True:
        menu(v)
        v=1
        v1=0
        r=input()
        mat(r)
        try: r=int(r)
        except: continue
        if (r<1) and (r>3): continue
        if r==1: podmenu1(v1)
        elif r==2: podmenu2(v1)
        elif r==3: podmenu3(v1)
        else: continue
        if r1==4 or r2==2: continue
        break
        #print(x1,x2,x3,x4,x5,x6,x7)







def ril_rul():
    global r,p,s
    while True:
        # выбор
        g = random.randint(1, 8)
        for i in range(n):
            k=5
            if s[i]== i-n:
                continue
            while True:
                while True:
                    clr()
                    print(r, 'раунд')
                    print(' ', a[i], "\n\n1. выстрелить\n2. прокрутить и выстрелить")
                    if k>0:
                        print('3. прокрутить только',k,'раз')
                        try:
                            d = int(input())
                            if (d>0) and (d<4):
                                break
                            else:
                                continue
                        except:
                            continue
                    else:
                        try:
                            d = int(input())
                            if (d==1) or(d==2):
                                break
                            else:
                                continue
                        except:
                            continue
                # выстрел
                if d == 1:
                    clr()
                    print(r, 'раунд  ')
                    print(' ', a[i], end=' ')
                    if g == s[i]:
                        print('убит')
                        s[i] = i-n
                        sleep(1)
                        break
                    elif s[i] == i-n:
                        break
                    else:
                        print('жив')
                    sleep(1)
                    break
                # прокрутка и выстрел
                elif d == 2:
                    clr()
                    print('прокрутка барабана')
                    sleep(1)
                    g = random.randint(1, 8)
                    clr()
                    print(r, 'раунд  ')
                    print(' ', a[i], end=' ')
                    if g == s[i]:
                        print('убит')
                        s[i] = i-n
                        sleep(1)
                        break
                    elif s[i] == i-n:
                        break
                    else:
                        print('жив')
                    sleep
                    break
                # прокрутка
                elif d == 3:
                    clr()
                    print('прокрутка барабана')
                    sleep(1)
                    g = random.randint(1, 8)
                    k-=1
                    continue
        #вывод
        clr()
        print(r, 'раунд')
        for i in range(n):
            if s[i]== i-n:
                continue
            print(' ', a[i], end=' ')
            if s[i] < 0:
                print('убит')
            else:
                print('жив')
        sleep(2)
        # подсчет
        p=0
        for i in range(n):
            p += s[i]
        r += 1
        # сравнение
        if p==o:
            break
        else:
            continue
