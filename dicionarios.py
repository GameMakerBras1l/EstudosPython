# Criando um dicionario de exemplo
pessoa = {"nome": "Marcel", "idade": 30, "cidade": "Recife"}

print("Meu dicionário:", pessoa)

# Acessando valores por chave
print("Nome: ", pessoa["nome"])
print("Idade: ", pessoa["idade"])
print("Cidade: ", pessoa["cidade"])
pessoa["Sobrenome"] = "Rolland"
print("Sobrenome: ", pessoa["Sobrenome"])

print("Dicionário atualizado: ", pessoa)

pessoa["idade"] = 31
print("Idade atualizada: ", pessoa["idade"])

# Removendo um item do dicionário
del pessoa["Sobrenome"]
print("Dicionário após remover o sobrenome:", pessoa)

# Metodos úteis para dicionários
chaves = list(pessoa.keys())
print("Chaves do dicionário: ", chaves)
print("Primeira chave: ", chaves[0])

# Metodos Values
valores = list(pessoa.values())
print("Valores do dicionário: ", valores)
print("Primeiro valor: ", valores[0])

# Metodos Items
itens = list(pessoa.items())
print("Itens do dicionário: ", itens)
print("Primeiro item: %s = %s", itens[0][0], itens[0][1])  # Acessando o valor do primeiro item