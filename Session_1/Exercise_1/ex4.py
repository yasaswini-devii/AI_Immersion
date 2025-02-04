def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "Error: Division by zero"

op = input('Enter 1.addition 2.subtraction 3.multiplication 4.divide: ')
a, b = map(int, input('Enter operands: ').split())
if op == '1':
    print(add(a, b))
elif op == '2':
    print(subtract(a, b))
elif op == '3':
    print(multiply(a, b))
elif op == '4':
    print(divide(a, b))
else:
    print('Invalid')
