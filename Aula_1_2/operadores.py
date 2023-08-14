import os
def verifica_numeros():   
    try:
        numero1 = int(input('Informe un numero: '))
        numero2 = int(input('Informe otro numero: '))

        if numero1 > 0 and numero2 > 0:

            if numero1 != numero2:

                if numero1 > numero2:
                    print('Primer numero es mayor')

                elif numero1 < numero2:
                    print('Segundo numero es mayor')

            elif numero1 == numero2:
                print('Los numeros son iguales.')
        else:
            print('Numeros necesitan ser positivos')

    except:
        print('Error al convertir los numeros...')

def verifica_idade():
    try:
        idade_usu = int(input('Informe su idade: '))

        if idade_usu > 0 and idade_usu <120:

            #Verificar si es adulta, necesita mayor de 18
            if idade_usu >=18:
                print("Es adulto")

            elif idade_usu >= 12 and idade_usu <18:
                print("Es joven.")
            elif idade_usu <= 12:
                print ("Es un bebe.")
        
        else:
            print('Idade invalida')


    except:
        print('Error al leer los datos')


if __name__ =='__main__':
    os.system('cls')
    os.system('python --version')

    verifica_idade()

