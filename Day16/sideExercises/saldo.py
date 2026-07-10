class ContaBancaria:

    def __init__ (self, titular):
        self.titular = titular
        self.saldo = 0
    
    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente!")
    
def main():
    conta1 = ContaBancaria("Matheus")
    conta1.depositar(100)
    conta1.sacar(25)
    print(f"Valor final: {conta1.saldo}")

if __name__ == "__main__":
    main()