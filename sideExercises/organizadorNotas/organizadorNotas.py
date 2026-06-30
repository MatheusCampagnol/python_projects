lista_notas = [
    {"aluno": "Alice", "disciplina": "Matemática", "nota": 9.5},
    {"aluno": "Bob", "disciplina": "Matemática", "nota": 7.0},
    {"aluno": "Alice", "disciplina": "História", "nota": 8.0},
    {"aluno": "Bob", "disciplina": "História", "nota": 6.5},
    {"aluno": "Alice", "disciplina": "Física", "nota": 9.0}
]

def agrupar_notas_por_aluno(lista_notas):
#1. Aqui há um dicionário vazio que deve receber os dados posteriormente.
    lista_notas_organizadas = {}

#2. Extração de dados. Aqui devemos usar o contador que percorre o dicionário.
    for alunos in lista_notas:
        aluno_atual = alunos["aluno"]
        nota_atual = alunos["nota"]

#3. Se não houver a entrada da chave no dicionário, adicionar.
        if aluno_atual not in lista_notas_organizadas:
            lista_notas_organizadas[aluno_atual] = []
#4. Faz o append das notas de uma determinada chave.
        lista_notas_organizadas[aluno_atual].append(nota_atual)
#5. Retorna o valor para o resultado da main que é mostrado posteriormente.
    return lista_notas_organizadas


def main():
    resultado = agrupar_notas_por_aluno(lista_notas)
    print(resultado)



if __name__ == "__main__":
    main()