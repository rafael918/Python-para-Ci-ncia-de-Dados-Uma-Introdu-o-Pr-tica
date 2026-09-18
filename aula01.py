# Python para Ciência de Dados: Uma Introdução Prática

## 🎯 Introdução

Esta apostila foi desenvolvida com base nas aulas práticas de Fundamentos de Python para Ciência de Dados. Aqui você encontrará explicações detalhadas dos conceitos abordados, exemplos práticos e exercícios para consolidar seu aprendizado.

---

## 🔢 Tipos de Dados

Em Python, existem vários tipos de dados fundamentais. Vamos conhecer os principais.

### String (`str`)

Representa texto. Sempre deve estar entre aspas simples ou duplas.

```python
nome = "William"  # Aspas duplas

nome = 'William'  # Aspas simples (mesmo resultado)
```

**Características:**

* Pode conter letras, números, símbolos e espaços.
* É imutável (não pode ser alterada após criação).
* Pode ser concatenada com outras strings.

### Inteiro (`int`)

Representa números inteiros (sem casas decimais).

```python
idade = 30
```

**Exemplos de números inteiros:**

* Números positivos: `1, 50, 1000`
* Números negativos: `-1, -50, -1000`
* Zero: `0`

### Float (`float`)

Representa números com casas decimais.

```python
altura = 1.74
peso = 75.5
```

**Exemplos de números `float`:**

* Decimais: `3.14, 2.5, 0.1`

### Booleano (`bool`)

Representa valores lógicos: `True` ou `False`.

```python
estudante = False
trabalha = True
```

**Características:**

* Sempre com a primeira letra maiúscula.
* Usado em estruturas condicionais e loops.
* Resultado de operações de comparação.

### 💡 Dica Prática

Você pode verificar o tipo de uma variável usando a função `type()`:

```python
print(type(nome))       # <class 'str'>
print(type(idade))      # <class 'int'>
print(type(altura))     # <class 'float'>
print(type(estudante))  # <class 'bool'>
```

---

## 🖨️ Função `print()`

A função `print()` é fundamental para exibir informações na tela. Vamos ver diferentes formas de usá-la.

### Formas Básicas

```python
nome = "William"

# 1. Print simples
print(nome)

# Saída: William

# 2. Print com texto e variável separados por vírgula
print("Meu nome é", nome)

# Saída: Meu nome é William

# 3. Print com f-string (recomendado)
print(f"Meu nome é {nome}")

# Saída: Meu nome é William

# 4. Print com separador personalizado
print("Meu nome é", nome, sep=":")

# Saída: Meu nome é:William
```

### 📝 Explicação das Diferentes Formas

1. **Print simples:** Exibe apenas o valor da variável.
2. **Vírgula:** Adiciona um espaço automaticamente entre os elementos.
3. **f-string:** Permite formatação mais avançada e é mais legível.
4. **Parâmetro `sep`:** Define o separador entre os elementos (o padrão é espaço).

### 🎯 Quando Usar Cada Forma

* **f-string:** Para formatação complexa e quando você quer controlar exatamente como o texto aparece.
* **Vírgula:** Para casos simples onde você quer espaçamento automático.
* **`sep`:** Quando você quer um separador específico (dois pontos, hífen, etc.).

---

## ➕➖ Operadores Aritméticos

Os operadores aritméticos permitem realizar cálculos matemáticos em Python.

```python
# Soma
print(5 + 5)    # Resultado: 10

# Subtração
print(2 - 2)    # Resultado: 0

# Multiplicação
print(2 * 2)    # Resultado: 4

# Divisão
print(2 / 5)    # Resultado: 0.4

# Potenciação
print(2 ** 2)   # Resultado: 4 (2 elevado à 2ª potência)

# Resto da divisão (módulo)
print(5 % 2)    # Resultado: 1 (resto de 5 ÷ 2)

# Divisão inteira
print(5 // 2)   # Resultado: 2 (parte inteira de 5 ÷ 2)
```

### 📊 Tabela de Operadores

