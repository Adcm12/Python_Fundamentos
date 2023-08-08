#  Crie uma classe chamada Livro que represente um livro.
#  A classe deve ter os atributos titulo, autor e ano. Crie um método para exibir as informações do livro (exibir_informacoes()).

class Livro:

    # Atributos

    titulo = 'Harry Potter y el prisionero de Azkaban'
    autor = 'Jk Rowling'
    ano = 1999

    # Metodos

    def exibir_informacion():

        print(f'\nLibro: {Livro.titulo} \nAutor: {Livro.autor} \nAno: {Livro.ano}')

Livro.exibir_informacion()