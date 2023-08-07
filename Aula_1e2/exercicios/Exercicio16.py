# Crie uma função que solicite ao usuário que insira uma lista de notas de alunos (números reais entre 0 e 10).
# 	A função deve calcular e exibir a média, a nota mais alta e a nota mais baixa. Utilize listas e for loops para
# 	processar as notas digitadas pelo usuário.
import os

def calcular_media_notas():
    notas_str = input("Ingrese una lista de notas separadas por espacios (números reales entre 0 y 10): ")
    notas_lista = [float(nota) for nota in notas_str.split()]

    suma = 0
    # nota_maxima = notas_lista[0]
    # nota_minima = notas_lista[0]

    for nota in notas_lista:
        suma += nota

        media = suma / len(notas_lista)
        
        if nota > notas_lista:
            # nota_maxima = nota
            print(notas_lista)
        
        elif nota < nota_minima:
            nota_minima = nota
            print(nota_minima)
        
    print("A média dos números digitados é:", media)


if __name__ == '__main__':
    os.system('cls')
    calcular_media_notas()