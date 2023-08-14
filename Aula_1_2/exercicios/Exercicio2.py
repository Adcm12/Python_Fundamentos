	# Escreva uma função que calcule a média de três notas fornecidas pelo usuário e
	# armazene o resultado em uma variável. Em seguida, exiba a média calculada no terminal.

import os

def media():

    nota1 = int(input('Informe primera nota: '))
    nota2 = int(input('Informe segunda nota: '))
    nota3 = int(input('Informe tercera nota: '))

    mediaa = (nota1 + nota2 + nota3)/3

    print(f'\nLa media de las notas informas es: {mediaa}')

if __name__ == '__main__':
    os.system('cls')
    media()