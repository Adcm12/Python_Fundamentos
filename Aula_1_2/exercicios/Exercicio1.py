#	Escreva uma função que solicite ao usuário que insira seu nome e, em seguida,
	# armazene esse valor em uma variável. Em seguida, exiba uma mensagem de boas-vindas
	# usando o nome digitado.
import os

def nome_usuario():
    nome= input('Informa un nombre: ')

    print(f'\nBem vindo {nome}')

if __name__ == '__main__':
    os.system('cls')
    nome_usuario()
    