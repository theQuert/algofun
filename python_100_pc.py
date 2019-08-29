

# 001

for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if((i != j) and (j != k) and (i != k)):
                print('{}{}{}'.format(i,j,k))
                
# 002
                
i = int(input('Please input the profit :'))
arr = [1000000, 600000, 400000, 200000, 100000, 0]
rate = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
pr = 0

for idx in range(0, 6):
    if i > arr[idx]:
        pr += (i - arr[idx]) * rate[idx]
        print((i - arr[idx]) * rate[idx])
        i = arr[idx]
print(pr)

# 003

import numpy
import math

for i in range(1, 100):
    arr[] = i

# 004
    
year = int(input('Input the year :'))
month = int(input('Input the month :'))
day = int(input('Input the day :'))

d = 0
arr = [31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 28, 31]
m_arr = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

for idx in range(0, 12):
    if month > m_arr[idx]:
        d += arr[idx]
        
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    d = d + day + 1
else:
    d = d + day
               
print(d)


# 005

x = int(input('Integer :'))
y = int(input('Integer :'))
z = int(input('Integer :'))
arr = [x, y, z]
arr.sort()

print(arr)


# 006
# Figure 1
def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(10))    

# Figure 2
def fib(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[i-1] + fibs[i-2])
    return fibs

print(fib(10))

# 007

a = [1, 2, 3]
b = a[:]

print(b)

# 008

for i in range(1, 10):
    for j in range(1, i+1):
        print('{} * {} = {}'.format(i, j, i*j))

# 009 

import time

myD = {1:'a', 2:'b'}
for key, value in dict.items(myD):
    print(key, value) 
    time.sleep(1)  ## Pause 1 second

# 010
    
import time

print(time.strftime('%Y:%m:%d %H:%M:%S'), time.localtime(time.time()))

time.sleep(1)
print(time.strftime('%Y:%m:%d %H:%M:%S'), time.localtime(time.time()))

# 011

def fib(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[i-1] + fibs[i-2])
    return fibs
print(fib(42))

#012

#013

for i in range(100, 1000):
    j = i % 100
    k = i / 10 % 10
    l = i / 10
    if i == (j**3 + k**3 + l**3):
        print('{}'.format(i))

# 014
        
# 015
        
score = int(input('Input your score :'))
if score >= 90:
    grade = 'A'
elif score >= 60:
    grade = 'B'
else:
    grade = 'C'

print('{} belong to {}'.format(score, grade))

# 016

import datetime

if __name__ == '__main__':
    print(datetime.date.today().strftime('%d/%m/%Y'))
    LeoBirthDate = datetime.date(1941, 1, 5)
    print(LeoBirthDate.strftime('%d/%m/%Y'))
    LeoBirthDateNextDay = LeoBirthDate + datetime.timedelta(days = 1)
    print(LeoBirthDateNextDay.strftime('%d/%m/%Y'))
    LeoFirstBirthDate = LeoBirthDate.replace(year = LeoBirthDate.year + 1)
    print(LeoBirthDate.strftime('%d, %m, %Y'))
    
# 017
    
import string
s = input('Input a number: \n')
letters = 0
spaces = 0
number = 0
others = 0
i = 0
while i < len(s):
    c = s[i]
    i += 1
    if c.isalpha():
        letters += 1
    elif c.isspace():
        spaces += 1
    elif c.isdigit():
        number += 1
    else:
        others += 1
print('There are {} letters, {} spaces, {} numbers, {} others'.format(letters, spaces, number, others))

# 018

n = int(input('Input n: '))
a = int(input('Input a: '))
Sn = 0
Sn1 = 0
Total = 0
for j in range(0, n+1):
    for i in range(0, j):
        Sn = a * 10**i
        Sn1 += Sn
print('Total = ', Sn1)

# 019

# 020

tour = []
height = []

hei = 100.0
tim = 10

for i in range(1, tim+1):
    if i == 1:
        tour.append(hei)
    else:
        tour.append(2*hei)
    hei /= 2
    height.append(hei)
print('Tour = {}'.format(sum(tour)))
print('The 10th time height = {}'.format(height[-1]))

# 021

init = 1
for i in range(9, 0, -1):
    init2 = 2 * (init + 1)
    init = init2
print(init)
    

# 022

# 023

from sys import stdout
for i in range(4):
    for j in range(2 - i + 1):
        stdout.write(' ')
    for k in range(2 * i + 1):
        stdout.write('*')
    for l in range(2 - i + 1):
        stdout.write(' ')
    stdout.write('\n')
    print
for i in range(3):
    for j in range(i + 1):
        stdout.write(' ')
    for k in range(4 - 2 * i + 1):
        stdout.write('*')
    for l in range(i + 1):
        stdout.write(' ')
    stdout.write('\n')
    print

# 024

