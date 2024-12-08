'''
Considere a seguinte operação em um número inteiro positivo arbitrário que:

* Se o número é par, divida-o por 2;
* Se é ímpar, multiplique-o por 3 e some 1

Após um numero X de loops, o resultado convertirá para 1. 
Independente do numero digitado inicialmente. 

'''

numero = int(input('Digite um numero inteiro e positivo: '))
loop = 0

def Collatz(num):

    global loop

    while num != 1:
        
        # se for par, num recebe num divido por 2
        if num % 2 == 0:
            num /= 2
        else:
            num = (num * 3) + 1
            
        print(num)

        loop += 1 

Collatz(numero)
print(f'Chegou a 1 após {loop}')
