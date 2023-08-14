# Desenvolva uma função que mostre na tela uma contagem regressiva de 5 a 1, 
# com uma pausa de um segundo entre cada número.
import os
import time

def conta_regresiva():

    for i in range(5,0,-1):
        print(i)
        time.sleep(1)

if __name__ == '__main__':
    os.system('cls')
    conta_regresiva()