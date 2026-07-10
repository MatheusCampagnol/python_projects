class Car:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def exibir_detalhes(self):
        print(f"Marca do carro: {self.marca}, do modelo {self.modelo} e ano {self.ano}")


carro1 = Car("Fiat", "Fastback", "2022")
carro2 = Car("Volkswagen", "Polo", "2018")

carro1.exibir_detalhes()
carro2.exibir_detalhes()
