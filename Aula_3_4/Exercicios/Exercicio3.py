# Crie uma classe chamada Carro que simule um carro. A classe deve ter os atributos marca, modelo e ano.
# Crie métodos para ligar (ligar()), desligar (desligar()) e exibir as informações do carro (exibir_informacoes()).
import time

class Carro():

    # Atributos

    marca = 'Maserati'
    modelo = 'GranTurismo'
    ano = 2023
    cor = "Prata"
    ligado = False

    # Metodos 

    def ligar():

        if not Carro.ligado:

            Carro.ligado=True
            time.sleep(1.5)
            print('\nCarro ligo com sucesso!')
        else:
            print('\nO carro ja esta ligado!\n')

    def desligar():

        if Carro.ligado:

            Carro.ligado=False
            time.sleep(1.5)
            print('\nCarro desligou con sucesso!')
        else:
            print("\nO carro já está desligado!")
    
    def exibir_informacion():

        estado = "Ligado" if Carro.ligado else "Desligado"
        time.sleep(2)
        print(f'\nMarca: {Carro.marca} \nModelo: {Carro.modelo} \nAno: {Carro.ano} \nCor: {Carro.cor} \nEstado: {estado}')

    def script():

        while True:
                
            message = input('''\nBienvenido a la interfaz de su carro, que desea hacer?: 
                            \n1) Ligar
                            \n2) Desligar
                            \n3) Mostrar informaçao
                            \n4) Salir
                            \nElija una opcion: ''')
            
            if message == '1':

                Carro.ligar()

            elif message == '2':

                Carro.desligar()
            
            elif message == '3':

                Carro.exibir_informacion()
            
            elif message == '4':

                break

            else:

                print('Informe una opcion valida!!!')

Carro.script()