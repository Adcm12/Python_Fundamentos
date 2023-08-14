# Crie uma função que solicite ao usuário que insira uma sequência de números inteiros 
# separados por espaço e, em seguida, calcule e exiba a média desses números. Utilize listas 
# para armazenar os números digitados pelo usuário e um for loop para calcular a soma dos elementos da lista.
import os

def calcular_media():
    numeros = input("Digite uma sequencia de números enteros separados por espacios: ")
    numeros_lista = [int(num) for num in numeros.split()]
    
    suma = 0
    for num in numeros_lista:
        suma += num

    media = suma / len(numeros_lista)

    print("A média dos números digitados é:", media)


if __name__ == '__main__':
    os.system('cls')
    calcular_media()
