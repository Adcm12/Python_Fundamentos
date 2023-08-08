class Calculadora:

    operaciones_limite = 10
    input_mensage = 'informe un numero entre 1 y 5: '
    input_mensage += '\n1 = Sumar'
    input_mensage += '\n2 = Restarr'
    input_mensage += '\n3 = multiplicarr'
    input_mensage += '\n4 = Dividir'
    input_mensage += '\n5 = Modulo'

    def sumar():
        ...
    def restar():
        ...
    def multiplicar():
        ...
    def division():
        ...
    def modulo():
        ...
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

                            else: 
                                ValueError()                           
                        except:
                            print('Error')            
                else:
                    print('Informe numeros positivos')

            except:
                print("Error")