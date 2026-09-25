#Lista de Exercícios — Listas em Python
#Resolva os exercícios abaixo utilizando os recursos de listas trabalhados em aula.


# 1. Lista de convidados

# Cria uma lista vazia
convidados = []

# append() - adiciona os nomes no final da lista
convidados.append("Ana")
convidados.append("Carlos")
convidados.append("Bruno")
convidados.append("Marina")

# insert() - coloca Pedro na segunda posição da lista
convidados.insert(1, "Pedro")

# Exibe a lista
print(convidados)

# sorts() - organiza os nomes em ordem alfabética
convidados.sort()

# Exibe a lista organizada
print(convidados)

#-------------------------------------------

# 2. Invertendo uma lista


# Cria a lista com os números
numeros = [10, 20, 30, 40, 50]

# Cria uma lista vazia
invertida = []

# pop() - retira o último elemento e salva na variável removido
removido = numeros.pop()
invertida.append(removido)

# Retira o próximo último elemento
removido = numeros.pop()
invertida.append(removido)

# Retira o próximo último elemento
removido = numeros.pop()
invertida.append(removido)

# Retira o próximo último elemento
removido = numeros.pop()
invertida.append(removido)

# Retira o último elemento
removido = numeros.pop()
invertida.append(removido)

# Exibe as duas listas
print("Lista original:", numeros)
print("Lista invertida:", invertida)


#-------------------------------------------------------------------

# 3. Fila de atendimento

# Cria a fila de atendimento
fila = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo"]

# Cria uma lista vazia para os atendidos
atendidos = []

# pop(0) - retira a primeira pessoa da fila
pessoa = fila.pop(0)
atendidos.append(pessoa)

# Retira a próxima pessoa da fila
pessoa = fila.pop(0)
atendidos.append(pessoa)

# Retira a próxima pessoa da fila
pessoa = fila.pop(0)
atendidos.append(pessoa)

# Exibe o resultado
print("Fila restante:", fila)
print("Pessoas atendidas:", atendidos)

#--------------------------------------------------------


# 4 Controle de produtos

produtos = ["Arroz", "Feijão", "Leite", "Café", "Leite", "Açúcar"]

# count() - conta quantas vezes "Leite" aparece
quantidade = produtos.count("Leite")
print("Leite aparece", quantidade, "vezes")

# remove() - remove apenas uma ocorrência da palavra "Leite"
produtos.remove("Leite")

# append() - adiciona "Macarrão" no final da lista
produtos.append("Macarrão")

# insert() - adiciona "Farinha" no início da lista
produtos.insert(0, "Farinha")

# sorts() - ordena a lista em ordem alfabética
produtos.sort()

# Exibe a lista final
print("Lista final:", produtos)