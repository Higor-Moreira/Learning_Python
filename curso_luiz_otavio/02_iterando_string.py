# Em python strings são iteráveis. Sabendo disso, faça um programa que:
# 1 - Peça ao usuário para digitar seu nome
# 2 - informe quantas letras tem o nome 
# 3 - conte quantas vogais tem o nome
# 4 - conte quantas vezes aparece a letra 'a'

resposta = 's'

while resposta == 's':
    nome = input('Digite seu nome: ')
    if nome.isalpha():
        qtd_letras = len(nome)
        qtd_vogais = 0
        qtd_a = 0
        for letra in nome:
            if letra.lower() in 'aeiou':
                qtd_vogais += 1
            if letra.lower() == 'a':
                qtd_a += 1
        print(f'O nome {nome} tem {qtd_letras} letras, {qtd_vogais} vogais e a letra "a" aparece {qtd_a} vezes.')

        resposta = input('Deseja continuar? (s/n) ').lower()
        if resposta == 'n':
            print('Obrigado por usar o programa!')
            break
    else:
        print('nome invalido, digite apenas letras.')