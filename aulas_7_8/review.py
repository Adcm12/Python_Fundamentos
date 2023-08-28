import os

def eh_positivo(numero):
    
    if numero % 2 == 0:

        print('Es positivo')

    else:

        print('Es negativo')

def son_iguales(numero1, numero2):
    
    if numero1 == numero2:

        print('Son iguales')

    else:

        print('No son iguales')





if __name__ == '__main__':

    eh_positivo(5)

    son_iguales(5, 4)

