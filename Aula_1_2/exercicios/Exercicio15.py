# Dado um número inteiro positivo N, Crie uma função que calcule a soma de todos os números ímpares de 1 até N.
# Utilize um for loop para iterar pelos números e um operador de módulo (%) para verificar se o número é ímpar.
import os

def suma_numeros_impares():
    suma = 0
    numero = int(input("Ingresa un número entero positivo: "))

    for i in range(1, numero+1):
        if i % 2 != 0:  # Verifica si el número es impar
            suma += i
    
    print("La suma de los números impares desde 1 hasta", numero, "es:", suma)

if __name__ == '__main__':
    os.system('cls')
    suma_numeros_impares()