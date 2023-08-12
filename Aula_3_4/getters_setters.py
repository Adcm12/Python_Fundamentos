class Animal():

    # Constructor

    # PRIVATE -> __nome
    # Protected -> _nome
    # Public

    def __init__(self, raza, cor, edad, nome):

        self._raza = raza
        self._cor = cor
        self._edad = edad
        self.__nome = nome
        print('Objetos instanciados con sucesso')


    #Getters
    @property
    def razas(self):

        return '\nRaza: '+ self._raza
    
    @property
    def cor(self):

        return '\nCor: '+self._cor
    
    @property
    def edad(self):

        return f'\nEdad: {self._edad}'
    

    @property
    def nome(self):

        return f'\nNome: {self.__nome}'
    

    #Setters
    @razas.setter
    def raza(self, raza_nova):

        print(f'Setou de {self.raza}, para {raza_nova}')
        self._raza = raza_nova

    @cor.setter
    def cor(self, cor_novo):
        print(f'Setou de {self.cor}, para {cor_novo}')
        self._cor = cor_novo

    @edad.setter
    def edad(self, edad_nova):

        print(f'Setou de {self.edad}, para {edad_nova}')
        self._edad = edad_nova

    @nome.setter
    def nome(self, nome_nova):

        print(f'Setou de {self.__nome}, para {nome_nova}')
        self.__nome = nome_nova


leon = Animal('Leon', 'preto', 15, 'Simba')
gato = Animal('gato', 'beige', 9, 'Garfield')
pantera = Animal('pantera', 'cinza', 10, 'Tachala')

print(leon.razas, leon.cor, leon.edad, leon.nome)
print(gato.razas, gato.cor, gato.edad, gato.nome)
print(pantera.razas, pantera.cor, pantera.edad, pantera.nome)