| Operador        | Símbolo | Exemplo  | Resultado | Descrição                      |
| --------------- | ------- | -------- | --------- | ------------------------------ |
| Soma            | `+`     | `3 + 2`  | `5`       | Adiciona dois números          |
| Subtração       | `-`     | `3 - 2`  | `1`       | Subtrai o segundo do primeiro  |
| Multiplicação   | `*`     | `3 * 2`  | `6`       | Multiplica dois números        |
| Divisão         | `/`     | `3 / 2`  | `1.5`     | Divide o primeiro pelo segundo |
| Potenciação     | `**`    | `3 ** 2` | `9`       | Primeiro elevado ao segundo    |
| Módulo          | `%`     | `5 % 2`  | `1`       | Resto da divisão               |
| Divisão inteira | `//`    | `5 // 2` | `2`       | Parte inteira da divisão       |

### 💡 Exemplos Práticos

```python
# Calculando a média de notas
nota1 = 8.5
nota2 = 7.0
nota3 = 9.0

media = (nota1 + nota2 + nota3) / 3

print(f"A média é: {media:.2f}")

# Verificando se um número é par ou ímpar
numero = 7

if numero % 2 == 0:
    print(f"{numero} é par")
else:
    print(f"{numero} é ímpar")
```

---

## ⚖️ Operadores de Comparação

Os operadores de comparação retornam valores booleanos (`True` ou `False`) e são essenciais para tomada de decisões no código.

```python
idade = 30
nome = "William"

# Maior que
print(1 > 2)       # False
print(idade > 25)  # True

# Igual a
print(idade == 30)      # True
print(nome == "Vitor")  # False

# Menor que
print(1 < 2)       # True
print(idade < 25)  # False

# Diferente de
print(nome != "Vitor")  # True
print(idade != 30)      # False

# Menor ou igual a
print(1 <= 1)      # True
print(idade <= 25) # False

# Maior ou igual a
print(1 >= 1)      # True
print(idade >= 25) # True
```

### 📋 Tabela de Operadores de Comparação

| Operador       | Símbolo | Exemplo  | Resultado | Descrição                               |
| -------------- | ------- | -------- | --------- | --------------------------------------- |
| Igual          | `==`    | `5 == 5` | `True`    | Verifica se são iguais                  |
| Diferente      | `!=`    | `5 != 3` | `True`    | Verifica se são diferentes              |
| Maior que      | `>`     | `5 > 3`  | `True`    | Verifica se o primeiro é maior          |
| Menor que      | `<`     | `3 < 5`  | `True`    | Verifica se o primeiro é menor          |
| Maior ou igual | `>=`    | `5 >= 5` | `True`    | Verifica se o primeiro é maior ou igual |
| Menor ou igual | `<=`    | `3 <= 5` | `True`    | Verifica se o primeiro é menor ou igual |

### ⚠️ Importante

* Use `==` para comparação, e não `=`.
* `=` é usado para atribuição.
* `==` é usado para comparação.
* Operadores de comparação podem ser usados com diferentes tipos de dados, desde que a operação seja válida.

### 💡 Exemplos Práticos

```python
# Verificando aprovação em um exame
nota = 7.5

if nota >= 7.0:
    print("Aprovado!")
else:
    print("Reprovado")

# Verificando se uma string não está vazia
nome = "João"

if nome != "":
    print(f"Olá, {nome}!")
else:
    print("Nome não informado")
```

---

## 🌡️ Exercício Prático: Conversão de Temperatura

### 📝 Enunciado

Escreva um algoritmo que converta Celsius para Fahrenheit.

Defina uma variável para Celsius, coloque um valor nela e faça a conversão.

Faça dois `prints`, usando duas formas diferentes, dizendo:

> "x graus C é igual a x graus F"

### ✅ Solução

```python
# Definindo a temperatura em Celsius
celsius = 17

# Fórmula de conversão: F = (C × 1.8) + 32
faren = (celsius * 1.8) + 32

# Primeira forma: usando f-string
print(f"{celsius} graus C é igual a {faren} graus F")

# Segunda forma: usando vírgulas
print(celsius, "graus C é igual a", faren, "graus F")
```

### 📊 Saída do Programa

```text
17 graus C é igual a 62.6 graus F
17 graus C é igual a 62.6 graus F
```

### 🔍 Explicação da Fórmula

A fórmula `F = (C × 1.8) + 32` é a conversão padrão de Celsius para Fahrenheit:

