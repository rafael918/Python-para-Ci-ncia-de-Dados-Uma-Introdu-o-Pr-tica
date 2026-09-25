# 📋 Listas

Listas são estruturas de dados que permitem armazenar múltiplos valores em uma única variável. São muito importantes em Ciência de Dados para armazenar datasets.

Python oferece vários métodos para manipular listas. Vamos conhecer os principais.

## 📝 Exemplo Completo

> Carregando código em Python…

## 📋 Tabela de Métodos

| Método     | Sintaxe                   | Descrição                                | Exemplo                   |
| ---------- | ------------------------- | ---------------------------------------- | ------------------------- |
| `append()` | `lista.append(item)`      | Adiciona um item no final                | `lista.append("novo")`    |
| `insert()` | `lista.insert(pos, item)` | Insere um item em uma posição específica | `lista.insert(1, "meio")` |
| `remove()` | `lista.remove(item)`      | Remove a primeira ocorrência             | `lista.remove("item")`    |
| `pop()`    | `lista.pop(pos)`          | Remove e retorna um item pelo índice     | `lista.pop(0)`            |
| `count()`  | `lista.count(item)`       | Conta as ocorrências do item             | `lista.count("a")`        |
| `sort()`   | `lista.sort()`            | Ordena a lista                           | `lista.sort()`            |

## 🔍 Detalhes dos Métodos

### `append(item)`

Adiciona o item no **final** da lista.

É mais eficiente que `insert()` para adicionar elementos no final.

### `insert(posição, item)`

Insere o item na posição especificada.

Os elementos existentes são deslocados para a direita.

Os índices começam em 0.

### `remove(item)`

Remove a **primeira ocorrência** do item.

Gera erro se o item não existir.

Use `count()` antes para verificar a existência do item, quando necessário.

### `pop(posição)`

Remove e **retorna** o item da posição especificada.

Se nenhuma posição for especificada, remove o último elemento.

É útil quando você precisa utilizar o valor removido.

### `count(item)`

Conta quantas vezes o item aparece na lista.

Retorna `0` se o item não existir.

É útil para verificar duplicatas.

### `sort()`

Ordena a lista **permanentemente**.

Para strings, utiliza ordem alfabética.

Para números, utiliza ordem crescente.

Use `sorted(lista)` quando quiser criar uma nova lista ordenada sem alterar a lista original.

## 💡 Exemplos Práticos

> Carregando código em Python…

## 🏙️ Exercício Prático: Manipulação de Listas

# 🎯 Conclusão

## 📚 O Que Aprendemos

Nesta apostila, cobrimos os fundamentos essenciais do Python:

* **Tipos de Dados:** `string`, `int`, `float` e `bool`.
* **Função `print()`:** Diferentes formas de exibir informações.
* **Operadores:** Aritméticos e de comparação.
* **Listas:** Criação, acesso, modificação e métodos.
* **Exercícios Práticos:** Aplicação dos conceitos aprendidos.
