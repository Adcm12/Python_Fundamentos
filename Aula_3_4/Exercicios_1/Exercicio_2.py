# Crie uma classe chamada Pessoa com o atributo nome (public). 
# Implemente métodos set_nome(novo_nome) e get_nome() para manipular esse atributo.

class Pessoa():
    def __init__(self, nomee):
        self.nomee = nomee
        print('Objeto instanciado con sucesso!!!')


    @property
    def nome(self):

        return f'\nNome:  {self.nomee}'
    
    
    @nome.setter
    def set_nome(self, nome_novo):

        print(f'\nSetou de {self.nomee}, para {nome_novo}')
        self.nomee = nome_novo


if __name__=='__main__':

    nome1 = Pessoa('Adrian')
    print(nome1.nome)

    nome1.set_nome = 'David'
    print(nome1.set_nome)