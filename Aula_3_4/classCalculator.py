class Calculadora:

    operaciones_limite = 10
    input_mensage = '\ninforme un numero entre 1 y 5: \n'
    input_mensage += '\n1 = Sumar'
    input_mensage += '\n2 = Restarr'
    input_mensage += '\n3 = multiplicarr'
    input_mensage += '\n4 = Dividir'
    input_mensage += '\n5 = Modulo'
    input_mensage += '\n6 = Salir\n: '

    def sumar(numero1, numero2):
        print(f'La suma de los numeros es: {numero1 + numero2}\n')

    def restar(numero1, numero2):
        print(f'La resta de los numeros es: {numero1 - numero2}\n')

    def multiplicar(numero1, numero2):
        print(f'La multiplicacion de los numeros es: {numero1 * numero2}\n')

    def division(numero1, numero2):
        print(f'La Division de los numeros es: {numero1 / numero2}\n')

    def modulo(numero1, numero2):
        print(f'El modulo de los numeros es: {numero1 % numero2}\n')

    def controle_operaciones():
        contador = 0

        while contador < Calculadora.operaciones_limite:

            contador +=1

            try :
                numero_1 = int(input('Informe el primero numero: '))
                numero_2 = int(input('Informe el segundo numero: '))
                
                if numero_1 > 0 and numero_2 > 0:

                    while True:
                        try: 

                            opcion = int (input(Calculadora.input_mensage))

                            if opcion == 1:
                                Calculadora.sumar(numero_1, numero_2)

                            elif opcion == 2:
                                Calculadora.restar(numero_1, numero_2)

                            elif opcion == 3:
                                Calculadora.multiplicar(numero_1, numero_2)

                            elif opcion == 4:
                                Calculadora.division(numero_1, numero_2)

                            elif opcion == 5:
                                Calculadora.modulo(numero_1, numero_2)
                            
                            elif opcion == 6:
                                break

                            else: 
                                ValueError()                           
                        except:
                            print('Error')            
                else:
                    print('Informe numeros positivos')

            except:
                print("Error")

Calculadora.controle_operaciones()