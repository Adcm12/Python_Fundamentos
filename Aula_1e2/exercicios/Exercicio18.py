# Crie um programa que solicite ao usuário que insira a quantidade de notas do aluno a serem calculadas.
# Em seguida, peça para o usuário digitar as notas uma por uma. Armazene essas notas em uma lista.
# Calcule a média das notas utilizando um for loop para somar todos os elementos da lista e dividir pela quantidade de notas.
# Verifique se a média é maior ou igual a 6.0. Se a média for maior ou igual a 6.0, exiba a mensagem "Aluno Aprovado!".
# Caso contrário, exiba a mensagem "Aluno Reprovado!".


# Dicas:
# Utilize um for loop para solicitar as notas e armazená-las na lista.
# Use um acumulador para calcular a soma das notas e, ao final do loop, divida pela quantidade de notas para obter a média.
# Use uma estrutura condicional (if-else) para verificar se o aluno foi aprovado ou reprovado com base na média calculada.
# Certifique-se de converter os valores digitados pelo usuário para o tipo adequado (int ou float) ao armazená-los na lista.

def informa_cantidad_notas():
     
    while True:

        try:
            cantidad_nota = int(input('Informa la cantidad de notas: '))

            if cantidad_nota>0:
                return cantidad_nota
            else:
                raise ValueError('Informe numeros mayor a 0')

        except Exception as e:

            print(f'ocurrio un error: {str(e)}')
            print("Informe una cantidad valida")
lista_nota = []
def leer_notas(cantidad_nota):
    
    contador = 0

    while len(lista_nota) < cantidad_nota:

        try:
            nota = float(input(f'Informe a  {len(lista_nota)+ 1}° una nota: '))

            if nota >= 0 and nota <= 10:
                lista_nota.append(nota)


        except Exception as e:

            print(f'ocurrio un error: {str(e)}')
            print("Informe una cantidad valida")

    return lista_nota

def calcula_media(lista_nota):
    suma = 0 

    for nota in lista_nota:
        suma += nota

    return suma / len(lista_nota)
    

def verificar_media(media):
    if media >=6:
        print('Alumno aprovado')
    else:
        print('Alumno reprovado')

def scrip():
    cantidad_nota = informa_cantidad_notas()
    lista_notas = leer_notas(cantidad_nota)
    media = calcula_media(lista_nota)
    verificar_media(media)


if __name__ == '__main__':

    scrip()
