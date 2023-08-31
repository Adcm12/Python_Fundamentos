import os

class Funciones():

    def eh_positivo(self, numero1, numero2):
        
        if numero1 > 0 and numero2 > 0:

            return True

        else:

            return False

    def son_iguales(self, numero1, numero2):
        
        if numero1 == numero2:

            print('Son iguales')

        else:

            print('No son iguales')

    def maior(self, numero1, numero2):

        if self.eh_positivo(numero1, numero2) is True:

            if numero1 > numero2:

                print( f'{numero1} es mayor que {numero2}')            

            elif numero2 > numero1: 
                print(f'{numero2} es mayor que {numero1}')

            else: 
                print("Los numeros son iguales, digite numero diferentes")
                
    def menor(self, numero1, numero2):

        if self.eh_positivo(numero1, numero2) is True:

            if numero1 < numero2:
                print(f'{numero1} es menor que {numero2}')
            
            elif numero2 < numero1: 
                print(f'{numero2} es menor que {numero1}')

            else: 
                print("Los numeros son iguales, digite numero diferentes")

    def verifica_si_es_par(self, numero):

        if numero > 0:

            if numero % 2 == 0:

                print('El numero es par') 

            else: 
                print('El numero es impar') 
        
        else:

            print('El numero es impar')

    def mayor_de_la_lista(self, lista):

        variable = 0

        for i in lista:

            if  i > variable:

                variable = i

        print(f'\nEl numero mayor de la lista es: {variable}')

    def cantidad_de_pares_en_lista(self, lista):

        lista_par : int= []
        lista_impar : int= []

        for i in lista:

            if i % 2 == 0:

                lista_par.append(i)
            
            else: 
                lista_impar.append(i)

        print(f'\nLista de pares {lista_par}, cantidad: {len(lista_par)}')
        print(f'\nLista de impares {lista_impar}, cantidad: {len(lista_impar)}')

    def menor_de_la_lista(self, lista):

        variable = lista[0]

        for i in lista:

            if  i < variable:

                variable = i

        print(f'\nEl numero menor de la lista es: {variable}')

    def calculadora(self, numero1, numero2, opcion):

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
            
        else:
            print('Digite una opcion valida')

    def buscar_letra(self, texto, letra):

        cantidad = 0
        cantidad_num = 0
        
        for i in texto:

            if i == letra:
                
                cantidad += 1
            else:
                False

            if i.isdigit():

                cantidad_num += 1
                        
        
        print(f'La letra {letra}, aparece: {cantidad} veces, y la cantidad de numeros: {cantidad_num}')

    def verificar_salario(self, hora, valor, dias):

        salario = (hora * valor) * dias

        print(f'El salario del colaborador por {dias} dias trabajados es: {round(salario, 2)}')

    def buscar_item_en_la_lista(self, lista):

        int_cuenta = 0
        float_cuenta = 0
        str_cuenta = 0

        for elemento in lista:

            if isinstance(elemento, int):

                int_cuenta += 1

            elif isinstance(elemento, float):
                
                float_cuenta += 1

            elif isinstance(elemento, str):

                str_cuenta += 1
            
        print(f'\nCantidad en total de datos en total: {(int_cuenta + float_cuenta + str_cuenta)} \nCantidad de string: {str_cuenta} \nCantidad de int: {int_cuenta} \nCantidad de floats: {float_cuenta}')
                

    def main(self):

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
        \n12) Buscar Item en lista
        \nOpcion = '''

        while True:

            try:

                funcion_seleccionada = int(input(menu))

                if funcion_seleccionada == 1:
                    
                    numero1 = int(input('\nDigite un numero: '))
                    numero2 = int(input('\nDigite otro numero: '))
                    print(self.eh_positivo(numero1, numero2))

                elif funcion_seleccionada == 2:

                    numero1 = int(input('\nDigite un numero: '))
                    numero2 = int(input('Digite otro numero: '))
                    self.son_iguales(numero1, numero2)

                elif funcion_seleccionada == 3:

                    numero1 = int(input('\nDigite un numero: '))
                    numero2 = int(input('Digite otro numero: '))
                    self.maior(numero1, numero2)

                elif funcion_seleccionada == 4:

                    numero1 = int(input('\nDigite un numero: '))
                    numero2 = int(input('Digite otro numero: '))
                    self.menor(numero1, numero2)

                elif funcion_seleccionada == 5:

                    numero = int(input('\nDigite un numero: '))
                    self.verifica_si_es_par(numero)
                
                elif funcion_seleccionada == 6:

                    lista = []
                    numero = int(input('Cuantos numeros va a inserir en la lista?: '))

                    for i in range (numero):

                        valor=int(input(f"Ingrese el elemento {(i+1)}: "))
                        lista.append(valor)
                    
                    self.mayor_de_la_lista(lista)
                
                elif funcion_seleccionada == 7:

                    lista = []
                    numero = int(input('Cuantos numeros va a inserir en la lista?: '))

                    for i in range (numero):

                        valor=int(input(f"Ingrese el elemento {(i+1)}: "))
                        lista.append(valor)
                    
                    self.cantidad_de_pares_en_lista(lista)

                elif funcion_seleccionada == 8:

                    lista = []
                    numero = int(input('Cuantos numeros va a inserir en la lista?: '))

                    for i in range (numero):

                        valor=int(input(f"Ingrese el elemento {(i+1)}: "))
                        lista.append(valor)
                    
                    self.menor_de_la_lista(lista)

                elif funcion_seleccionada == 9:

                    while True:

                        try:
                            opcion = int(input('\nEscoja una opcion \n1) Sumar \n2)Restar \n3)Multiplicar \n4)Dividir \n5)Break \n: '))
                            
                            if opcion == 5:

                                break
                            else:    
                                numero1 = int(input('\nDigite un numero: '))
                                numero2 = int(input('Digite otro numero: '))
                                self.calculadora(numero1, numero2, opcion)

                        except Exception as e:
                            print('Erro: ', e)

                elif funcion_seleccionada == 10:

                    texto = input('Digite un texto: \n')
                    letra = input('Digite la letra a buscar: ')

                    if len(letra) == 1 and len(texto) >= 10:

                        self.buscar_letra(texto, letra)

                    else:
                        print("El texto debe tener por lo menos 10 caracteres")
                
                elif funcion_seleccionada == 11:

                    try:

                        horas = int(input('Digite las horas trabajadas: '))
                        valor = float(input('Digite el valor de las horas: '))
                        dias = int(input('Digite cuantos dias trabajo del mes: '))

                        self.verificar_salario(horas, valor, dias)
                        
                    except Exception as e:
                        print('Erro: ', e)

                elif funcion_seleccionada == 12:
                    
                    lista = []

                    try:

                        int_cuenta = int(input('\nCuantos datos tipo (int) va a inserir en la lista?. (Minimo 2): '))
                        str_cuenta = int(input('\nCuantos datos tipo (str) va a inserir en la lista?. (Minimo 2): '))
                        float_cuenta = int(input('\nCuantos datos tipo (float) va a inserir en la lista?. (Minimo 2): '))

                        if int_cuenta >= 2 and float_cuenta >= 2 and str_cuenta >= 2:

                            for i in range (int_cuenta):

                                valor = int(input(f"\nIngrese el elemento {(i+1)} tipo (int): "))
                                lista.append(valor)

                            for i in range (str_cuenta):

                                valor = input(f"\nIngrese el elemento {(i+1)} tipo (str): ")
                                lista.append(valor)

                            for i in range (float_cuenta):

                                valor = float(input(f"\nIngrese el elemento {(i+1)} tipo (float): "))
                                lista.append(valor)

                            print("\nLa lista cumple con los requisitos.")

                            self.buscar_item_en_la_lista(lista)

                        else:
                            print("No cumple con los requisitos.")
                    
                    except Exception as e:
                        print('Erro: ', e)

            except Exception as e:
                print('Erro: ', e)

if __name__ == '__main__':

    objeto = Funciones()
    objeto.main()


