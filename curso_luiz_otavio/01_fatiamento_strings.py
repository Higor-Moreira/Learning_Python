"""
Exercicio:

1- Peça ao usuario para digitar seu nome
2 - Peça ao usuario para digitar sua idade
3 - Verifique se nome e idade foram digitados

Exiba:

1 - seu nome é {nome}
2 - seu nome invertido é {nome invertido}
3 - Seu nome contém ou não espaço
4 - Seu nome tem {n} letras
5 - A primeira letra do seu nome é {primeira letra}
6 - A última letra do seu nome é {última letra}

Se nada for digitado em nome ou idade:
    exiba "Desculpe, voce deixou campos vazios. 

"""

nome_digitado = input('Digite seu nome: ')
idade_digitado = input('Digite sua idade: ')

nome_invertido = nome_digitado[::-1]

if not nome_digitado or not idade_digitado:
    print('Desculpe, voce deixou campos vazios.')
else:
    print(f'seu nome é {nome_digitado}')
    print(f'seu nome invertido é {nome_invertido}')
    print(f'Seu nome contém espaço: {"sim" if " " in nome_digitado else "não"}')
    print(f'Seu nome tem {len(nome_digitado)} letras')
    print(f'A primeira letra do seu nome é {nome_digitado[0]}')
    print(f'A última letra do seu nome é {nome_digitado[-1]}')

