#Crie uma classe chamada Aluno que represente um aluno. A classe deve ter os atributos nome, matricula e notas (uma lista de notas).
#Crie métodos para calcular a média (calcular_media()) e exibir o status do aluno com base na média (exibir_status()).

class Aluno:
    def __init__(self, nome, matricula, notas):
        self.nome = nome
        self.matricula = matricula
        self.notas = notas

    def calcular_media(self):
        if not self.notas:
            return 0.0
        return sum(self.notas) / len(self.notas)

    def exibir_status(self):
        media = self.calcular_media()
        if media >= 7.0:
            return f"O aluno {self.nome} ({self.matricula}) foi aprovado com média {media:.2f}. Parabéns!"
        elif media >= 5.0:
            return f"O aluno {self.nome} ({self.matricula}) está de recuperação com média {media:.2f}. Estude um pouco mais."
        else:
            return f"O aluno {self.nome} ({self.matricula}) foi reprovado com média {media:.2f}. Estude mais para o próximo semestre."

# Exemplo de uso
notas_aluno1 = [8.5, 7.0, 9.2]
aluno1 = Aluno("João", "2023001", notas_aluno1)
print(aluno1.exibir_status())

notas_aluno2 = [5.0, 6.2, 4.8]
aluno2 = Aluno("Maria", "2023002", notas_aluno2)
print(aluno2.exibir_status())

notas_aluno3 = []
aluno3 = Aluno("Pedro", "2023003", notas_aluno3)
print(aluno3.exibir_status())
