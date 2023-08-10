class Triangulo:

    def __init__(self, lado1, lado2, lado3):

        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

        print('\nObjetos instanciados con sucesso!!!')
    

    def eh_valido(self):
        
        valido1 = self.lado1 + self.lado2 > self.lado3 
        valido2 = self.lado1 + self.lado3 > self.lado2 
        valido3 = self.lado2 + self.lado3 > self.lado1

        return valido1 is True and valido2 is True and valido3 is True
    
            
    def calcular_perimetro(self):

        return print(f'\nEl perimetro del triangulo es: {self.lado1 + self.lado2 + self.lado3}')
    


    def tipo_triangulo(self):

        if not Triangulo.eh_valido(self):

            print('\nNo es valido!')

        Triangulo.calcular_perimetro(self)

        if self.lado1 == self.lado2 == self.lado3:

            print('\nEl triagulo es equilatero')
        
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:

            print('\nEl triangulo es Isosceles')

        else:

            print('\nEl triangulo es Escaleno')        

if __name__=='__main__':

    self1 = Triangulo(lado1 = 5, lado2 = 4.6, lado3 = 4.6)
    self1.tipo_triangulo()
    self2 = Triangulo(lado1 = 4.6, lado2 = 5, lado3 = 4.6)
    self2.tipo_triangulo()
    self3 = Triangulo(lado1 = 5, lado2 = 5, lado3 = 4.6)
    self3.tipo_triangulo()