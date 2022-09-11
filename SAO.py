import math

n1 = ('Insira a operação desejada ')
n1 += ('\nPara soma digíte + ')
n1 += ('\nPara subtração digíte - ')
n1 += ('\nPara multiplicação  Digíte *')
n1 += ('\nPara raiz quadrada digíte #')
n1 += ('\nPara numeros elevados **')
n1 += ('\nPara divisão digíte / \n OPERAÇÃO: ')

operacao = input(n1)

num_1 = int(input('Insira o primeiro número: '))
num_2 = int(input('Insira o segundo número: '))

if operacao == '+':
    print(f'Operação: {num_1} + {num_2} = {num_1 + num_2}')

elif operacao == '-':
    print(f'Operação: {num_1} - {num_2} = {num_1 + num_2}')

elif operacao == '*':
    print(f'Operação: {num_1} * {num_2} = {num_1 * num_2}')

elif operacao == '/':
    print(f'Operação: {num_1} / {num_2} = {num_1 / num_2}')

elif operacao == '**':
    print(f'Operação: {num_1} ** {num_2} = {num_1 ** num_2}')


else:
   print('Essa operação não é válida para esta calculadora, tente novamente! ')