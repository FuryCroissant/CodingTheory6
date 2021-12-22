import numpy as np
import itertools

k1 = 4
n1 = 7
g1 = np.array([1, 0, 1, 1])#порождающий многочлен

k2 = 9
n2 = 15
g2 = np.array([1, 0, 0, 1, 1, 1, 1])#порождающий многочлен

def Encode1(input):
    c = np.array([0, 0, 0, 0, 0, 0, 0])
    for i in range(0, k1):
        if input[i] == 1:
            c[i:i + 4] ^= g1
    return c

def Remainder1(input):
    r = input.copy()
    for i in range(n1 - 1, n1 - k1 - 1, -1):
        if r[i] == 1:
            r[i - (n1 - k1): i + 1] ^= g1
    return r

def WH(a):  # расчёт веса Хэмминга
    wt = 0
    for i in range(int(len(a))):
        if (a[i]):
            wt += 1
    return wt

def Decode1(w):
    s = Remainder1(w)
    for i in range(n1):
        s1 = np.roll(s, i)
        ss =Remainder1(s1)
        if WH(ss)<=count_er:
            x = np.roll(ss, n1 - i)
            return x^w

def Encode2(input):
    c2 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    for j in range(0, k2):
        if input[j] == 1:
            c2[j:j + 7] ^= g2
    return c2
def Remainder2(input):
    r = input.copy()
    for i in range(n2 - 1, n2 - k2 - 1, -1):
        if r[i] == 1:
            r[i - (n2 - k2): i + 1] ^= g2
    return r
def Decode2(w):
    s = Remainder2(w)
    for i in range(n2):
        s1 = np.roll(s, i)
        ss = Remainder2(s1)
        for e in range(len(E)):
            if np.array_equal(E[e], ss):
                x = np.roll(ss, n2 - i)
                return x^w


print("ЧАСТЬ 1")
#входящая посл-ть
a = [1, 0, 0, 1]
print(a)
A = Encode1(a)
print("Закодированное сообщение", A)
encod = A.copy()
#кол-во ошибок от 1 до 3
while True:
    count_er = int(input("Количество ошибок?: "))
    if not 1 <= (count_er) <= 3:
        print("Попробуйте снова")
    else:
        print(count_er)
        break
mas_er2=[]
z=0
#последовательно вносим ошибки
while z < count_er:
    i = int(input("В какой бит внести ошибку?: "))
    if not 0 <= (i) < n1: #не выходим за границы сообщения
        print("Число не в диапазоне, попробуйте снова")
        i = int(input("В какой бит внести ошибку?: "))
    elif i in mas_er2:
        print("Число ранее было задано,попробуйте снова")#е меняем один и тот же бит несколько раз
        i = int(input("В какой бит внести ошибку?: "))
    else:
        print("i =", i)
        mas_er2.append(i)#запоминаем номер бита для проверки
        encod[i] = not encod[i]#еняем бит
        print("Cлово с ошибкой в бите",i,":", encod)
    z+=1
de = Decode1(encod)
print(de)

print("ЧАСТЬ 2")
E = []
e1 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
e2 = [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
e3 = [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
e4 = [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
E.append(e1)
E.append(e2)
E.append(e3)
E.append(e4)
for i in range(1, 15):
    e1 = np.roll(e1, 1)
    e2 = np.roll(e2, 1)
    e3 = np.roll(e3, 1)
    e4 = np.roll(e4, 1)
    E.append(e1)
    E.append(e2)
    E.append(e3)
    E.append(e4)

b = [1, 0, 0, 1, 0, 0, 0, 1, 1]
print(b)
B = Encode2(b)
print("Закодированное сообщение", B)
encod1 = B.copy()
#кол-во ошибок от 1 до 4
while True:
    count_er1 = int(input("Количество ошибок?: "))
    if not 1 <= (count_er1) <= 4:
        print("Попробуйте снова")
    else:
        print(count_er1)
        break
mas_er3=[]
z1=0
#последовательно вносим ошибки
while z1 < count_er1:
    i = int(input("В какой бит внести ошибку?: "))
    if not 0 <= (i) < n2: #не выходим за границы сообщения
        print("Число не в диапазоне, попробуйте снова")
        i = int(input("В какой бит внести ошибку?: "))
    elif i in mas_er3:
        print("Число ранее было задано,попробуйте снова")#е меняем один и тот же бит несколько раз
        i = int(input("В какой бит внести ошибку?: "))
    else:
        print("i =", i)
        mas_er3.append(i)#запоминаем номер бита для проверки
        encod1[i] = not encod1[i]#еняем бит
        print("Cлово с ошибкой в бите",i,":", encod1)
    z1+=1
de1 = Decode2(encod1)
print(de1)
