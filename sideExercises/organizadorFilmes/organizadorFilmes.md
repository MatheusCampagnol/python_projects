# Exercício 2: O Organizador de Filmes

## Objetivo: Praticar a criação dinâmica de dicionários e o aninhamento (listas dentro de dicionários).

Você tem uma lista de dicionários, onde cada dicionário representa um filme e seu respectivo gênero. O problema é que esses dados estão desorganizados.

Sua tarefa:
- Crie uma função chamada agrupar_por_genero(lista_filmes) que recebe essa lista e retorna um único dicionário, onde as chaves são os gêneros (ex: "Ficção", "Ação") e os valores são listas contendo os nomes dos filmes daquele gênero.

```
filmes_desorganizados = [
    {"titulo": "Matrix", "genero": "Ficção"},
    {"titulo": "O Senhor dos Anéis", "genero": "Fantasia"},
    {"titulo": "Duro de Matar", "genero": "Ação"},
    {"titulo": "Blade Runner", "genero": "Ficção"},
    {"titulo": "Gladiador", "genero": "Ação"},
    {"titulo": "Harry Potter", "genero": "Fantasia"}
]

# Crie a função agrupar_por_genero(lista_filmes) aqui
# O resultado esperado ao final é um dicionário assim:
# {
#   "Ficção": ["Matrix", "Blade Runner"],
#   "Fantasia": ["O Senhor dos Anéis", "Harry Potter"],
#   "Ação": ["Duro de Matar", "Gladiador"]
# }
```
