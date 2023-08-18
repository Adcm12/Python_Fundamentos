import sqlite3
import os

class BancoDeDados():
    conexion = None

    @staticmethod
    def crear_conexion(nome_base):
        BancoDeDados.conexion = sqlite3.connect(nome_base)
        print('Conexión establecida!')
        return BancoDeDados.conexion

    @staticmethod
    def crear_tabela(nome_tabela_nova):
        cursor = BancoDeDados.conexion.cursor()
        
        sql = f'''
        CREATE TABLE IF NOT EXISTS {nome_tabela_nova} (
            id INTEGER PRIMARY KEY,
            nome TEXT (40),
            numero TEXT (15),
            email TEXT (40)); '''

        cursor.execute(sql)
        cursor.close()
        print(f'\n¡Tabla nueva creada con éxito!')

    @staticmethod
    def inserir_dados(nome_tabela, nome_usu, numero_usu, email_usu):
        cursor = BancoDeDados.conexion.cursor()

        sql = f""" 
                INSERT INTO {nome_tabela}
                (nome, numero, email)
                VALUES (?, ?, ?)
                """
        cursor.execute(sql, (nome_usu, numero_usu, email_usu))
        BancoDeDados.conexion.commit()
        cursor.close()
        print(f'\nDatos insertados en {nome_tabela} con éxito')

    @staticmethod
    def deleta_linha(id_linha, nome_tabela):
        cursor = BancoDeDados.conexion.cursor()
        
        sql = f''' 
        DELETE FROM {nome_tabela}
        WHERE id = ?;
        '''
        cursor.execute(sql, (id_linha,))
        num_filas_deletadas = cursor.rowcount
        BancoDeDados.conexion.commit()
        cursor.close()

        if num_filas_deletadas > 0:
            print('Línea eliminada con éxito')
        else:
            print('No se encontró ninguna línea con ese ID')

    @staticmethod
    def mostar_tabela(nome_tabela):
        cursor = BancoDeDados.conexion.cursor()
        cursor.execute(f'SELECT * FROM {nome_tabela}')
        rows = cursor.fetchall()

        if rows:
            for row in rows:
                print(row)
        else:
            print('\nLa tabla está vacía.')
        cursor.close()

    @staticmethod
    def actualiza_linha(nombre_tabla, id_linha, nome_novo, numero_novo, email_novo):
        cursor = BancoDeDados.conexion.cursor()
        sql = f'''
        UPDATE {nombre_tabla}
        SET nome = ?, numero = ?, email = ?
        WHERE id = ?;
        '''
        cursor.execute(sql, (nome_novo, numero_novo, email_novo, id_linha))
        BancoDeDados.conexion.commit()
        print('\n Datos actualizados con exito!')
        cursor.close()

    @staticmethod
    def database_manager():
        conn = BancoDeDados.crear_conexion('base_de_datos.db')

        menu = '''
                \n1 - Crear tabla
                \n2 - Insertar datos
                \n3 - Eliminar línea
                \n4 - Mostrar tabla
                \n5 - Actualizar línea
                \n6 - Salir: '''
        
        while True:
            try:
                operacion = int(input(menu))

                if operacion == 1:
                    nombre_tabla = input('Ingrese el nombre de la nueva tabla: ')
                    BancoDeDados.crear_tabela(nombre_tabla)

                elif operacion == 2:
                    tabla = input('\nIngrese el nombre de la tabla: ')
                    nombre_usu = input('\nIngrese el nombre: ')
                    numero_usu = input('Ingrese el número: ')
                    email_usu = input('Ingrese el correo electrónico: ')

                    if len(nombre_usu) >= 3 and 11 <= len(numero_usu) <= 13 and '@' in email_usu and '.com' in email_usu:
                        print(f'\nNombre {nombre_usu}, número {numero_usu}, y correo electrónico {email_usu} son datos válidos')
                        BancoDeDados.inserir_dados(tabla, nombre_usu, numero_usu, email_usu)
                    else:
                        print('\nPor favor ingrese datos válidos')

                elif operacion == 3:
                    nombre_tabla = input('Ingrese el nombre de la tabla: ')
                    id_eliminar = int(input('Ingrese el ID de la línea a eliminar: '))
                    BancoDeDados.deleta_linha(id_eliminar, nombre_tabla)

                elif operacion == 4:
                    nombre_tabla = input('Ingrese el nombre de la tabla: ')
                    BancoDeDados.mostar_tabela(nombre_tabla)

                elif operacion == 5:
                    nombre_tabla = input('Ingrese el nombre de la tabla: ')
                    id_actualizar = int(input('Ingrese el ID de la línea a actualizar: '))
                    nombre_nuevo = input('Ingrese el nuevo nombre: ')
                    numero_nuevo = input('Ingrese el nuevo número: ')
                    email_nuevo = input('Ingrese el nuevo correo electrónico: ')
                    BancoDeDados.actualiza_linha(nombre_tabla, id_actualizar, nombre_nuevo, numero_nuevo, email_nuevo)

                elif operacion == 6:
                    break

                else:
                    print('Ingrese una opción válida')

            except Exception as e:
                print(f'Ocurrió un error: {str(e)}')

        conn.close()
        print('Conexión cerrada')

if __name__ == '__main__':
    os.system('cls')
    BancoDeDados.database_manager()
