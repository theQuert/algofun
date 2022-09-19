# coding=utf-8
'''
        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)
'''

#x = float(input('x = '))
#if x > 1:
#    y = 3 * x - 5
#elif x >= -1:
#    y = x + 2
#else:
#    y = 5 * x + 3
#
#print('(%.2f) = %.2f' % (x, y))
#

#value = float(input('Input the length'))
#unit = input('Pls input the unit: ')
#if unit == 'inch' or unit == '英吋':
#    print('%f inch = %f cm' % (value, value * 2.54))
#elif unit == 'cm' or unit == '釐米':
#    print('%f cm = %f inch' % (value, value / 2.54))
#else:
#    print('Pls input valid value...')

#score = float(input('Input the score: '))
#if score >= 90:
#    grade = 'A'
#elif score >= 80:
#    grade = 'B'
#elif score >= 70:
#    grade = 'C'
#elif score >= 60:
#    grade = 'D'
#else:
#    grade = 'F'
#print('Grade: {0}'.format(grade))

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
length = a + b + c
if((a + b > c) and (a +c > b) and (b + c > a)):
    print('Length: {0}'.format(length))
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('Area: %f' % (area))
else:
    print('Try again...')