# Dado um número inteiro positivo N, crie uma função que exiba todos os números pares de 0 
# até N (inclusive). Utilize um for loop para iterar pelos números e um operador de módulo (%) 
# para verificar se o número é par.
import os

def numeros_pares():

    numero = int(input("Informe un numero entero positivo: "))

    for i in range(numero+1):
        if i % 2 == 0:
            print(i)

if __name__ == '__main__':
    os.system('cls')
    numeros_pares()