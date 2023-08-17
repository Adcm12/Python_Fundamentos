import sqlite3
import os
#Crear class para manipular el bd

    #Crear conexion

class BancoDeDados():

    criar_conexion = None

    @staticmethod # Permite accesar metodo sin crear objetos
    def crear_conexion(nome_base):
        BancoDeDados.conexion = sqlite3.connect(nome_base)
        print('Conexion establecida!')
        return BancoDeDados.conexion

    
    @staticmethod # Permite accesar metodo sin crear objetos
    def crear_tabela(nome_tabela_nova):
        cursor = BancoDeDados.conexion.cursor()
        
        sql = f'''
        CREATE TABLE if not exists {nome_tabela_nova} (\n
            id INTEGER PRIMARY KEY,\n
            nome TEXT (40),
            numero TEXT (15),
            email TEXT (40)); '''

        cursor.execute(sql)
        cursor.close()
        print(f'\nTabel nova creada con exito!')


    @staticmethod # Permite accesar metodo sin crear objetos
    def inserir_dados(nome_tabela, nome_usu, numero_usu, email_usu):
        cursor = BancoDeDados.conexion.cursor()

        sql = f""" 
                insert into {nome_tabela}\
                (nome, numero, email)\
                values ('{nome_usu}', '{numero_usu}', '{email_usu}' )
                """
        cursor.execute(sql)
        BancoDeDados.conexion.commit()
        cursor.close()
        print(f'\nDatos inseridos en {nome_tabela} con exito')

    @staticmethod # Permite accesar metodo sin crear objetos
    def deleta_linha(id_linha):
        pass

    @staticmethod # Permite accesar metodo sin crear objetos
    def mostar_tabela(nome_tabela):
        pass


    @staticmethod # Permite accesar metodo sin crear objetos
    def actualiza_linha(id_linha, nome_novo, numero_novo, email_novo):
        pass
    
    def database_manager():

        conn = BancoDeDados.crear_conexion('base_de_datos.db')

        menu = '''
                \n1 - Crear tabela
                \n2 - Inserir datos
                \n3 - Deletar linha
                \n4 - Mostrar tabela
                \n5 - Actualizar linha
                \n6 - Salir: '''
        while True :
            try:
                os.system('cls')
                operacio = int(input(menu))

                if operacio == 1:

                    nome_tabela = input('Informe el nombre de la tabela nueva: ')

                    BancoDeDados.crear_tabela(nome_tabela)

                elif operacio == 2:

                    tabela = input('Informe el nombre de la tabela: ')
                    nome_usu = input('Informe el nombre: ')
                    numero_usu = input('Informe el numero: ')
                    email_usu = input('Informe el email: ')

                    BancoDeDados.inserir_dados(nome_tabela= tabela, nome_usu=nome_usu, numero_usu=numero_usu, email_usu= email_usu)
                    

                elif operacio == 3:
                    pass                    

                elif operacio == 4:
                    pass

                elif operacio == 5:
                    pass

                elif operacio == 6:

                    quit()
                
                else: 

                    print('Informe una opcion valida')

            except Exception as e:
                print(f'Ocurrio un error: {str(e)}')
    
        conn.close()

#Crear funcion main, que sera la interface del usuario

if __name__ == '__main__':

    os.system('cls')
    BancoDeDados.database_manager()

