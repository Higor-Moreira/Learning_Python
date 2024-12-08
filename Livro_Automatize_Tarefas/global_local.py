# Entendendo escopo local e global 

nome = 'Igor'


def Teste():
    nome = 'Higor'
    print(nome)

Teste()
print(nome)

# ==============================

idade = 28

def Aniversario():
    global idade # referencia a variavel global
    idade += 1

Aniversario()
print(idade)
