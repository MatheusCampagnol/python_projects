class Produto:
    def __init__(self, produto, preco):
        self.produto = produto
        self.preco = preco


class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar_produto(self, produto):
        self.itens.append(produto)    

    def mostrar_carrinho_de_compras(self):
        print("Seu carrinho contém os seguintes itens")
        for indice, item in enumerate(self.itens, start=1):
            print(f"{indice}. {item.produto}, preço: R${item.preco}")

    def calcular_total(self):
        valor_total = 0
        for item in self.itens:
            valor_total += item.preco
        print(f"O seu sub-total até o momento é de R${valor_total}")


produto1 = Produto("Detergente Ypê", 2.50)
produto2 = Produto("Tênis New Balance BB80", 315)
carrinho1 = Carrinho()
carrinho1.adicionar_produto(produto1)
carrinho1.adicionar_produto(produto2)
carrinho1.mostrar_carrinho_de_compras()
carrinho1.calcular_total()