x = 2
y = 1
res = 0
for i in range(1, 21):
    if i == 1:
        res += x / y
    else:
        y, x = x, x+y
        res += x/ y
        
print(res)

# 025

total = 0

for i in range(1, 21):
    if i == 1:
        semi =  1
    else:
        semi = semi * i
        total += semi
print(total)

# 026

def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n-1)
print(fac(5))

# 027

# 027_ptc
string = input('Input the string :')
str_list = list(string)
print(str_list)

str_list.reverse()

fullstr = ''.join(str_list)
print(fullstr)

# 027

string = input('Input a string :')
str_list = list(string)
str_list.reverse()
full_str = ''.join(str_list)

print(full_str)

# 028

# 029

x = int(input('Input a number :'))
a = x / 10000
b = x % 10000 / 1000
c = x % 1000 / 100
d = x % 100 / 10
e = x % 10 

if a != 0:
    print('5', e, d, c, b, a)
elif b != 0:
    print('4', e, d, c, b)
elif c != 0:
    print('3', e, d, c)
elif d != 0:
    print('2', e, d)
else:
    print('1', e)

# 030

number = int(input('Input a number : '))
string = str(number)
flag = True

for i in range(0, 2):
    if string[i] != string[4-i]:
        flag = False
        break
if flag:
    print('This is true')
else:
    print('False')        

# 031
    
letter = input('Please input the letter :')

if letter == 'S':
    print('Please input the second letter')
    letter = input('Please input the second letter')
    if letter == 'a':
        print('Saturday')
    elif letter == 'u':
        print('Sunday')
    else:
        print('Data error')

elif letter == 'M':
    print('Monday')
elif letter == 'W':
    print('Wednesday')
elif letter == 'F':
    print('Friday')

elif letter == 'T':
    print('Please input second letter')
    letter = input('Please input the second letter')
    if letter == 'u':
        print('Tuesday')
    elif letter == 'h':
        print('Thursday')
    else:
        print('Data error')

# 032
        
a = ['one', 'two', 'three']
a.reverse()
print(a)

# 033

L = [1, 2, 3, 4, 5]
print(L)


import os
print(os.getpid())
pid = os.fork()

# Build new process with fork()

import os, time

source = 10
try:
    pid = os.fork()
    if pid == 0:
        print('this is a child process')
        source = source - 1
        time.sleep(3)
    else:
        print('This is a parent process')
    
    print(source)
except OSError:
    pass

# 034
    
def hello_world():
    print('Hello World !')

def three_hellos():
    for i in range(3):
        hello_world()

if __name__ == '__main__':
    three_hellos()

# 035

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033]92m'
    WARNING = '\033]93m'
    FAIL = '\033[91m'
    ENDC = '033[0m'
    BOLD = '033[1m'
    UNDERLINE = '\033[4m'
    
print('\033[1;33;44m 警告的文字 \033[0m')
print(bcolors.WARNING + '警告的文字' + bcolors.ENDC)

# 036

lower = int(input('Input the lower :'))
upper = int(input('Input the upper :'))
L = list()

for i in range(lower, upper+1):
    for j in range(2, i):
        if ((i % j) == 0):
            break
    else:
        L.append(i)

def list_duplicate(List):
    return list(dict.fromkeys(List))

print(list_duplicate(L))

# 037

if __name__ == '__main__':
    N = 10
    print('Input 10 numbers :')
    ls = list()
    for i in range(N):
        ls.append(int(input('Input 10 numbers :')))
    print(ls)
    print('After sorting...')
    ls.sort()
    print(ls)

# 038
    
if __name__ == '__main__':
    a = []
    sum = 0
    for i in range(3):
        a.append([])
        for j in range(3):
            a[i].append(int(input('Input the numbers :\n')))
    for i in range(3):
        sum += a[i][i]
    print(sum)

# 039_Figure1
    
if __name__ == '__main__':
    a = [1,4,6,9,13,16,19,28,40,100,0]
    print('Original list...')
    number = int(input('Please input a number :'))
    a.append(number)
    a.sort()
    print(a)
    
# 039_Figure2

if __name__ == '__main__':
    a = [1,4,6,9,13,16,19,28,40,100]
    print('Original List...')
    print(a)
    number = int(input('Input a number : '))

    for i in range(10):
        if a[i] > number:
            a.insert(i, number)
    
    a = list(dict.fromkeys(a))
    print(a)

# 040
    
if __name__ == '__main__':
    a = [9, 6, 5, 4, 1]    
    a.sort()
    print(a)

# 041
    
def varfunc():
    var = 0
    print('var = {}'.format(var))
    var += 1
    
if __name__ == '__main__':
    for i in range(3):
        varfunc()
    
class Static:
    StaticVar = 5
    def varfunc(self):
        self.StaticVar += 1
        print(self.StaticVar)
        
print(Static.StaticVar)
a = Static()
for i in range(3):
    a.varfunc()






