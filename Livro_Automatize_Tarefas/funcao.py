# treinando conceitos de funcao, chamada, return, etc.

def Menu():
    print("=" * 25)
    print('>>> CALCULADORA <<<') 
    print('Operações:')
    print('1 - Soma')
    print('2 - Subtracao')
    operacao = input('Qual operacao deseja fazer: ')
    print("=" * 25)
    return operacao

def Soma(num1, num2):
    return f'{num1} + {num2} é igual a {num1 + num2}'

    '''
    Escopo local:
    as variaveis no escopo local sao criadas quando a funcao 
    é chamada, e sao destruidas assim que a funcao retorna o valor. 
    '''

def Subtracao(num1, num2):
    return f'{num1} - {num2} é igual a {num1 - num2}'

while True:

    operacao = Menu() # armazena a escolha do usuario 

    if operacao == '1':
        num1 = int(input('Digite o primeiro numero: '))
        num2 = int(input('Digite o segundo numero: '))
        print(Soma(num1, num2))
    
    elif operacao == '2':
        num1 = int(input('Digite o primeiro numero: '))
        num2 = int(input('Digite o segundo numero: '))
        print(Subtracao(num1, num2))




