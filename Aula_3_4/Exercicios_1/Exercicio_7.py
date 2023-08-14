# Crie uma classe chamada Veiculo com os atributos marca (private), modelo (private) e ano (private). Crie um construtor para inicializar 
# esses atributos. Implemente métodos get_marca(), get_modelo() e exibir_informacoes().

class Vehiculo():

    def __init__(self, marca, modelo, ano):

        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano


    @property
    def get_marca(self):
        return self.__marca
    
    
    @property
    def get_modelo(self):
        return self.__modelo
    
    
    @property
    def get_ano(self):
        return self.__ano
    

    def exibir_informacion(self):

        return f'\nMarca: {self.__marca}  \nModelo: {self.__modelo}  \nAno: {self.__ano}'
    
    
if __name__ == '__main__':

    carro1 = Vehiculo('Maserati', 'GranTurismo', 2023)
    print(carro1.exibir_informacion())