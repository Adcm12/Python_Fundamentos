import os
from review_db import Logica_Banco

class Funciones(Logica_Banco):

    def eh_positivo(self, numero1, numero2):
        
        if numero1 > 0 and numero2 > 0:

            return True

        else:

            return False

    def son_iguales(self, numero1, numero2):
        
        if numero1 == numero2:

            return True

        else:
            
            return False

    def maior(self, numero1, numero2):

        if self.eh_positivo(numero1, numero2) is True:

            if numero1 > numero2:

                self.mayor = f'{numero1} es mayor que {numero2}'            

            elif numero2 > numero1: 

                self.mayor = f'{numero2} es mayor que {numero1}'

            else: 
                self.mayor = f"Los numeros {numero1} y {numero2} son iguales, digite numero diferentes"

        return self.mayor
                
    def menor(self, numero1, numero2):

        if self.eh_positivo(numero1, numero2) is True:

            if numero1 < numero2:
                self.menorr = f'{numero1} es menor que {numero2}'
            
            elif numero2 < numero1: 
                self.menorr= f'{numero2} es menor que {numero1}'

            else: 
                self.menorr = f'{numero1} y {numero2} son iguales, digite numeros diferentes'
        
        return self.menorr
                
    def verifica_si_es_par(self, numero):

        if numero > 0:

            if numero % 2 == 0:

                self.par = f'El numero {numero} es par'

            else: 

                self.par = f'El numero {numero} es impar'
        
        else:

            self.par = f'El {numero} numero es negativo'
        
        return self.par

    def mayor_de_la_lista(self, lista):

        variable = 0

        for i in lista:

            if  i > variable:

                variable = i

        self.mayor = f'\nEl numero mayor de la lista es: {variable}'
        return self.mayor

    def cantidad_de_pares_en_lista(self, lista):

        lista_par : int= []
        lista_impar : int= []

        for i in lista:

            if i % 2 == 0:

                lista_par.append(i)
            
            else: 
                lista_impar.append(i)

        self.lista1 = f'\nLista de pares {lista_par}, cantidad: {len(lista_par)}'
        self.lista2 = f'\nLista de impares {lista_impar}, cantidad: {len(lista_impar)}'

    def menor_de_la_lista(self, lista):

        variable = lista[0]

        for i in lista:

            if  i < variable:

                variable = i

        self.menor_lista = f'\nEl numero menor de la lista es: {variable}'
        return self.menor_lista

    def calculadora(self, numero1, numero2, opcion):

        self.operacion = ''

        if opcion == 1:

            resultado = numero1 + numero2
            self.operacion = f'La suma es: {resultado}'

        elif opcion == 2:

            resultado = numero1 - numero2
            self.operacion = f'La resta es: {resultado}'

        elif opcion == 3:

            resultado = numero1 * numero2
            self.operacion = f'La multiplicacion es: {resultado}'

        elif opcion == 4:

            resultado = numero1 / numero2
            self.operacion = f'La division es: {resultado}'
            
        else:
            self.operacion = 'Digite una opcion valida'
        
        return self.operacion 

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
                        
        
        self.letra = f'La letra {letra}, aparece: {cantidad} veces, y la cantidad de numeros: {cantidad_num}'
        return self.letra
    
    def verificar_salario(self, hora, valor, dias):

        salario = (hora * valor) * dias

        self.salario = f'El salario del colaborador por {dias} dias trabajados es: {round(salario, 2)}'
        return self.salario
    
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
            
        self.total = f'\nCantidad en total de datos en total: {(int_cuenta + float_cuenta + str_cuenta)} Cantidad de string: {str_cuenta} Cantidad de int: {int_cuenta} Cantidad de floats: {float_cuenta}'
                

    def main(self):

        self.crear_conexion('base.db')

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
        \n13) --> Base de datos <---
        \n14) Salir
        \nEscoja la opcion: '''

        while True:

            try:

                registro_string = ' '
                funciones = ' '
                funcion_seleccionada = int(input(menu))

                if funcion_seleccionada == 1:
                    
                    numero1 = int(input('\nDigite un numero: '))
                    numero2 = int(input('\nDigite otro numero: '))
                    
                    if self.eh_positivo(numero1, numero2) == True:

                        print('Son positivos')
                        registro_string = f'{numero1} y {numero2} son positivos '
                        funciones = 'Eh_positivo'

                elif funcion_seleccionada == 2:

                    numero1 = int(input('\nDigite un numero: '))
                    numero2 = int(input('Digite otro numero: '))

                    if self.son_iguales(numero1, numero2) == True:

                        print(f"Los numeros {numero1} y {numero2} son iguales ")
                        registro_string = f'{numero1} y {numero2} son iguales '
                    
                    else:
                        print(f"Los numeros {numero1} y {numero2} no son iguales ")
                        registro_string = f'{numero1} no es igual a {numero2}'
                    
                    funciones = 'son_iguales'
                                            
                elif funcion_seleccionada == 3:

                    numero1 = int(input('\nDigite un numero: '))
                    numero2 = int(input('Digite otro numero: '))

                    self.maior(numero1, numero2)
                    print(self.mayor)
                    variable = self.mayor
                    registro_string  = variable
                    funciones = 'maior'

                elif funcion_seleccionada == 4:

                    numero1 = int(input('\nDigite un numero: '))
                    numero2 = int(input('Digite otro numero: '))

                    self.menor(numero1, numero2)                    
                    print(self.menorr)
                    variable = self.menorr
                    registro_string  = variable
                    funciones = 'menor'

                elif funcion_seleccionada == 5:

                    numero = int(input('\nDigite un numero: '))
                    self.verifica_si_es_par(numero)
                    print(self.par)
                    registro_string = self.par
                    funciones = 'Verifica si es par'
                
                elif funcion_seleccionada == 6:

                    lista = []
                    numero = int(input('Cuantos numeros va a inserir en la lista?: '))

                    for i in range (numero):

                        valor=int(input(f"Ingrese el elemento {(i+1)}: "))
                        lista.append(valor)
                    
                    self.mayor_de_la_lista(lista)
                    print(self.mayor)
                    registro_string = self.mayor
                    funciones = 'Mayor de la lista'
                
                elif funcion_seleccionada == 7:

                    lista = []
                    numero = int(input('Cuantos numeros va a inserir en la lista?: '))

                    for i in range (numero):

                        valor=int(input(f"Ingrese el elemento {(i+1)}: "))
                        lista.append(valor)
                    
                    self.cantidad_de_pares_en_lista(lista)
                    print(self.lista1, self.lista2)
                    funciones = 'Cantidad de pares e impares en una lista'
                    registro_string = f'{self.lista1} -- {self.lista2}'

                elif funcion_seleccionada == 8:

                    lista = []
                    numero = int(input('Cuantos numeros va a inserir en la lista?: '))

                    for i in range (numero):

                        valor=int(input(f"Ingrese el elemento {(i+1)}: "))
                        lista.append(valor)
                    
                    self.menor_de_la_lista(lista)
                    print(self.menor_lista)
                    registro_string = self.menor_lista
                    funciones = 'Menor de una lista'

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
                                print(self.operacion)
                                registro_string = self.operacion
                                funciones = "Calculadora"
                                self.insere_registro('Registro', funciones, registro_string)

                        except Exception as e:
                            print('Erro: ', e)

                elif funcion_seleccionada == 10:

                    texto = input('Digite un texto: \n')
                    letra = input('Digite la letra a buscar: ')

                    if len(letra) == 1 and len(texto) >= 10:

                        self.buscar_letra(texto, letra)
                        print(self.letra)

                    else:
                        self.letra = "El texto debe tener por lo menos 10 caracteres"
                        print(self.letra)

                    registro_string = self.letra
                    funciones = 'Buscar letra'
                
                elif funcion_seleccionada == 11:

                    try:

                        horas = int(input('Digite las horas trabajadas: '))
                        valor = float(input('Digite el valor de las horas: '))
                        dias = int(input('Digite cuantos dias trabajo del mes: '))

                        self.verificar_salario(horas, valor, dias)
                        print(self.salario)
                        registro_string = self.salario
                        funciones = "Verificar salario"
                        
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
                            print(self.total)

                        else:
                            self.total = "No cumple con los requisitos."
                            print(self.total)

                        registro_string = self.total
                        funciones = 'Buscar iten en la lista'


                    except Exception as e:
                        print('Erro: ', e)

                elif funcion_seleccionada == 13:
            
                    menu_2 = int(input('Seleccione una opncion \n1) Retorna ultimo registtro \n2) Deletar un registro \n3) Retornar cantidad de registro \n4)Break \nEscoje una opcion: '))
                    
                    if menu_2 == 1:

                        self.retorna_ultimo_registtro_inserido()

                    elif menu_2 == 2:

                        id_lnha = int(input('\nInforme el id de la linea: '))
                        self.deletar_registro(id_lnha)

                    elif menu_2 == 3:

                        self.retornar_cantidad_registro()
                    
                    elif menu_2 == 4:

                        break

                elif funcion_seleccionada == 14:

                    break

                self.insere_registro('Registro', funciones, registro_string)

            except Exception as e:
                print('Erro: ', e)

if __name__ == '__main__':

    objeto = Funciones()
    objeto.main()


