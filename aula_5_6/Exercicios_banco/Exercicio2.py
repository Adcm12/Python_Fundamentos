# Neste exercício, você criará uma hierarquia de classes envolvendo uma classe abstrata Pessoa, com subclasses Aluno e Professor.
# Cada classe deve implementar métodos específicos, usando conceitos de abstração, herança e programação orientada a objetos (POO).
# Crie uma classe abstrata chamada Pessoa com o método abstrato exibir_info() e calcular_salario().
# Implemente o método exibir_info() para exibir informações básicas da pessoa, como nome e idade.
# Implemente o método calcular_salario() como um método abstrato, que será diferente para cada subclasse.
# Crie uma subclasse Aluno que herde da classe Pessoa.
# Implemente o método exibir_info() para exibir informações específicas de um aluno, como nome, idade e número de matrícula.
# Implemente o método calcular_salario() para alunos, que, neste caso, não se aplica. Pode ser um método vazio.
# Crie uma subclasse Professor que herde da classe Pessoa.
# Implemente o método exibir_info() para exibir informações específicas de um professor, como nome, idade e disciplina lecionada.
# Implemente o método calcular_salario() para professores, calculando o salário com base na carga horária e valor por hora.
# Crie instâncias de Aluno e Professor.
# Chame o método exibir_info() para cada instância para verificar a exibição correta das informações.
# Chame o método calcular_salario() para o professor e exiba o valor calculado.
# Utilize a biblioteca sqlite3 para criar uma tabela chamada Pessoas com os campos tipo (para distinguir entre aluno e professor),
# nome, idade, info_extra (número de matrícula para aluno, disciplina para professor) e salario (nullable para aluno).
# Implemente métodos para adicionar instâncias de Aluno e Professor à tabela Pessoas, extraindo as informações dos métodos exibir_info()
# e calcular_salario() e outros métodos que trabalhem comandos SQL atráves de métodos / funções em Python.

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

    def calcular_salario(self):
        salario = self.carga_horaria * self.valor_por_hora
        print(f'Salario: {salario}')
    
    def exibir_info(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, Disciplina: {self.disciplina}")

# Criar instâncias de Aluno e Professor
aluno = Aluno("João", 20, "A12345")
professor = Professor("Maria", 35, "Matemática", 40, 50.0)

# aluno.exibir_info()
# professor.exibir_info()
# professor.calcular_salario()


# Crear tabla
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

# Ingresar datos en la tabla
cursor.execute('INSERT INTO Pessoas (tipo, nome, idade, info_extra, salario) VALUES (?, ?, ?, ?, ?)',
               ('aluno', aluno.nome, aluno.idade, aluno.matricula, None))
conn.commit()

# Ingresar datos en la tabla profesor
cursor.execute('INSERT INTO Pessoas (tipo, nome, idade, info_extra, salario) VALUES (?, ?, ?, ?, ?)',
               ('professor', professor.nome, professor.idade, professor.disciplina, professor.calcular_salario()))
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
            print(f"Aluno: Nome={nome}, Idade={idade}, Matrícula={info_extra}")

        elif tipo == 'professor':
            print(f"Professor: Nome={nome}, Idade={idade}, Disciplina={info_extra}, Salário={salario}")

    conn.close()

listar_pessoas()


