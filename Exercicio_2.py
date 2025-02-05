#Exercicio 2 calculadora
def calculadora(a, b): # a = num1, b = num2
    soma = a + b
    subtracao = a - b
    multiplicacao = a * b
    divisao = a / b
    return soma, subtracao, multiplicacao, divisao

num1 = int(input('digite um numero: '))
num2 = int(input('digite outro numero: '))
operacao = input('digite a operacao (+, -, *, /): ')

if operacao == '+':
    print(f'{num1} + {num2} = {calculadora(num1, num2)[0]}')
if operacao == '-':
    print(f'{num1} - {num2} = {calculadora(num1, num2)[1]}')
if operacao == '*':
    print(f'{num1} * {num2} = {calculadora(num1, num2)[2]}')
if operacao == '/':
    print(f'{num1} / {num2} = {calculadora(num1, num2)[3]}')