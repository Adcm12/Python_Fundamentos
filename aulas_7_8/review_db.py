import os 
import sqlite3
from datetime import datetime

class Logica_Banco():


    def crear_conexion(self, nome_base):

        try:

            conn = sqlite3.connect(nome_base)
            print('Conexion establecida')

            return conn

        except Exception as e:
            print(f'Erro: {str(e)}')

    def crear_tabela(self, nome_tabela):

        try:

            conn = self.crear_conexion('base.db')
            cursor = conn.cursor()

            sql_string = f"""
            Create table if not exists {nome_tabela} (
            id integer primary key,
            funcion text(40),
            registro text(40),
            data_hora_registrado text(20)
            )            
            """
            cursor.execute(sql_string)
            cursor.close()
            conn.commit()
            conn.close()
            print(f'Tabela {nome_tabela}, creada con exito')

        except Exception as e:
            print(f'Erro: {str(e)}')

    def retorna_ultimo_registtro_inserido(self):

        try:

            conn = sqlite3.connect("base.db")

            cursor = conn.cursor()

            cursor.execute("SELECT * FROM Registro ORDER BY id DESC LIMIT 1")

            resultados = cursor.fetchone()

            conn.close()

            id, funciones, registro, data = resultados

            print(f'''\033[034mId:\033[0m {id} 
                  \033[034m\nFunciones:\033[0m {funciones} 
                  \033[034m\nRegistro:\033[0m {registro} 
                  \033[034m\nData:\033[0m {data}''')

        except Exception as e:
            print(f'Erro: {str(e)}')

    def insere_registro(self, nome_tabela, funciones, registro):

        try:

            conn = self.crear_conexion('base.db')
            cursor = conn.cursor()

            sql_string = f"""
            insert into {nome_tabela} (funcion, registro, data_hora_registrado)
            values ('{funciones}', '{registro}', '{datetime.now().strftime('%d/%m/%Y - %H:%M:%S')}')           
            """
            cursor.execute(sql_string)
            cursor.close()
            conn.commit()
            conn.close()
            print(f'Datos inseridos con exito')
        except Exception as e:
            print(f'Erro: {str(e)}')
            
    def deletar_registro(self, id_linha):

        try:

            conn = sqlite3.connect("base.db")
            cursor = conn.cursor()

            cursor.execute(f"DELETE FROM Registro WHERE id = {id_linha}")
            conn.commit()
            conn.close()
            print('Datos eliminados con exito')

        except Exception as e:
            print(f'Erro: {str(e)}')

    def retornar_cantidad_registro(self, nome_tabela):
        try:
            
            conn = sqlite3.connect("base.db")

            cursor = conn.cursor()

            cursor.execute(f"SELECT COUNT(*) FROM {nome_tabela}")

            lineas = cursor.fetchone()[0]

            conn.close()

            print(f'Cantidad de registros en la tabla: {lineas}')

        except Exception as e:
            print(f'Erro: {str(e)}')

if __name__ == '__main__':

    os.system('cls')

    objeto_banco= Logica_Banco()
    # objeto_banco.crear_conexion('base.db')
    objeto_banco.retornar_cantidad_registro('Registro')

   



    

    