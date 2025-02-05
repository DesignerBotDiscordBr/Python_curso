
#Exercicio 1 verificaçao de impar ou par
def verificacao_de_par_impar():
    num = int(input('digite um numero: '))
    if num % 2 == 0:
        print(f'{num} é par')
    else:
        print(f'{num} é impar')

verificacao_de_par_impar()

