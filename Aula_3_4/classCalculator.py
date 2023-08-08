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
        print(f'\033[034mA La suma de los numeros es: {numero1 + numero2}\n \033[0m')

    def restar(numero1, numero2):
        print(f'\31[030m La resta de los numeros es: {numero1 - numero2}\n\33[0m')

    def multiplicar(numero1, numero2):
        print(f'\34[030m La multiplicacion de los numeros es: {numero1 * numero2}\n\33[0m')

    def division(numero1, numero2):
        print(f'\35[030m La Division de los numeros es: {numero1 / numero2}\n\33[0m')

    def modulo(numero1, numero2):
        print(f'\36[030m El modulo de los numeros es: {numero1 % numero2}\n\33[0m')

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
                                break

                            elif opcion == 2:
                                Calculadora.restar(numero_1, numero_2)
                                break

                            elif opcion == 3:
                                Calculadora.multiplicar(numero_1, numero_2)
                                break

                            elif opcion == 4:
                                Calculadora.division(numero_1, numero_2)
                                break

                            elif opcion == 5:
                                Calculadora.modulo(numero_1, numero_2)
                                break
                            
                            elif opcion == 6:
                                break

                            else: 
                                ValueError()                           
                        except:
                            print('Error')            
                else:
                    print('Informe numeros positivos')

            except KeyboardInterrupt:
                quit()
            except:
                print("Error")


    

Calculadora.controle_operaciones()