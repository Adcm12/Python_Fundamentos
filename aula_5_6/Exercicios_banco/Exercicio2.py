from abc import ABC, abstractmethod
import sqlite3

# Clases

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
        print(f"\nNome: {self.nome}, Idade: {self.idade}, Matrícula: {self.matricula}")

    def calcular_salario(self):
        pass

class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina, carga_horaria, valor_por_hora):
        super().__init__(nome, idade)
        self.disciplina = disciplina
        self.carga_horaria = carga_horaria
        self.valor_por_hora = valor_por_hora
    
    def exibir_info(self):
        print(f"\nNome: {self.nome}, Idade: {self.idade}, Disciplina: {self.disciplina}")

    def calcular_salario(self):
        salario = self.carga_horaria * self.valor_por_hora
        return salario

# Funcion para adicionar personas

def adicionar_pessoa():

    tipo = input("\nDigite 'alumno' para adicionar um alumno, ou 'profesor' para adicionar um profesor: ")
    nome = input("\nDigite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    
    if tipo == 'alumno':

        matricula = input("Digite o número de matrícula do aluno: ")
        aluno = Aluno(nome, idade, matricula)
        salario = None
        info_extra = matricula

    elif tipo == 'profesor':

        disciplina = input("Digite a disciplina lecionada pelo profesor: ")
        carga_horaria = int(input("Digite a carga horária do profesor: "))
        valor_por_hora = float(input("Digite o valor por hora do profesor: "))
        professor = Professor(nome, idade, disciplina, carga_horaria, valor_por_hora)
        salario = professor.calcular_salario()
        info_extra = disciplina
    
    conn = sqlite3.connect("pessoas.db")
    cursor = conn.cursor()

    cursor.execute('INSERT INTO Pessoas (tipo, nome, idade, info_extra, salario) VALUES (?, ?, ?, ?, ?)',
                   (tipo, nome, idade, info_extra, salario))
    conn.commit()


def mostrar_personas():

    conn = sqlite3.connect("pessoas.db")
    cursor = conn.cursor()

    tipo = input('Digite el tipo de persona, "alumno" o "professor": ')

    if tipo == 'alumno':

        cursor.execute("SELECT nome, idade, info_extra FROM Pessoas WHERE tipo = 'alumno'")
        alunos = cursor.fetchall()

        for aluno in alunos:

            nome, idade, info_extra = aluno

            print(f"\nAlumno:\nNombre: {nome}, Edad: {idade}, Matrícula: {info_extra}")

    elif tipo == 'professor':

        cursor.execute("SELECT nome, idade, info_extra, salario FROM Pessoas WHERE tipo = 'profesor'")        
        profesores = cursor.fetchall()

        for professor in profesores:

            nome, idade, info_extra, salario = professor
            print(f"\nProfesor:\nNombre: {nome}, Edad: {idade}, Disciplina: {info_extra}, Salario: {salario}")

    conn.close()

def crear_tabela():

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


while True:

    crear_tabela()
    conn = sqlite3.connect("pessoas.db")
    cursor = conn.cursor()

    opcion = int(input('Digite uma opcao: \n 1) Adicionar pessoas \n 2) Mostrar pessoas \n 3) Salir:  '))

    if opcion == 1 :

        adicionar_pessoa()

    elif opcion == 2:

        mostrar_personas()

    elif opcion == 3:

        break
    else: 
        print('Opcao invalida!\n')
conn.close()