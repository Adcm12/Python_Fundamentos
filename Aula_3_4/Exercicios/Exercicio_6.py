# Crie uma classe Livro com construtor que aceite os parâmetros titulo, autor e ano. Crie métodos get_titulo(), get_autor()
# e get_ano() para acessar esses atributos. 

class Livro:

    def __init__(self, titulo, autor, ano):

        self.titulo = titulo
        self.autor = autor
        self.ano = ano


    @property
    def get_titulo(self):
        return f'\nTitulo: {self.titulo}'
    
    
    @property
    def get_autor(self):
        return f'\nAutor: {self.autor}'
    
    
    @property
    def get_ano(self):
        return f'\nAno: {self.ano}'
    
    
if __name__ == '__main__':

    libro1 = Livro('Harry Potter y el prisionero de Azkaban', 'Jk Rowling', 1999)
    print(libro1.get_titulo, libro1.get_autor, libro1.get_ano)