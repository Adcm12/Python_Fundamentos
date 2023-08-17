import sqlite3

class Aluno:
    def __init__(self, id, nome, idade, nota):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.nota = nota

    def get_id(self):
        return self.id

    def get_nome(self):
        return self.nome

    def get_idade(self):
        return self.idade

    def get_nota(self):
        return self.nota

    def set_nome(self, nome):
        self.nome = nome

    def set_idade(self, idade):
        self.idade = idade

    def set_nota(self, nota):
        self.nota = nota

    @staticmethod
    def criar_aluno(nome, idade, nota):

        conexao = sqlite3.connect('escola.db')
        cursor = conexao.cursor()
        cursor.execute('INSERT INTO Alunos (nome, idade, nota) VALUES (?, ?, ?)', (nome, idade, nota))
        conexao.commit()
        conexao.close()

    @staticmethod
    def buscar_aluno_por_id(id):

        conexao = sqlite3.connect('escola.db')
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM Alunos WHERE id = ?', (id,))
        aluno_data = cursor.fetchone()
        conexao.close()
        
        if aluno_data:
            id, nome, idade, nota = aluno_data
            return Aluno(id, nome, idade, nota)
        else:
            return None

    @staticmethod
    def listar_alunos():
        conexao = sqlite3.connect('escola.db')
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM Alunos')
        alunos_data = cursor.fetchall()
        conexao.close()
        alunos = []
        for aluno_data in alunos_data:
            id, nome, idade, nota = aluno_data
            aluno = Aluno(id, nome, idade, nota)
            alunos.append(aluno)
        return alunos

def main():
    conexao = sqlite3.connect('escola.db')
    cursor = conexao.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Alunos (id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER, nota REAL)')
    conexao.commit()
    conexao.close()

    while True:
        print("\nMenu:")
        print("1 - Criar Aluno")
        print("2 - Buscar Aluno por ID")
        print("3 - Listar Alunos")
        print("4 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Informe o nome do aluno: ")
            idade = int(input("Informe a idade do aluno: "))
            nota = float(input("Informe a nota do aluno: "))
            Aluno.criar_aluno(nome, idade, nota)
            print("Aluno criado com sucesso!")

        elif escolha == '2':
            id = int(input("Informe o ID do aluno: "))
            aluno = Aluno.buscar_aluno_por_id(id)
            if aluno:
                print(f"ID: {aluno.get_id()}")
                print(f"Nome: {aluno.get_nome()}")
                print(f"Idade: {aluno.get_idade()}")
                print(f"Nota: {aluno.get_nota()}")
            else:
                print("Aluno não encontrado.")

        elif escolha == '3':
            alunos = Aluno.listar_alunos()
            print("\nLista de Alunos:")
            for aluno in alunos:
                print(f"ID: {aluno.get_id()}, Nome: {aluno.get_nome()}, Idade: {aluno.get_idade()}, Nota: {aluno.get_nota()}")

        elif escolha == '4':
            break

        else:
            print("Opção inválida. Escolha uma opção válida.")

if __name__ == '__main__':
    main()
