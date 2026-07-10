class Bichinho:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 0
        self.energia = 10
    
    def alimentar(self, quantidade):
        if self.energia + quantidade > 100:
            print("Aviso: Energia máxima atingida!")
            self.energia = 100 # Trava no limite máximo
        else:
            self.energia += quantidade
            self.fome -= quantidade

    def brincar(self, tempo):
        if self.energia - tempo < 0:
            print("Seu Tamagoichi precisa descansar.")
            self.energia = 0
        else:
            self.energia -= tempo
            self.fome += tempo
    
    def status(self):
        print(f"'{self.nome}' com {self.energia} de energia e {self.fome} de fome.")
    

tamagotchi1 = Bichinho("Matheus")
tamagotchi1.alimentar(105)
tamagotchi1.brincar(200)
tamagotchi1.status()