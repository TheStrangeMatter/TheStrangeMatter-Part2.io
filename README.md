# TheStrangeMatter-Part2.
  
| номер | че как оно | 
| --- | --- |
| 1 | |
| 2 | |
| 3 | |
| 4 | |
| 5 | |
| 6 | |
| 7 | |
| 8 | |
| 9 | |
| 10 | |
| 11 | |
| 12 | |
| 13 | |
| 14 | |
| 15 | |
| 16 | |
| 17 | |
| 18 | |
| 19 | |
| 20 | |
| 21 | |
| 22 | |
| 23 | |
| 24 | |
| 25 | |
| 26 | |
| 27 | |
| 28 | |
| 29 | |
| 30 | |
| 31 | |
| 32 | |
| 33 | |
| 34 | |
| 35 | |
| 36 | |
| 37 | |
| 38 | |
| 39 | |
| 40 | |
| 41 | |
| 42 | |
| 43 | |
| 44 | |
| 45 | |
| 46 | |
| 47 | |
| 48 | |
| 49 | |
| 50 | |
| 51 | |
| 52 | |
| 53 | |
| 54 | |
| 55 | |
| 56 | |
| 57 | |
| 58 | |
| 59 | |
| 60 | |
| 61 | |
| 62 | |
| 63 | |
| 64 | |
| 65 | |
| 66 | |
| 67 | |
| 68 | |
| 69 | |
| 70 | |
| 71 | |
| 72 | |
| 73 | |
| 74 | |
| 75 | |
| 76 | |
| 77 | |
| 78 | |
| 79 | |
| 80 | |
| 81 | |
| 82 | |
| 83 | |
| 84 | |
| 85 | |
| 86 | |
| 87 | |
| 88 | |
| 89 | |
| 90 | |
| 91 | |
| 92 | |
| 93 | |
| 94 | |
| 95 | |
| 96 | |
| 97 | |
| 98 | |
| 99 | |
| 100 | |

```python
### 1

### 2
print('x y z w')
for x in range(2):
   for y in range(2):
      for z in range(2):
         for w in range(2):
            if (not(y<=x) or (z<=w) or not(z))==False:
               print(x, y, z, w)
x y z w
0 0 1 0
1 0 1 0
1 1 1 0

### 3

### 4


### 5

for i in range(1,100):
    chislo=''
    num=(bin(i)[2:])
    if num.count('1')%2==0:
        chislo='10'+num[2:]+'0'

    if num.count('1')%2!=0:
        chislo='11'+num[2:]+'1'
    if int(chislo,2)>40:
        print (i, int(chislo,2))
        break



for N in range(516):
  b = f'{N:b}'
    if N% 2 == 0:
      b += '10'
    else:
      b = '1' + b * '01'
    if int(b, 2) > 516:
      print(N)
      break



Организовать перебор чисел.
Перевести число в двоичную форму.
Проверить число по условиям.
Проверить число в скобках (строку, по условиям).
Проверить результат на условие и вывести его.

Найти минимальное число, которое после перевода в двоичную форму преобразовывается по правилу: 


#6
from turtle import *
left(90)
for i in range(7):
    forward(300)
    right(120)
pu()
for x in range(1,9):
    for y in range(1,10):
        goto(x*30,y*30)
        dot(5)
done()


Вспомнить команды черепашки
forward()
left/right
goto
pu() - хвост поднять 
dot() - ширина линии
done
Нарисовать фигуру по алгоритму, с учетом масштаба.
Нарисовать точки и посчитать их.

Условие:
равноб треугольник
кт - 15
лев кат || OY
прямой угол смотрит в лев верхний

import turtle as t


k=10

t.left(90)
for i in range(3):
    t.right(45)
    t.forward(15 * (2** 0.5) * 10)
    t.right(180-45)
    t.forward(15*k)
    t.right(90)
    t.forward(15 * 10)
    t.right(90)

t.pu()
for x in range(1,14):
    for y in range(1,15):
        t.goto(x*10,y*10)
        t.dot(5)
t.done()



### 8(2)
from itertools import product
nums=product('01234567',repeat=5)
k=0
n='16 36 56 76 61 63 65 67'
nn=n.split()
for n in nums:
    numb=''.join(n)
    sp=[]
    if numb.count('6')==1 and numb[0]!='0':
        for x in nn:
            if x in numb:
                sp.append(x)
        if not sp: 
            k+=1
print(k)


Написать все возможные варианты последовательности
Проверить варианты по условиям задачи
содержит одну 4 и рядом с ней нет четного числа

### 9
счетесли($A1:$D1;A1)
если(сумм(G1;L1)=8;1;0)
срзначесли(G1:L1;1;A1:F1)
суммесли(G1:L1;2;A1:f1)
если(и(M1=1;N1<=01);1;0)

# загрузка текста из txt
text=t.split(";")
#result = [int(item) for item in text]
result = list(map(int, text))
x=0
y=x+6
counter=double_num=0

while True:
   n=0
   res6=result[x:y]
   for element in res6:
      if res6.count(element)>2:
         for yy in range(res6.count(element)): res6.remove(element) 
         # удаление значений больше 2 штук
      if res6.count(element)==2:
         n+=2   
         double_num=element 
         res6.remove(element)
         res6.remove(element)

   if n==2 and len(res6)==4:  
      if (sum(res6)/len(res6))<=(double_num*2): counter+=1

   print(counter)
   if y>=len(result):break         
   x=x+6
   y=x+6
   
### 11   

for x in range(10000):
    s = x
    s = (s - 10) // 7
    n = 1
    while s > 0:
        n = n * 2
        s = s - n
    if n == 8:
        print(x)
        break

### 12

spisok=[]
for num in range(2,1000):
  n=0 
  for delit in range (2,100):
    if num%delit==0 and x<i: n+=1
  
  if n==0:spisok.append(num)
        
flag=False
for i in spisok:
    for y in range (100):
        if y*4+117==i and flag==False:
            print(y, i)
            flag=True


### 14

for x in range(15):
    a15=1*15**4+2*15**3+3*15**2+x*15**1+5
    b15=1*15**4+x*15**3+2*15**2+3*15+3
    sum10=a15 + b15
    if sum10%14==0:
        print(x , sum10//14)
        break


### 15 

for A in range(100):
    if all(((x % 3 == 0) <= (x % 5 != 0)) or x + A >= 70 for x in range(1, 10000)):
        print(A)
        break
```

### 16
