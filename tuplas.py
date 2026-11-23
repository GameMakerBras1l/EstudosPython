# Criando uma tupla de exemplo
minha_tupla = (1, 2, 2, 3, 4)

print("Minha tupla: ", minha_tupla)

print("minha_tupla[0]: ", minha_tupla[0])
print("minha_tupla[2]: ", minha_tupla[2])

# O -1 serve para acessar o último elemento da tupla ou lista
print("minha_tupla[-1]: ", minha_tupla[-1])

# Metodo count() - Conta quantas vezes um elemento aparece na tupla
contagem = minha_tupla.count(2)
print("O número 2 aparece ", contagem, " vezes na tupla.")

indice = minha_tupla.index(3)
print("O índice do elemento 3 é: ", indice)