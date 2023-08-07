	# Crie uma função que remova as duplicatas de uma lista de números. Por exemplo, se a lista for [1, 2, 2, 3, 4, 4, 5],
	# o programa deve retornar a lista sem duplicatas: [1, 2, 3, 4, 5]. Utilize listas e um for loop para percorrer a lista 
	# original e uma nova lista para armazenar os elementos únicos.

def eliminar_duplicados(lista):
    lista_sin_duplicados = []
    for elemento in lista:
        if elemento not in lista_sin_duplicados:
            lista_sin_duplicados.append(elemento)
    return lista_sin_duplicados

mi_lista = [1, 2, 2, 3, 4, 4, 5]
lista_sin_duplicados = eliminar_duplicados(mi_lista)
print("Lista original:", mi_lista)
print("Lista sin duplicados:", lista_sin_duplicados)