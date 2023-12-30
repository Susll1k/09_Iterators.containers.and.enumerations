

#1----------------------------------------------------------------------------------------------------

lst=[1,2,3,4,5,6,7]
d={}
for i in lst:
    m=i**3
    if m%2 != 0:
        d[i] = m
print(d)


#2----------------------------------------------------------------------------------------------------

lst=[1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
l=[]
for i in lst:
    if i%2 == 0:
        l.append(i)
        continue
    sorted(l)
    s =set(l)
print(s)


#3----------------------------------------------------------------------------------------------------

lst=[]
a=0
for i in range (10):
    lst.append(a)
    a=a+10
print(lst)

#4----------------------------------------------------------------------------------------------------

num=int(input("Число: "))
def f(n):
    for i in range(1,n):
        if i%7 == 0:
            yield i 

for i in f(num):
    print (i)

#5----------------------------------------------------------------------------------------------------

import re
import itertools

word = input("Введите слово:")
words = re.findall("[A-z]", word)
sum=0
r = 1
comb = set(itertools.permutations(words, r))



while len(comb):
    for c in comb:
        print("".join(c))
    sum+=len(comb)
    r += 1
    comb = set(itertools.permutations(words, r))
print(sum)


