# Ordena-o-de-Listas
Este projeto demonstra diferentes formas de ordenar listas em Python, utilizando os métodos sort() e sorted(). Inclui exemplos de ordenação crescente, decrescente, criação de novas listas ordenadas e também a ordenação de listas de tuplas com o uso de lambda.
# 🐍 Python - Ordenação de Listas

Este repositório contém exemplos em **Python** que demonstram diferentes formas de **ordenar listas** utilizando os métodos `sort()` e `sorted()`.  

## 📌 Funcionalidades
- Ordenação crescente e decrescente de listas numéricas.
- Uso do `sort()` para modificar a lista original.
- Uso do `sorted()` para criar uma nova lista ordenada sem alterar a original.
- Ordenação de listas de tuplas utilizando `key` e `lambda`.

## 📝 Código de Exemplo

```python
lista = [5, 2, 9, 1, 5, 6] 

print(lista)

# Ordenação crescente
lista.sort()
print(lista)

# Ordenação decrescente
lista.sort(reverse=True)
print(lista)

# Usando sorted() - cria nova lista ordenada
lista = [5, 2, 9, 1, 5, 6]
lista_ordenada = sorted(lista)
print(lista_ordenada)

# Usando sorted() em ordem decrescente
lista = [5, 2, 9, 1, 5, 6]
lista_ordenada_inv = sorted(lista, reverse=True)
print(lista_ordenada_inv)

# Ordenando lista de tuplas pelo segundo elemento
lista = [('maça', 3), ('banana', 4), ('toranja', 2), ('uva', 1)]
lista_ordenada = sorted(lista, key=lambda x: x[1])
print(lista_ordenada)
