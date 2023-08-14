# Expanda o exercício da classe Triangulo. Torne os atributos lado1, lado2 e lado3 private. Crie métodos get_lado1(), get_lado2() e get_lado3()
# para acessar os lados e métodos set_lado1(novo_lado), set_lado2(novo_lado) e set_lado3(novo_lado) para modificar os lados. No método eh_valido(),
# verifique se os lados formam um triângulo válido.

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__lado3 = lado3

    @property
    def get_lado1(self):
        return f'\nLado 1: {self.__lado1}'
    
    @property
    def get_lado2(self):
        return f'\nLado 2: {self.__lado2}'
    
    @property
    def get_lado3(self):
        return f'\nLado 3: {self.__lado3}'
    
    @get_lado1.setter
    def set_lado1(self, lado1_novo):
        self.__lado1 = lado1_novo
        print(f'\nLado 1 novo: {lado1_novo}')
        
    @get_lado2.setter
    def set_lado2(self, lado2_novo):
        self.__lado2 = lado2_novo
        print(f'Lado 2 novo: {lado2_novo}')

    @get_lado3.setter
    def set_lado3(self, lado3_novo):
        self.__lado3 = lado3_novo
        print(f'Lado 3 novo: {lado3_novo}')

    def eh_valido(self):
        valido1 = self.__lado1 + self.__lado2 > self.__lado3 
        valido2 = self.__lado1 + self.__lado3 > self.__lado2 
        valido3 = self.__lado2 + self.__lado3 > self.__lado1

        if valido1 and valido2 and valido3:
            return '\nEs un triângulo válido!'
        else:
            return "\nNo es un triângulo!"

    def __str__(self):
        return f'{self.get_lado1}\n{self.get_lado2}\n{self.get_lado3}'

if __name__ == '__main__':

    triangulo1 = Triangulo(lado1=5, lado2=4.6, lado3=4.6)
    print(triangulo1.get_lado1, triangulo1.get_lado2, triangulo1.get_lado3)
    print(triangulo1.eh_valido())

    triangulo1.set_lado1 = 10
    triangulo1.set_lado2 = 9
    triangulo1.set_lado3 = 7

    print(triangulo1.eh_valido()) 






