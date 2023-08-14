import os

def capturando_datos():
    #Lendo dados do usuario
    Texto = input('Informe un texto: ')
    print('Voce escrveu: ', Texto)
    print(type(Texto))

    inteiro = input('\nInforme un entero: ')
    #Tentar executar o codigo  e continuar caso haja erro
    try:
        inteiro = int(inteiro)
    except:
        print('Error al intentar convertir entero...')
    print(f'Usted informo: {inteiro}')


    float_usu = input('\nInforme un float: ')
    try:
        inteiro = float(float_usu)
    except:
        print('Error al intentar convertir float...')
        
    print(f'Usted informo: {float_usu}')

if __name__ == '__main__':
    os.system('cls')
    
    print('Ejecutando primera vez----')
    capturando_datos()
    print('\nEjecutando segunda vez----\n')
    capturando_datos()
    print('\nEjecutando tercera vez----\n')
    capturando_datos()
    
