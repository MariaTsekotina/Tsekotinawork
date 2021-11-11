from random import *

loom=input("Купи слона!")
while loom.title()!="Слон": #upper(),lower()
    loom=input("Все говорят"+loom+"! А ты купи!!!")
print("Слон твой!!!")













































# 6
from random import *
N=int(input("Mitu: "))
p=n=o=0
while N>0:
    N-=1
    B=randint(-100,100)
    print(B)
    if B>0:
        p+=1
    elif B<0:
        n+=1
    else:
        o+=1
print("Pos:",p)
print("Neg:",n)
print("Nullid:",o)








# 4
for i in range(10,20):

   print(i**2)
print("Ruut on")









# 3
from random import *
korrutis=1
for i in range(8):
    B=randint(-100,100)
    print(B)
    if B>0: korrutis*=B
print("Korrutis on",korrutis)


















#1...A
A=10
s=0
for arv in range(1,A+1):
    print(arv)
    s+=arv
print("Summa",s)

























t=0 #arvude kogus
q=0 # int
while t<15:
    t+=1
    a=float(input("Sisesta arv:"))
    if a==round(a): q+=1
print("Täisarvude kogus:" ,q)
# 1 for abil
for t in range(15):
    a=float(input("Sisesta arv:"))
    if a==round(a): q+=1
print("Täisarvude kogus:" ,q)




for i in range(5):
    print("Hello World!!!")

print("WHILE TRUE")
k=0
while True:
    k+=1
    print("Hello World!!!")
    if k==5: break
print("WHILE Tingimusega")
k=0
while k>5:
    print("Hello World!!!")
    k+=1

