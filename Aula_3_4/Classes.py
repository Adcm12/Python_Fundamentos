class ClaseCachorro:

    # Atributos = Variables

    raza = 'Pitbull'
    edad = 4
    cor = 'Cinza'

    # Metodos = Funciones

    def latir(latidas):
        
        for latida in range(latidas):
            print('au au')
    
    def comer(comida, horario):

        print(f'\nau au, comi {comida}, au au en horario {horario}')

    def mostrar_info():
        print(f'El cachorro es de raza: {ClaseCachorro.raza}, y tiene {ClaseCachorro.edad} anos')

class ClasePessoa:

    # Atributos = Variables

    nome = 'Adrian'
    edad = 19
    altura = 180
    peso = 72
    pais_origem = 'Venezuela'
    genero = 'Masculino'

    # Metodos = Funciones

    def decir_hola():
        print(f'\nHola, yo soy {ClasePessoa.nome}')

    def mostrar_datos():

        print(f'Yo tengo {ClasePessoa.edad} anos, {ClasePessoa.altura}cm altura, peso {ClasePessoa.peso}kg, y mi genero es {ClasePessoa.genero}')

    def mostrar_origem():
        print(f'Yo vengo de {ClasePessoa.pais_origem}')

ClaseCachorro.latir(10)
ClaseCachorro.comer('raçao', '10:00am')
ClaseCachorro.mostrar_info()
print('\n---------------------\n')
ClasePessoa.decir_hola()
ClasePessoa.mostrar_datos()
ClasePessoa.mostrar_origem()