* Multiplicamos por `1.8`, que é equivalente a `9/5`.
* Somamos `32` para ajustar o ponto de congelamento.

---

## 📋 Listas

Listas são estruturas de dados que permitem armazenar múltiplos valores em uma única variável. São muito importantes em Ciência de Dados para armazenar datasets.

### 🎯 Conceitos Básicos

```python
# Criando listas
alunos = ["Priscila", "Douglas", "Glaciane", "Thomas"]
idades = [18, 25, 23, 12]

# Acessando elementos (índices começam em 0)
print("O primeiro aluno é", alunos[0])  # Priscila
print("A primeira idade é", idades[0])  # 18

# Modificando elementos
idades[0] = 19

print(idades)  # [19, 25, 23, 12]

# Operações com elementos
print(idades[0] + idades[1])  # 19 + 25 = 44
```

### 📊 Características das Listas

1. **Ordenadas:** Os elementos têm posições.
2. **Mutáveis:** Podem ser alteradas após a criação.
3. **Permitem duplicatas:** O mesmo elemento pode aparecer várias vezes.
4. **Índices começam em 0:** O primeiro elemento está no índice `0`.

### 🎯 Índices Positivos e Negativos

```python
lista = ["A", "B", "C", "D", "E"]

# Índices positivos (da esquerda para direita)
print(lista[0])  # A
print(lista[1])  # B
print(lista[2])  # C

# Índices negativos (da direita para esquerda)
print(lista[-1])  # E (último elemento)
print(lista[-2])  # D (penúltimo elemento)
print(lista[-3])  # C
```

### 💡 Exemplos Práticos

```python
# Lista de preços de produtos
precos = [10.50, 25.00, 8.75, 15.30]

produtos = ["Arroz", "Feijão", "Macarrão", "Óleo"]
```

---

## 🔧 Métodos de Listas

Python oferece vários métodos para manipular listas. Vamos conhecer os principais.

### 📝 Exemplo Completo

```python
listaDeCompras = ["mamao", "melancia", "melancia", "feijao"]

print("Lista original:", listaDeCompras)

# Inserindo elemento em posição específica
listaDeCompras.insert(1, "cebola")

print("Após inserir cebola na posição 1:", listaDeCompras)

# Adicionando elemento no final
listaDeCompras.append("arroz")

print("Após adicionar arroz:", listaDeCompras)

# Contando ocorrências
print("Quantas melancias:", listaDeCompras.count("melancia"))

# Ordenando a lista
listaDeCompras.sort()

print("Lista ordenada:", listaDeCompras)

# Removendo primeira ocorrência
listaDeCompras.remove("melancia")

print("Após remover uma melancia:", listaDeCompras)

# Removendo elemento por posição
listaDeCompras.pop(1)

print("Após remover elemento da posição 1:", listaDeCompras)
```

### 📋 Tabela de Métodos

| Método     | Sintaxe                   | Descrição                         | Exemplo                   |
| ---------- | ------------------------- | --------------------------------- | ------------------------- |
| `append()` | `lista.append(item)`      | Adiciona item no final            | `lista.append("novo")`    |
| `insert()` | `lista.insert(pos, item)` | Insere item em posição específica | `lista.insert(1, "meio")` |
| `remove()` | `lista.remove(item)`      | Remove a primeira ocorrência      | `lista.remove("item")`    |
| `pop()`    | `lista.pop(pos)`          | Remove e retorna item por índice  | `lista.pop(0)`            |
| `count()`  | `lista.count(item)`       | Conta ocorrências do item         | `lista.count("a")`        |
| `sort()`   | `lista.sort()`            | Ordena a lista                    | `lista.sort()`            |

### 🔍 Detalhes dos Métodos

#### `append(item)`

* Adiciona o item no **final** da lista.
* É mais eficiente que `insert()` para adicionar no final.

#### `insert(posição, item)`

* Insere o item na posição especificada.
* Os elementos existentes são deslocados para a direita.
* Os índices começam em `0`.

#### `remove(item)`

* Remove a **primeira ocorrência** do item.
* Gera erro se o item não existir.
* Use `count()` antes para verificar a existência, quando necessário.

#### `pop(posição)`

* Remove e **retorna** o item da posição especificada.
* Se a posição não for especificada, remove o último elemento.
* É útil quando você precisa utilizar o valor removido.

