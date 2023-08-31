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
            registro text(50),6
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
            ...

        except Exception as e:
            print(f'Erro: {str(e)}')

    def insere_registro(self, nome_tabela, registro):

        try:

            conn = self.crear_conexion('base.db')
            cursor = conn.cursor()

            sql_string = f"""
            insert into {nome_tabela} (registro, data_hora_registrado)
            values ('{registro}', '{datetime.now().strftime('%d/%m/%Y - %H:%M:%S')}')           
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

            ...
        except Exception as e:
            print(f'Erro: {str(e)}')


    def retornar_cantidad_registro(self, nome_tabela):
        try:
            ...

        except Exception as e:
            print(f'Erro: {str(e)}')

if __name__ == '__main__':

    os.system('cls')

    objeto_banco= Logica_Banco()
    objeto_banco.crear_tabela('Registro')

    objeto_banco.insere_registro('Registro', 'Testando')
   



    

    