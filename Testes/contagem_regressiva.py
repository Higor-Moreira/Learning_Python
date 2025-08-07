import time

espera = time.sleep(1)  # Espera 1 segundo

inicial = 10

while inicial > 0:
    print(inicial)
    espera
    inicial -= 1

print("Fim da contagem regressiva!")
