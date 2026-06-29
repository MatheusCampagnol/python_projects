filmes_desorganizados = [
    {"titulo": "Matrix", "genero": "Ficção"},
    {"titulo": "O Senhor dos Anéis", "genero": "Fantasia"},
    {"titulo": "Duro de Matar", "genero": "Ação"},
    {"titulo": "Blade Runner", "genero": "Ficção"},
    {"titulo": "Gladiador", "genero": "Ação"},
    {"titulo": "Harry Potter", "genero": "Fantasia"}
]

filmes_organizados = [
    {
        "Ficção": []
    },
    {
        "Fantasia": []
    },
    {
        "Ação": []
    }
]

# Crie a função agrupar_por_genero(lista_filmes) aqui
# O resultado esperado ao final é um dicionário assim:
# {
#   "Ficção": ["Matrix", "Blade Runner"],
#   "Fantasia": ["O Senhor dos Anéis", "Harry Potter"],
#   "Ação": ["Duro de Matar", "Gladiador"]
# }


def agrupar_por_genero(lista_filmes):
    # 1. Criamos o dicionário vazio ANTES do loop começar
    filmes_organizados = {}

    for filme in lista_filmes:
        # Extraímos os dados para facilitar a leitura
        genero_atual = filme["genero"]
        titulo_atual = filme["titulo"]

        # 2. Verificamos se esse gênero já existe no dicionário novo
        # Se NÃO existir, nós criamos a chave e colocamos uma lista vazia lá dentro
        if genero_atual not in filmes_organizados:
            filmes_organizados[genero_atual] = []
        
        # 3. Agora TEMOS CERTEZA que a chave existe e que lá dentro tem uma lista.
        # Só falta colocar o titulo_atual dentro dessa lista!
        
        filmes_organizados[genero_atual].append(titulo_atual)

    # Retornamos o dicionário completo e organizado
    return filmes_organizados




if __name__ == "__main__":
    resultado = agrupar_por_genero(filmes_desorganizados)
    print(resultado)