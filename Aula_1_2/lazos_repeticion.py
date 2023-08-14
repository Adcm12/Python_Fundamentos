import os
from operadores import *

def script_idade():

    while True:

        verifica_idade()

        verificacion = input('Informe s salir, o cualquier otro caracter para continuar: ')
        verificacion = verificacion.lower()
        if verificacion == 's':
            break

def script_numeros(limite_loop):

    contador = 0

    while contador < limite_loop:
        contador+=1
        verifica_numeros()
        print('\n')
    print(f'El loop rodo {limite_loop}')


if __name__ == '__main__':
    os.system('cls')

    # script_idade()
    limite_loop = int(input('Informa cuantas veces va a rodar el programa: '))
    script_numeros(limite_loop)

