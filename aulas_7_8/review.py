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

def mayor_de_la_lista(lista):

    variable = 0

    for i in lista:

        if  i > variable:

            variable = i

    print(f'\nEl numero mayor de la lista es: {variable}')

def cantidad_de_pares_en_lista(lista):

    lista_par : int= []
    lista_impar : int= []

    for i in lista:

        if i % 2 == 0:

            lista_par.append(i)
        
        else: 
            lista_impar.append(i)

    print(f'\nLista de pares {lista_par}, cantidad: {len(lista_par)}')
    print(f'\nLista de impares {lista_impar}, cantidad: {len(lista_impar)}')

def menor_de_la_lista(lista):

    variable = lista[0]

    for i in lista:

        if  i < variable:

            variable = i

    print(f'\nEl numero menor de la lista es: {variable}')

def calculadora(numero1, numero2, opcion):

    if opcion == 1:

        resultado = numero1 + numero2
        print(f'La suma es: {resultado}')

        
    elif opcion == 2:

        resultado = numero1 - numero2
        print(f'La resta es: {resultado}')

    elif opcion == 3:

        resultado = numero1 * numero2
        print(f'La multiplicacion es: {resultado}')

    elif opcion == 4:

        resultado = numero1 / numero2
        print(f'La division es: {resultado}')
    
    # elif opcion == 5:

    #     quit()
    
    else:
        print('Digite una opcion valida')

def buscar_letra(texto, letra):

    cantidad = 0
    
    for i in texto:

        if i == letra:
            
            cantidad += 1
        else:
            False
                       
    
    print(f'La letra {letra}, aparece: {cantidad}')

def verificar_salario(hora, valor, dias):

    salario = (hora * valor) * dias

    print(f'El salario del colaborador por {dias} dias trabajados es: {round(salario, 2)}')

def main():

    menu = '''
    \nSeleccione la funcion:
    \n1) Es positivo:
    \n2) Son iguales
    \n3) Maior
    \n4) Menor
    \n5) Es Par
    \n6) Mayor de varios numeros
    \n7) Cantidad de pares e impares
    \n8) Menor de varios numeros
    \n9) Calculadora
    \n10) Buscar letra
    \n11) Calcular salario
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
            
            elif funcion_seleccionada == 6:

                lista = []
                numero = int(input('Cuantos numeros va a inserir en la lista?: '))

                for i in range (numero):

                    valor=int(input(f"Ingrese el elemento {(i+1)}: "))
                    lista.append(valor)
                
                mayor_de_la_lista(lista)
            
            elif funcion_seleccionada == 7:

                lista = []
                numero = int(input('Cuantos numeros va a inserir en la lista?: '))

                for i in range (numero):

                    valor=int(input(f"Ingrese el elemento {(i+1)}: "))
                    lista.append(valor)
                
                cantidad_de_pares_en_lista(lista)

            elif funcion_seleccionada == 8:

                lista = []
                numero = int(input('Cuantos numeros va a inserir en la lista?: '))

                for i in range (numero):

                    valor=int(input(f"Ingrese el elemento {(i+1)}: "))
                    lista.append(valor)
                
                menor_de_la_lista(lista)

            elif funcion_seleccionada == 9:

                while True:

                    try:
                        opcion = int(input('\nEscoja una opcion \n1) Sumar \n2)Restar \n3)Multiplicar \n4)Dividir \n5)Break \n: '))
                        
                        if opcion == 5:

                            break
                        else:    
                            numero1 = int(input('\nDigite un numero: '))
                            numero2 = int(input('Digite otro numero: '))
                            calculadora(numero1, numero2, opcion)

                    except Exception as e:
                        print('Erro: ', e)

            elif funcion_seleccionada == 10:

                texto = input('Digite un texto: \n')
                letra = input('Digite la letra a buscar: ')

                buscar_letra(texto, letra)
            
            elif funcion_seleccionada == 11:

                horas = int(input('Digite las horas trabajadas: '))
                valor = float(input('Digite el valor de las horas: '))
                dias = int(input('Digite cuantos dias trabajo del mes: '))

                verificar_salario(horas, valor, dias)


        except Exception as e:
            print('Erro: ', e)

if __name__ == '__main__':

    main()

