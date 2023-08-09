class Pessoa():

    nome = 'Adrian'
    edad = 19
    origem = 'Venezuela'

    def decir_hola(self):

        print(f'Hola soy {Pessoa.nome}')

    def pensar(self):

        print('Yo estoy pensando')

    def comprar(self):

        print('Compra realizada!')

    def get_nome(self):

        return Pessoa.nome
    def get_edad(self):

        return Pessoa.edad
    
    def get_origem(self):

        return Pessoa.origem
    

    # setter para setar el nombre

    def setter_nome(self, nome_novo):

        Pessoa.nome = nome_novo
    
    def setter_edad(self, edad_nova):

        Pessoa.edad = edad_nova



pessoa_1 = Pessoa()
pessoa_2 = Pessoa()

pessoa_1.decir_hola()
pessoa_2.decir_hola()
pessoa_1.comprar()

print(pessoa_1.get_nome())
print(pessoa_1.get_edad())
print(pessoa_1.get_origem())

pessoa_1.setter_nome('David')
print(pessoa_1.get_nome())

pessoa_1.setter_edad(30)
print(pessoa_1.get_edad())


