# Exercício Extra: O Gerenciador de Notas Acadêmicas

Imagine que você é um professor e tem uma lista de dicionários contendo o nome do aluno, a disciplina e a nota que ele tirou. Você precisa organizar um "Boletim" agrupando todas as notas por aluno.

## O Desafio:
Crie uma função chamada agrupar_notas_por_aluno(lista_notas) que recebe uma lista de dicionários e retorna um dicionário onde a chave é o nome do aluno e o valor é uma lista de todas as notas que ele tirou em diferentes disciplinas.

Dados de entrada:
```
lista_notas = [
    {"aluno": "Alice", "disciplina": "Matemática", "nota": 9.5},
    {"aluno": "Bob", "disciplina": "Matemática", "nota": 7.0},
    {"aluno": "Alice", "disciplina": "História", "nota": 8.0},
    {"aluno": "Bob", "disciplina": "História", "nota": 6.5},
    {"aluno": "Alice", "disciplina": "Física", "nota": 9.0}
]
``` 

## Resultado esperado:

``` 
{
    "Alice": [9.5, 8.0, 9.0],
    "Bob": [7.0, 6.5]
}
```

## Dica: A lógica é idêntica ao dos filmes!

- Crie um dicionário vazio.

- Percorra a lista_notas com um for.

- Verifique se o aluno já é uma chave no seu dicionário. Se não for, crie a chave apontando para uma lista vazia.

- Use o .append() para adicionar a nota dentro da lista daquele aluno.

Tente escrever a função agrupar_notas_por_aluno e veja se consegue chegar nesse dicionário final. 