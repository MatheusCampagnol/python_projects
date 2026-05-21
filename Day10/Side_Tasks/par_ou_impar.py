#- pede um número
#- diz se é par ou ímpar
#- pergunta se quer continuar
from rich import print

def show_result(number, result):
    print(f"Seu número {number} é {result}.")


def check_even_or_not(number):
    result = ""
    if number % 2 == 0:
        result = "par"
    else:    
        result = "ímpar"
    return result            
    

def get_number(prompt):
    while True:
#Coleta o número via função get_number da main, converte aqui para int
#e atribui o valor a value.
        value = (input(prompt).strip())
#Checa primeiro se há pontos ou vírgulas (sinal de float). Se houver, descarta.
        if "," in value or "." in value:
            print("[bold red]Digite apenas números inteiros.[/bold red]")
            continue
#Checa se há alphas no número. Se houver, descarta.        
        if any(number.isalpha() for number in value):
            print("[bold red]Letters are not allowed.[/bold red]")
            continue
#Tenta por fim retornar um int. Se falhar, sobe um ValueError.        
        try:
            return int(value)
        except ValueError:
            print("[bold red]Invalid number.[/bold red]")

def reprocess(prompt):
    while True:
        go_again_ind = (input(prompt))
        if go_again_ind in ["sim", "Sim", "não", "Não"]:
            return go_again_ind
        else:
#Retorna a própria função novamente.
            print(f"[bold red]Esse valor é inválido. Tente novamente.[/bold red]")                        
            return input(prompt).lower()
        

def main():
    while True:
        number = get_number("Digite um número para checar se é par ou ímpar: ")
        result = check_even_or_not(number)
        show_result(number, result)
        go_again = reprocess("Deseja checar novamente? Digite 'Sim' para continuar, 'Não' para parar: ").lower()
        
        if go_again == "não":
            break
    
if __name__ == "__main__":
    main()