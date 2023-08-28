import os

def eh_positivo(numero1, numero2):
    
    if numero1 > 0 and numero2 > 0:

        return True

    else:

        return False

def son_iguales(numero1, numero2):
    
    if numero1 == numero2:

        print('Son iguales')

    else:

        print('No son iguales')

def maior(numero1, numero2):

    if eh_positivo(numero1, numero2) is True:

        if numero1 > numero2:

            print( f'{numero1} es mayor que {numero2}')            

        elif numero2 > numero1: 
            print(f'{numero2} es mayor que {numero1}')

        else: 
            print("Los numeros son iguales, digite numero diferentes")
            
def menor(numero1, numero2):

    if eh_positivo(numero1, numero2) is True:

        if numero1 < numero2:
            print(f'{numero1} es menor que {numero2}')
        
        elif numero2 < numero1: 
            print(f'{numero2} es menor que {numero1}')

        else: 
            print("Los numeros son iguales, digite numero diferentes")


def verifica_si_es_par(numero):

    if numero > 0:

        if numero % 2 == 0:

            print('El numero es par') 

        else: 
            print('El numero es impar') 
    
    else:

        print('El numero es impar')


def main():

    menu = '''
    \nSeleccione la funcion:
    \n1) Es positivo:
    \n2) Son iguales
    \n3) Maior
    \n4) Menor
    \n5) Es Par
    \nOpcion = '''

    while True:

        try:

            funcion_seleccionada = int(input(menu))

            if funcion_seleccionada == 1:
                
                numero1 = int(input('\nDigite un numero: '))
                numero2 = int(input('\nDigite otro numero: '))
                print(eh_positivo(numero1, numero2))

            elif funcion_seleccionada == 2:

                numero1 = int(input('\nDigite un numero: '))
                numero2 = int(input('Digite otro numero: '))
                son_iguales(numero1, numero2)

            elif funcion_seleccionada == 3:

                numero1 = int(input('\nDigite un numero: '))
                numero2 = int(input('Digite otro numero: '))
                maior(numero1, numero2)

            elif funcion_seleccionada == 4:

                numero1 = int(input('\nDigite un numero: '))
                numero2 = int(input('Digite otro numero: '))
                menor(numero1, numero2)

            elif funcion_seleccionada == 5:

                numero = int(input('\nDigite un numero: '))
                verifica_si_es_par(numero)

        except Exception as e:

            print('Erro: ', e)



if __name__ == '__main__':

    main()

