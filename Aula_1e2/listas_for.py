import os

def mostrar_lista():
    lista_dados = [

        1,
        2,
        3,
        4,
        'hello',
        'Hola',
        True,
        False

    ]

    for i in lista_dados:
        print(i)

def mostrar_dados():

    lista1 = []

    for i in range(5):
        item = input(f'Informe el {i+1}° item: ')
        lista1.append(item)

    for item in lista1:
        print(item)    

def script_lista():
    lista_dados = []

    contador =0

    while contador <10:
        contador +=1
        item_informadp = input(f'Informe el {contador}° item: ')
        lista_dados.append(item_informadp)

    for indice, itemm in enumerate(lista_dados):
        print(f'\nposicion {indice+1} - valor: {itemm}')

    #----------
    while True:
        try:
            posicion_item = int(input('Informe la poscion del item: '))
            print(f'El item que esta en la poscicon {posicion_item} e: {lista_dados[posicion_item]}')

            verificacion = input('\ns para salir: ')
            if verificacion == 's':
                break

        except:
            print('Informe solo enteros para las posciones...')
        
if __name__ == '__main__':
    os.system('cls')

    # mostrar_lista()
    # mostrar_dados()
    script_lista()


