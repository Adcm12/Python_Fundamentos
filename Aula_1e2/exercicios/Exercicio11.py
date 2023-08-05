# Dado um número inteiro positivo N, crie uma função que exiba todos os números pares de 0 
# até N (inclusive). Utilize um for loop para iterar pelos números e um operador de módulo (%) 
# para verificar se o número é par.


def numeros_pares():

    numero = int(input("Digite um número inteiro positivo: "))

    for i in range(numero+1):
        if i % 2 == 0:
            print(i)



numeros_pares()
