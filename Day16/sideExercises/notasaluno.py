class Aluno:
    def __init__ (self, nome):
        self.nome = nome
        self.notas = []

    def adicionar_nota(self, notas):
        self.notas.append(notas)

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)

    def verificar_status(self):
        media = sum(self.notas) / len(self.notas)
        if media >= 7:
            return "Aprovado"
        else:
            return "Reprovado"

def main():
    aluno1 = Aluno("Matheus")
    aluno1.adicionar_nota(2)
    aluno1.adicionar_nota(2)
    aluno1.adicionar_nota(2)
    media = aluno1.calcular_media()
    print(f"Média do aluno {aluno1.nome}: {media}")
    print(aluno1.verificar_status())

if __name__ == "__main__":
    main()