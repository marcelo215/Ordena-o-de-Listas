lista = [5, 2, 9, 1, 5, 6]

print (lista)
 
lista.sort()

print (lista)
 
lista.sort(reverse=True)

print(lista)
 
 
lista = [5, 2, 9, 1, 5, 6]

lista_ordenada = sorted(lista)

print(lista_ordenada)
 
lista = [5, 2, 9, 1, 5, 6]

lista_ordenada_inv = sorted(lista, reverse=True)

print(lista_ordenada_inv)
 
 
 
lista = [('maça', 3), ('banana', 4), ('toranja', 2), ('uva', 1)]

lista_ordenada =sorted(lista, key=lambda x: x[1])

print(lista_ordenada)
 