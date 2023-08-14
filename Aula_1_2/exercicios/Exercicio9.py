# Crie uma função que converta um valor em dólar para real. Peça ao usuário que insira a cotação do 
# dólar e o valor em dólar a ser convertido. Em seguida, exiba o valor equivalente em reais.
import os

def convertir_a_real():

    os.system('cls')
    
    valor_D= float(input('Digite el valor del real a dolar: '))
    cantidad= float(input("Digite la cantidad de dolares a convertir: " + '$'))

    conversion= valor_D * cantidad

    print(f'La converion es: {conversion} R$')

def convertir_a_dolar():
    
    os.system('cls')

    valor_R =float(input('Valor del Dolar en Reales: '))
    cantidad=int(input("Cantidad de Dolares a Convertir: "))

    conversion=valor_R/cantidad

    print( f"La conversión es: {conversion}$")


while True:

    # 

    seleccion= int(input('''Seleccione una opcion: 
                         \n1) Convertir de Dolar a Real 
                         \n2)Convertir de Real a Dolar
                         \n3)Salir
                         \n'''))
    
    if seleccion == 1:
        convertir_a_real()

    elif seleccion ==2:
        convertir_a_dolar()
    
    elif seleccion == 3:
        break

    else:
        os.system('cls')
        print('Digite una opcion valida!!!!!\n')


# if __name__ == '__main__':
#     os.system('cls')
#     # convertir_a_real()
#     # convertir_a_dolar()