#F = float(input('Input the temperature'))
#C = (F - 32)* 1.8
#print('%.1f temperature = %.1f Celsius degree'%(F, C))

#radius = float(input('Input the redius: '))
#perimeter = 2 * 3.1416 * radius
#area = 3.1416 * radius * radius
#print('Length: %.1f'%(perimeter))
#print('Area: %.1f'%(area))

year = int(input('Input the year: '))
is_leap = year % 4 == 0 and year % 100 != 0 or \
    year % 400 == 0
print(is_leap)