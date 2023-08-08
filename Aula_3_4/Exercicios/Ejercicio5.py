
# Crie uma classe chamada Triangulo que represente um triângulo. A classe deve ter os atributos lado1, lado2 e lado3.
# Crie métodos para verificar se os lados formam um triângulo válido (eh_valido()), calcular o perímetro (calcular_perimetro())
# e exibir o tipo do triângulo com base nos lados (tipo_triangulo())


class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def eh_valido(self):
        return self.lado1 + self.lado2 > self.lado3 and self.lado1 + self.lado3 > self.lado2 and self.lado2 + self.lado3 > self.lado1
    
    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3
    
    def tipo_triangulo(self):
        if not self.eh_valido():
            return "Inválido"
        
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilátero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "Isósceles"
        else:
            return "Escaleno"

# Criando uma instância da classe Triangulo
meu_triangulo = Triangulo(3, 4, 5)

# Testando os métodos
if meu_triangulo.eh_valido():
    print(f"Perímetro do triângulo: {meu_triangulo.calcular_perimetro()}")
    print(f"Tipo do triângulo: {meu_triangulo.tipo_triangulo()}")
else:
    print("Os lados não formam um triângulo válido.")
