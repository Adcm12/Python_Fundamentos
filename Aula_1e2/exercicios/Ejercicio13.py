# Crie um jogo em que o computador escolhe um número aleatório entre 1 e 100, e o usuário deve adivinhar
# qual é esse número. O programa deve fornecer dicas se o número fornecido pelo usuário é maior ou menor 
# que o número escolhido pelo computador. Utilize um while loop para continuar o jogo até que o usuário acerte o número. Use
import os
import random

def juego_adivina_numero():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print("Juego de adivinar el numero!!!")
    print("Intenta adivinar el número secreto entre 1 e 100.")

    while True:
        try:
            intento = int(input("Digite primer intento: "))

            if intento < 1 or intento > 100:
                print("Digite um número entre 1 e 100.")
                continue

            tentativas += 1

            if intento == numero_secreto:
                print(f"Felicitaciones! usted acerto el número secreto {numero_secreto} en {tentativas} intentos.")
                break
            elif intento < numero_secreto:
                print("El número secreto es mayor. Intente de nuevo.")
            else:
                print("El número secreto es menor. Intenta de nuevo.")
        except ValueError:
            print("Digite un número intero válido.")

if __name__ == '__main__':
    os.system('cls')
    juego_adivina_numero()