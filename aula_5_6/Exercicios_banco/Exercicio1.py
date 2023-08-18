# 1 - Neste exercício, você vai criar uma aplicação de gerenciamento de alunos usando SQLite3 e programação orientada
# a objetos (POO) em Python. A aplicação permitirá criar, visualizar, atualizar e excluir registros de alunos em uma
# tabela chamada Alunos no banco de dados. Utilize a biblioteca sqlite3 para criar um banco de dados chamado escola.db.
# Crie uma tabela chamada Alunos com os seguintes campos: id, nome, idade e nota. Crie uma classe chamada Aluno.
# Crie os atributos id, nome, idade e nota na classe. Implemente o construtor __init__() para receber os valores dos atributos.
# Crie métodos de getters (get_id(), get_nome(), get_idade(), get_nota()) para acessar os valores dos atributos.
# Crie métodos de setters (set_nome(), set_idade(), set_nota()) para definir os valores dos atributos.
# Crie um método estático na classe Aluno chamado criar_aluno() que aceita os valores de nome, idade e nota como parâmetros.
# Este método deve criar uma instância da classe Aluno com os valores passados e inserir um registro na tabela Alunos com esses valores.
# Crie um método estático chamado buscar_aluno_por_id() que aceita um ID como parâmetro e retorna uma instância de Aluno com os valores
# correspondentes da tabela Alunos. Crie um método estático chamado listar_alunos() que consulta a tabela Alunos e retorna uma lista de
# instâncias de Aluno. Crie um loop principal que exibe um menu para o usuário com opções como "Criar Aluno", "Buscar Aluno por ID", "Listar Alunos"
# e "Sair". Implemente a lógica para cada opção do menu, chamando os métodos correspondentes da classe Aluno. Na opção "Criar Aluno", solicite ao
# usuário que insira nome, idade e nota e, em seguida, chame o método criar_aluno(). Na opção "Buscar Aluno por ID", peça ao usuário para inserir
# um ID e exiba os detalhes do aluno correspondente usando o método buscar_aluno_por_id(). Na opção "Listar Alunos", liste todos os alunos usando o
# método listar_alunos(). Ao sair do loop principal, feche a conexão com o banco de dados.

import os
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
            
        try:

            menu = '''Menu:
                \n1 - Criar Aluno
                \n2 - Buscar Aluno por ID
                \n3 - Listar Alunos
                \n4 - Sair
                \nEscolha uma opção: '''
            
            escolha = input(menu)

            if escolha == '1':

                nome = input("\nInforme o nome do aluno: ")
                idade = int(input("Informe a idade do aluno: "))
                nota = float(input("Informe a nota do aluno: "))

                Aluno.criar_aluno(nome, idade, nota)
                os.system('cls')
                print("Aluno criado com sucesso!")

            elif escolha == '2':

                id = int(input("\nInforme o ID do aluno: "))
                aluno = Aluno.buscar_aluno_por_id(id)

                os.system('cls')
                if aluno:

                    print(f"ID: {aluno.get_id()}")
                    print(f"Nome: {aluno.get_nome()}")
                    print(f"Idade: {aluno.get_idade()}")
                    print(f"Nota: {aluno.get_nota()}\n")

                else:
                    print("Aluno não encontrado.")

            elif escolha == '3':

                alunos = Aluno.listar_alunos()
                os.system('cls')            
                print("Lista de Alunos:")

                for aluno in alunos:
                    print(f"\nID: {aluno.get_id()}, Nome: {aluno.get_nome()}, Idade: {aluno.get_idade()}, Nota: {aluno.get_nota()}")

            elif escolha == '4':
                break

            else:
                print("Opção inválida. Escolha uma opção válida.")

        except Exception as e:
            print(f'Ocurrió un error: {str(e)}')

if __name__ == '__main__':
    os.system('cls')
    main()
