# Crie uma função que solicite ao usuário que insira seu endereço completo 
# (incluindo rua, número, bairro, cidade e CEP) e armazene as informações em variáveis separadas. 
# Depois mostre essas informações usando concatenação com uma mensagem.

import os

def endereço():

    ciudad = input('Informe su ciudad: ')
    bairro = input('Informe su bairro: ')
    rua = input('Informe su rua: ')
    numero = int(input('Informe el numero: '))
    cep = input('Informe su CEP: ')

    print(f'\nSu endereço es: Ciudad: {ciudad}, Barrio: {bairro}, Rua: {rua}, Numero: {numero}, CEP: {cep}')

if __name__ == '__main__':
    os.system('cls')
    endereço()
