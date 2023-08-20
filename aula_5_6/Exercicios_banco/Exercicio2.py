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
import os

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

    tipo = input("\nDigite 'Alumno' para adicionar um alumno, ou 'Profesor' para adicionar um profesor: ").capitalize()
    nome = input("\nDigite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))


    if tipo == 'Alumno':

        matricula = input("Digite o número de matrícula do aluno: ")
        aluno = Aluno(nome, idade, matricula)
        salario = None
        info_extra = matricula

    elif tipo == 'Profesor':

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
    os.system('cls')
    print(f'{tipo} adiccionado con sucesso!')

def mostrar_personas():

    conn = sqlite3.connect("pessoas.db")
    cursor = conn.cursor()

    tipo = input('Digite el tipo de persona, "Alumno" o "Profesor": ').capitalize()
    os.system('cls')

    if tipo == 'Alumno':

        cursor.execute("SELECT nome, idade, info_extra FROM Pessoas WHERE tipo = 'Alumno'")
        alunos = cursor.fetchall()

        for aluno in alunos:

            nome, idade, info_extra = aluno

            print(f"\nAlumno:\nNombre: {nome}, Edad: {idade}, Matrícula: {info_extra}")

    elif tipo == 'Profesor':

        cursor.execute("SELECT nome, idade, info_extra, salario FROM Pessoas WHERE tipo = 'Profesor'")        
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

if __name__ == '__main__':

    try: 
        while True:

            crear_tabela()
            conn = sqlite3.connect("pessoas.db")
            cursor = conn.cursor()

            opcion = int(input('\nDigite uma opcao: \n 1) Adicionar pessoas \n 2) Mostrar pessoas \n 3) Salir:  '))

            if opcion == 1 :

                adicionar_pessoa()

            elif opcion == 2:

                mostrar_personas()

            elif opcion == 3:

                break
            else: 
                print('Opcao invalida!\n')

        

    except Exception as e:
        print(f'Ocurrió un error: {str(e)}')

    conn.close()