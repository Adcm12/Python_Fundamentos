#   Crie uma função que converta um valor em horas para minutos e segundos. Solicite ao usuário que 
#   digite o valor em horas e, em seguida, exiba as conversões para minutos e segundos.
# 	Fórmula para converter horas em minutos: Minutos = Horas * 60
# 	Fórmula para converter horas em segundos: Segundos = Horas * 3600

import os

def convertir_hora():

    hora=int(input("Digite la cantidad de horas: "))
    minuto=(hora*60)
    print (f'\n\033[034mA {hora} horas convertida a minutos: {minuto}\n \033[0m')

    segundo=(hora*3600)
    print (f'{hora} horas convertida a segundos: {segundo}\n')

if __name__ == '__main__':
    os.system('cls')
    convertir_hora()