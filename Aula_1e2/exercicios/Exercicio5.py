# 	Crie uma função que exiba uma mensagem perguntando a idade do usuário e, com base na idade fornecida,
# 	exiba diferentes mensagens de acordo com as seguintes faixas etárias: 0-12 anos, 13-17 anos, 18 ou mais anos.
# 	(mais faixas etárias podem ser incluídas)
import os

def idade():
    
    edad = int(input('Informa la edad: '))

    if (edad >0 and edad <100):    
        if (edad >0 and edad <=12):
            print('Ustes es un bebe')

        elif (edad >=13 and edad <=18):
            print('Usted es un joven')

        elif (edad >=19 and edad <=55):
            print('Usted es un adulto')

        elif (edad >=56 and edad <100):
            print ('Usted es anciano')
    else:
        print("Edad no válida")
    

if __name__ == '__main__':
    os.system('cls')
    idade()
