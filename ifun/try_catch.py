try:
    age = int(input('Age :'))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be zero')
except ValueError:
    print('Invalid value')
