from abc import ABC, abstractmethod
import sqlite3

class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @abstractmethod
    def exibir_info(self):
        pass

    @abstractmethod
    def calcular_salario(self):
        pass

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def exibir_info(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, Matrícula: {self.matricula}")

    def calcular_salario(self):
        pass

class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina, carga_horaria, valor_por_hora):
        super().__init__(nome, idade)
        self.disciplina = disciplina
        self.carga_horaria = carga_horaria
        self.valor_por_hora = valor_por_hora
    
    def exibir_info(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, Disciplina: {self.disciplina}")

    def calcular_salario(self):
        salario = self.carga_horaria * self.valor_por_hora
        return salario

def adicionar_pessoa():
    tipo = input("Digite 'aluno' para adicionar um aluno, ou 'professor' para adicionar um professor: ")
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    
    if tipo == 'aluno':
        matricula = input("Digite o número de matrícula do aluno: ")
        aluno = Aluno(nome, idade, matricula)
        salario = None
        info_extra = matricula
    elif tipo == 'professor':
        disciplina = input("Digite a disciplina lecionada pelo professor: ")
        carga_horaria = int(input("Digite a carga horária do professor: "))
        valor_por_hora = float(input("Digite o valor por hora do professor: "))
        professor = Professor(nome, idade, disciplina, carga_horaria, valor_por_hora)
        salario = professor.calcular_salario()
        info_extra = disciplina
    
    conn = sqlite3.connect("pessoas.db")
    cursor = conn.cursor()

    cursor.execute('INSERT INTO Pessoas (tipo, nome, idade, info_extra, salario) VALUES (?, ?, ?, ?, ?)',
                   (tipo, nome, idade, info_extra, salario))
    conn.commit()

    conn.close()

def listar_pessoas():
    conn = sqlite3.connect("pessoas.db")
    cursor = conn.cursor()

    cursor.execute('SELECT tipo, nome, idade, info_extra, salario FROM Pessoas')
    pessoas = cursor.fetchall()

    for pessoa in pessoas:
        tipo, nome, idade, info_extra, salario = pessoa

        if tipo == 'aluno':
            print(f"\nAluno: \nNome: {nome}, Idade: {idade}, Matrícula: {info_extra}")

        elif tipo == 'professor':
            print(f"\nProfessor: \nNome: {nome}, Idade: {idade}, Disciplina: {info_extra}, Salário: {salario}")

    conn.close()

conn = sqlite3.connect("pessoas.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Pessoas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tipo TEXT,
        nome TEXT,
        idade INTEGER,
        info_extra TEXT,
        salario REAL
    )
''')

conn.commit()
conn.close()

while True:
    adicionar_pessoa()
    listar_pessoas()
    continuar = input("Deseja adicionar outra pessoa? (sim/não): ")
    if continuar.lower() != 'sim':
        break
