#Realizando importaciones de bibliotecas
#Por padrao, elas seran importadas en el comienzo
#do archivos/programas.py
import time
import os

# 3Sirve para enviar comando al terminal entre otras funciones

os.system('cls')

# os.system('dir')

# # taskill serve para parar el archivo responsable 
# # para rodar una aplicacion el sistema


# os.system('taskkill /f /im brave.exe') 

numero_entero1: int = 5
numero_entero2 = 89
numero_entero3 = 500

nome1: str = "\nAdrian"
nome: str = "\nCastillo"
texto = '\nJAJAJA'

print(f'Datos de las variables de tipo int, \n', numero_entero1,'\n', numero_entero2, '\n', numero_entero3)
print(f'\nDatos de las variables de tipo str {nome}, {nome1}, {texto}')

salario: float = 15.56

print(f'\nDatos de las variables de tipo float\n{salario}')

verdade: bool = True

print(f'\nDatos de las variables de tipo bool\n {verdade}')

lista: list = [
    numero_entero1,
    numero_entero2,
    salario,
    verdade
]

time.sleep(3)

os.system('cls')

print(f'\nDatos de la lista: {lista[1]}')

for item in lista:
    print('\n', item)

