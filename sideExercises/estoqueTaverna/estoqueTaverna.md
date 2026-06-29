# Exercício 1: O Estoque da Taverna

Objetivo: Praticar a inserção, atualização e leitura de valores em um dicionário.

Imagine que você está criando um jogo de RPG e precisa gerenciar o estoque de uma taverna. Você receberá um dicionário inicial com os itens e as quantidades.

- Suas tarefas:

  -  Escreva uma função adicionar_item(item, quantidade) que adiciona um novo item ao dicionário ou, se ele já existir, soma a quantidade nova à quantidade existente.

   - Escreva uma função calcular_valor_total(precos) que recebe um segundo dicionário (com os preços de cada item) e calcula qual é o valor total em moedas de todo o estoque da taverna.

## Código base para começar:

```
estoque = {
    "pocao_vida": 10,
    "pao": 25,
    "queijo": 8
}

tabela_precos = {
    "pocao_vida": 50.0,
    "pao": 2.5,
    "queijo": 5.0,
    "espada_ferro": 150.0
}

# 1. Crie a função adicionar_item(item, quantidade) aqui

# 2. Crie a função calcular_valor_total(precos) aqui
``