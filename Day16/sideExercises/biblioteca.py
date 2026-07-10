class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

class Biblioteca:
    def __init__(self):
        self.acervo = []

    def adicionar_livro(self, livro):
        self.acervo.append(livro)

    def emprestar_livro(self, titulo_do_livro):
        # Percorre a lista de objetos Livro
        for livro in self.acervo:
            if livro.titulo == titulo_do_livro:
                if livro.disponivel:
                    livro.disponivel = False
                    print(f"Sucesso: Você emprestou '{livro.titulo}'.")
                    return # Sai do método após encontrar e emprestar
                else:
                    print(f"O livro '{livro.titulo}' já está emprestado.")
                    return
        print("Livro não encontrado na biblioteca.")

    def mostrar_acervo(self):
        for livro in self.acervo:
            status = "Disponível" if livro.disponivel else "Emprestado"
            print(f"- {livro.titulo} por {livro.autor} [{status}]")

#Criação das instâncias
meulivro1 = Livro("Minha Amiga Genial", "Elena Ferrante")
minha_biblioteca = Biblioteca()

#Chama o método adicionar livro passando como parâmetro a instância meulivro1.
minha_biblioteca.adicionar_livro(meulivro1)

minha_biblioteca.mostrar_acervo()
minha_biblioteca.emprestar_livro("Minha Amiga Genial")
minha_biblioteca.emprestar_livro("Minha Amiga Genial") # Tentando emprestar de novo