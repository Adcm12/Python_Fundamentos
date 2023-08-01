# 	Crie uma função que peça ao usuário que digite um número inteiro e, em seguida,
# 	armazene esse valor em uma variável. Crie mais funções para o usuário também informar 
# 	dados do tipo float e string, e armazene todos os dados em variáveis. Em seguida
# 	adicione todos esses items em uma lista e mostre os item através de um laço de repetição for. 
import os

lista=[] 

def numero_entero():

    entero = int(input('Informa un numero entero: '))
    lista.append(entero)

def numero_float():
    floatt = float(input('Informa un numero float: '))
    lista.append(floatt)

def string():
    str= input("Informe una cadena de caracteres: ")
    lista.append(str)

if __name__ == '__main__':
    os.system('cls')
    numero_entero()
    numero_float()
    string()

    for i in lista:
        print('\n',i)