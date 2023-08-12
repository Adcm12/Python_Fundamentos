# Crie uma classe chamada Produto que represente um produto em uma loja. A classe deve ter os atributos:
# nome (private), preco e codigo (public). Crie um construtor para inicializar esses atributos 
# e métodos get_nome(), get_preco() e set_preco(novo_preco) para acessar e modificar o preço.

class Producto():

    # Atributos:

    def __init__(self, nome, preço, codigo):

        self.__nome = nome
        self.preço = preço
        self.codigo = codigo

        print('Objeto instanciado con sucesso!!!')

    #Getters
    @property
    def nome(self):

        return f'\nNome:  {self.__nome}'
    
    
    @property
    def get_preço(self):

        return f'\nPreço:  {self.preço}'
    
    
    @property
    def get_codigo(self):

        return f'\nCodigo: {self.codigo}'


    #Setters
    @get_preço.setter
    def set_preço(self, preço_novo):

        print(f'Setou de {self.preço}, para {preço_novo}')
        self.preço = preço_novo


if __name__=='__main__':

    producto1 = Producto('Telefone', 1500, 1)      
    producto2 = Producto('Relogio', 3560, 2)      
    producto3 = Producto('Notebook', 8560, 3)      
    producto4 = Producto('Tv', 2000, 4)      

    print(producto1.nome, producto1.get_preço, producto1.get_codigo)
    print(producto2.nome, producto2.get_preço, producto2.get_codigo)
    print(producto3.nome, producto3.get_preço, producto3.get_codigo)
    print(producto4.nome, producto4.get_preço, producto4.get_codigo)
