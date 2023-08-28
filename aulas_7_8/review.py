import os

def eh_positivo(numero):
    
    if numero > 0:

        print('Es positivo')

    else:

        print('Es negativo')

def son_iguales(numero1, numero2):
    
    if numero1 == numero2:

        print('Son iguales')

    else:

        print('No son iguales')

def main():

    menu = '''
    \nSeleccione la funcion:
    \n1) Es positivo:
    \n2) Son iguales
    \nOpcion = '''

    while True:

        try:

            funcion_seleccionada = int(input(menu))

            if funcion_seleccionada == 1:
                
                numero = int(input('Digite un numero: '))
                eh_positivo(numero)

            elif funcion_seleccionada == 2:

                numero1 = int(input('Digite un numero: '))
                numero2 = int(input('Digite otro numero: '))
                son_iguales(numero1, numero2)



        except Exception as e:

            print('Erro: ', e)



if __name__ == '__main__':

    main()

