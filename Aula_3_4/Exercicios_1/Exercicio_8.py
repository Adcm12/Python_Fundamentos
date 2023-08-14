#  Crie uma classe chamada Escola. Defina um atributo alunos como private (uma lista vazia no construtor). Crie métodos para adicionar
#  (adicionar_aluno(aluno)), remover (remover_aluno(aluno)) e exibir a lista de alunos (exibir_alunos()).
#  Crie um construtor e trabalhe a manipulação da classe e dos dados via objetos.


class Escola:
    def __init__(self):
        self.__alunos = []


    def adicionar_aluno(self, aluno):
        self.__alunos.append(aluno)
        print(f"\nAluno {aluno} adicionado com sucesso.")


    def remover_aluno(self, aluno):
        if aluno in self.__alunos:
            self.__alunos.remove(aluno)
            print(f"\nAluno {aluno} removido com sucesso.")

        else:
            print(f"\nAluno {aluno} não encontrado na lista.")


    def exibir_alunos(self):
        print("\nLista de alunos: ")
        for aluno in self.__alunos:
            print(aluno)


if __name__ == '__main__':
        
    minha_escola = Escola()

    minha_escola.adicionar_aluno("João")
    minha_escola.adicionar_aluno("Maria")
    minha_escola.adicionar_aluno("Carlos")

    minha_escola.exibir_alunos()

    minha_escola.remover_aluno("Maria")

    minha_escola.exibir_alunos()