#### `count(item)`

* Conta quantas vezes o item aparece na lista.
* Retorna `0` se o item não existir.
* É útil para verificar duplicatas.

#### `sort()`

* Ordena a lista **permanentemente**.
* Para strings: ordem alfabética.
* Para números: ordem crescente.
* Use `sorted(lista)` para criar uma nova lista ordenada.

### 💡 Exemplos Práticos

```python
# Gerenciando lista de tarefas
tarefas = [
    "Estudar Python",
    "Fazer exercícios",
    "Revisar notas"
]

# Adicionando nova tarefa
tarefas.append("Preparar apresentação")

print("Tarefas:", tarefas)

# Inserindo tarefa urgente no início
tarefas.insert(0, "Reunião urgente")

print("Com tarefa urgente:", tarefas)

# Removendo tarefa concluída
tarefas.remove("Estudar Python")

print("Após concluir uma tarefa:", tarefas)
```

---

## 🏙️ Exercício Prático: Manipulação de Listas

### 📝 Enunciado

Escreva um algoritmo com uma lista de 3 cidades.

O algoritmo deve:

1. Mostrar a cidade na posição 2.
2. Alterar a cidade na posição 0.
3. Inserir uma cidade na posição 1.
4. Inserir uma cidade na última posição.

### ✅ Solução

```python
# Criando lista de 3 cidades
cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte"]

# Mostrando cidade na posição 2 (índice 2)
print("Cidade na posição 2:", cidades[2])

# Alterando cidade na posição 0 (índice 0)
cidades[0] = "Salvador"

print("Após alterar posição 0:", cidades)

# Inserindo cidade na posição 1 (índice 1)
cidades.insert(1, "Brasília")

print("Após inserir na posição 1:", cidades)

# Inserindo cidade na última posição
cidades.append("Fortaleza")

print("Após adicionar na última posição:", cidades)
```

### 📊 Saída Esperada

```text
Cidade na posição 2: Belo Horizonte
Após alterar posição 0: ['Salvador', 'Rio de Janeiro', 'Belo Horizonte']
Após inserir na posição 1: ['Salvador', 'Brasília', 'Rio de Janeiro', 'Belo Horizonte']
Após adicionar na última posição: ['Salvador', 'Brasília', 'Rio de Janeiro', 'Belo Horizonte', 'Fortaleza']
```

### 🔍 Explicação Passo a Passo

1. **Criação da lista:** Iniciamos com 3 cidades.
2. **Acesso por índice:** `cidades[2]` acessa o terceiro elemento (`Belo Horizonte`).
3. **Modificação:** `cidades[0] = "Salvador"` substitui São Paulo por Salvador.
4. **Inserção no meio:** `insert(1, "Brasília")` adiciona Brasília na segunda posição.
5. **Inserção no final:** `append("Fortaleza")` adiciona Fortaleza ao final.

### 🎯 Variações do Exercício

```python
# Versão mais interativa
cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte"]

print("Lista original:", cidades)

print("Primeira cidade:", cidades[0])

print("Última cidade:", cidades[-1])

# Ordenando alfabeticamente
cidades_ordenadas = sorted(cidades)

print("Cidades em ordem alfabética:", cidades_ordenadas)
```

---

## 🎯 Conclusão

### 📚 O Que Aprendemos

Nesta apostila, cobrimos os fundamentos essenciais do Python:

1. **Tipos de Dados:** String, `int`, `float`, `bool`.
2. **Função `print()`:** Diferentes formas de exibir informações.
3. **Operadores:** Aritméticos e de comparação.
4. **Listas:** Criação, acesso, modificação e métodos.
5. **Exercícios Práticos:** Aplicação dos conceitos aprendidos.

### 📖 Recursos Adicionais

* **Documentação Python:** https://docs.python.org/
* **Python.org Tutorial:** https://docs.python.org/3/tutorial/
* **Real Python:** https://realpython.com/
* **Python Brasil:** https://python.org.br/

---

**Desenvolvido com base nas aulas práticas de Fundamentos de Python para Ciência de Dados.**

*Esta apostila serve como material de referência e estudo para aprofundar os conhecimentos apresentados em sala de aula.*
