# Declaração de uma lista

minha_lista = [1, 2, 3, 4, 5, 7, 8, False]

# Exibindo a lista completa
print("Minha lista de exemplo: ", minha_lista)

# Exibindo elementos individuais da lista
# minha_lista[0] = "Python"
print("Minha lista de exemplo: ", minha_lista)

print("minha_lista[0]: ", minha_lista[0])
print("minha_lista[5]: ", minha_lista[5])

# Fatiando/slicing a lista
print("minha_lista[1:4]: ", minha_lista[1:4])
print("minha_lista[:6]: ", minha_lista[:6])
print("minha_lista[2:]: ", minha_lista[2:])

# Metodo append() - Adiciona um elemento ao final da lista
minha_lista.append(6)
print("Apos append(6): ", minha_lista)

# Metodo Index
indice = minha_lista.index(6)
print("Indice do elemento 6: ", indice)

# Metodo insert() - Adiciona um elemento em uma posição específica da lista
minha_lista.insert(2, 10)
print("Apos insert(2, 10): ", minha_lista)

# Metodo pop() - Remove um elemento da lista pelo índice
elemento_removido = minha_lista.pop(3)
print("Elemento removido: ", elemento_removido)
print("Apos pop(3): ", minha_lista)

# Metodo remove() - Remove um elemento da lista pelo valor
minha_lista.remove(False)
print("Apos remove(False): ", minha_lista)

# Metodo sort() - Ordena a lista
minha_lista.sort()
print("Apos sort(): ", minha_lista)