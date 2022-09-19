text = 'world'
print('Hello, {}'.format(text))

myname = 'Jack'
mytext = 'WOrld'
print('Hello, {name}, hello, {text}'.format(name=myname, text=mytext))

print({':x'}.format(23))

text = 'world'
print(f'Hello, {text}')
print('Hello, {thetext}'.format(thetext=text))

x = 10
y = 27
print(f'x + y = {x + y}')
print('x + y = {ans}'.format(ans=x+y))

def hello(text, name):
    return f'Hello, {name}, {text}'

def ano_hello(text, name):
    return '{text}, {name}.'.format(name=name, text=text)

print(ano_hello('Hello', 'Leo'))

from string import Template as tp

text = 'world'
tp.substitute('Hello, $text')
