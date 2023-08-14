# Crie uma classe chamada Triangulo que represente um triângulo. A classe deve ter os atributos lado1, lado2 e lado3.
# Crie métodos para verificar se os lados formam um triângulo válido (eh_valido()), calcular o perímetro (calcular_perimetro())
# e exibir o tipo do triângulo com base nos lados (tipo_triangulo())

class Triangulo:

    lado1 = int(input('\nIngresa un lado del triangulo: '))
    lado2 = int(input('Ingresa otro lado del triangulo: '))
    lado3 = int(input('Ingresa otro lado del triangulo: '))

    def eh_valido(lado1, lado2, lado3):
        
        if Triangulo.lado1 + Triangulo.lado2 > Triangulo.lado3 and Triangulo.lado1 + Triangulo.lado3 > lado2 and lado2 + Triangulo.lado3 > Triangulo.lado1:

            return
        
    def calcular_perimetro(lado1, lado2, lado3):

        print(f'\nEl perimetro del triangulo es: {Triangulo.lado1 + Triangulo.lado2 + Triangulo.lado3}')

        return 
    
    def tipo_triangulo(lado1, lado2, lado3):

        if not Triangulo.eh_valido(lado1, lado2, lado3):

            print('\nNo es valido!')

        Triangulo.calcular_perimetro(lado1, lado2, lado3)

        if Triangulo.lado1 == Triangulo.lado2 == Triangulo.lado3:

            print('\nEl triagulo es equilatero')
        
        elif Triangulo.lado1 == Triangulo.lado2 or Triangulo.lado1 == Triangulo.lado3:

            print('\nEl triangulo es Isosceles')

        else:

            print('\nEl triangulo es Escaleno')

Triangulo.tipo_triangulo(Triangulo.lado1, Triangulo.lado2, Triangulo.lado3)

    