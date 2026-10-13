#Calculating the value of expression

expression = input(f'Please input mathematical expression: ')

if '+' in expression:
    a, b = map(int, expression.split('+'))
    print(a + b)

elif '-' in expression:
    a, b = map(int, expression.split('-'))
    print(a - b)

elif '*' in expression:
    a, b = map(int, expression.split('*'))
    print(a * b)
