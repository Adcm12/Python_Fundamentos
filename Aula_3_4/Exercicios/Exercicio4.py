#  Crie uma classe chamada Agenda que represente uma agenda de contatos. A classe deve ter um atributo para armazenar uma lista de contatos.
#  Crie métodos para adicionar (adicionar_contato(nome, telefone)), remover (remover_contato(nome)), e exibir todos os contatos (exibir_contatos()).

class Agenda:
    
    def __init__(self):
        self.contatos = []
    
    def adicionar_contato(self, nome, telefone):
        contato = {'nome': nome, 'telefone': telefone}
        self.contatos.append(contato)
        print(f"Contato {nome} adicionado com sucesso.")
    
    def remover_contato(self, nome):
        contatos_restantes = [contato for contato in self.contatos if contato['nome'] != nome]
        if len(contatos_restantes) < len(self.contatos):
            self.contatos = contatos_restantes
            print(f"Contato {nome} removido com sucesso.")
        else:
            print(f"Contato {nome} não encontrado na agenda.")
    
    def exibir_contatos(self):
        if self.contatos:
            print("Lista de contatos:")
            for contato in self.contatos:
                print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}")
        else:
            print("A agenda está vazia.")

# Criando uma instância da classe Agenda
minha_agenda = Agenda()

# Testando os métodos
minha_agenda.adicionar_contato("Alice", "123456789")
minha_agenda.adicionar_contato("Bob", "987654321")
minha_agenda.exibir_contatos()

minha_agenda.remover_contato("Alice")
minha_agenda.exibir_contatos()

minha_agenda.remover_contato("Charlie")  # Tentando remover um contato que não existe
