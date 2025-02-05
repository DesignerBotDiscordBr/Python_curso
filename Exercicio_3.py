# Exercicio 4 Lista de compras

import os
lista = set()
lista_1 = list(lista)
while True:
    lista_input = input('Para [I]nserir, [L]istar, [A]pagar, [S]air: ').lower()
    if len(lista_input) > 1:
        print('tem mais de uma letra')
        
        if not input('deseja continuar? [S]im ou [N]ao: ').lower().startswith('s'): 
            break
        else:
            continue

    if lista_input == 'i':
        os.system('cls')
        item = input('digite o item: ').lower()
        lista_1.append(item)
    elif lista_input == 'l':
        for i, valor in enumerate(lista_1):
            print(f'Indice: {i}, Produto: {valor}')
        if len(lista_1) == 0:
            print('A lista esta vazia')
    elif lista_input == 's':
        break
    elif lista_input == 'a':
        try:
            obj_para_apagar = (input('digite o indice do item para apagar: '))
            if obj_para_apagar.isnumeric():
                obj_para_apagar = int(obj_para_apagar)
            else:
                print('indice invalido')
                continue
            print(lista_1.pop(obj_para_apagar),": " ,'foi apagado com sucesso✅ ' )
        except IndexError:
            print('Encontramos um erro❌:', IndexError)
    else:
        print('Comando invalido')