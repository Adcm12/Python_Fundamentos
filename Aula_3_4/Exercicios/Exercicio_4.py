# Crie uma classe chamada Funcionario com os atributos nome (private), salario (private) 
# e cargo (public). Crie métodos para definir o nome (set_nome(novo_nome)), obter o 
# nome (get_nome()), calcular aumento de salário (aumentar_salario(aumento)) e exibir informações 
# completas do funcionário (exibir_informacoes()). Crie um construtor e trabalhe 
# a manipulação da classe e dos dados via objetos.

class Funcionario():

    def __init__(self, nome, salario, cargo):

        self.__nome = nome
        self.__salario = salario
        self.cargo = cargo

    @property
    def get_nome(self):

        return self.__nome
    
    
    @get_nome.setter
    def set_nome(self, novo_nome):

        self.__nome = novo_nome
    

    def aumento_salario(self, aumento):

        if aumento > 0:

            self.__salario += aumento

    
    def exibir_informaciones(self):

        return f'\nNome: {self.__nome}  \nSalario: {self.__salario}  \nCargo: {self.cargo}'
    

if __name__ == "__main__":
    funcionario1 = Funcionario("David", 3000, "Operador")
    print(funcionario1.exibir_informaciones())

    print("\nAumentando o salário do funcionário...")
    funcionario1.aumento_salario(500)
    print(funcionario1.exibir_informaciones())

    print("\nMudando o nome do funcionário...")
    funcionario1.set_nome= "José"
    print(funcionario1.exibir_informaciones())