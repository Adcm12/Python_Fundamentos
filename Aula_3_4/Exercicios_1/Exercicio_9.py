# Crie uma classe chamada Animal. Defina um atributo especie com visibilidade default.
# Crie métodos get_especie() e set_especie(nova_especie) para manipular esse atributo.

class Animal:
    def __init__(self, especie):

        self.especie = especie  

    def get_especie(self):

        return f'\nEspecie: {self.especie}'
    

    def set_especie(self, nova_especie):

        self.especie = nova_especie
        print(f'\nNova espécie: {nova_especie}')


meu_animal = Animal("Cachorro")

print(meu_animal.get_especie())

meu_animal.set_especie("Gato")

