from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#Instancia-se as classes.
money_machine = MoneyMachine()
menu = Menu()
coffe_maker = CoffeeMaker()

#Cria-se uma variável de controle para desligamento da máquina.
is_on = True

#Loop geral para fazer as coisas enquanto a máquina está ligada.
while is_on:
#Passa os itens via método get_items da classe Menu instanciada por menu.
    options = menu.get_items()
#Abre uma variável choice para a escolha da bebida. 
#Options então passa a ser nossas opções vinda do método anterior, via classe Menu.    
    choice = input(f"What would you like ({options}): ")
#Agora aplicam-se as escolhas possíveis como desligar a máquina, relatórios (report) ou por fim, fazer a bebida.
#Rotina para desligamento da máquina:
    if choice == "off":
        is_on = False
#Rotina para processamento do relatório: veja que esses dois métodos são chamados de objetos diferentes e ambos tem propósitos diferentes.
#Um traz a quantidade de recursos, o outro o de dinheiro recebido.
    elif choice == "report":
        coffe_maker.report()
        money_machine.report()
#Finalmente, o processamento da bebida.        
    else:
#Veja que aqui a variável drink é criada e a bebida é buscada no Menu via variável Choice anterior.        
        drink = menu.find_drink(choice)
#E agora observe que as checagens finais são feitas. Se há recurso suficiente,
#Se o dinheiro inserido é suficiente e por fim, se ambas são atendidas, faz-se o café.
    if coffe_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
        coffe_maker.make_coffee(drink)        
