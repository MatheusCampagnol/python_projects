import ascii_art as aa
from rich import print

dic_operators = {
    "Add": "+",
    "Subtraction": "-",
    "Multiplication": "*",
    "Division": "/"
}

def perform_add(first_number, second_number):
    return first_number + second_number

def perform_subtraction(first_number, second_number):
#Aqui podemos dar return direto, sem usar uma variável.    
    return first_number - second_number

def perform_multiplication(first_number, second_number):
    return first_number * second_number

def perform_division(first_number, second_number):
    return first_number / second_number

# Mapeia o símbolo para a função (isso evita vários if/elif)
operations_map = {
    "+": perform_add,
    "-": perform_subtraction,
    "*": perform_multiplication,
    "/": perform_division
}

def continue_calculation(result):
#atribui a variável answer para mostrar o resultado.
    answer = input(f"Type 'yes' to continue calculating with {result}. Otherwise type 'no': ").lower()
    if answer in ("yes", "no"):
        return answer
    print("[bold red]Invalid input. Please type only yes or no.[/bold red]")

def show_operations():
#Mostra as operações e provavelmente nem precisaria ser um dicionário.    
    for key, op in dic_operators.items():
        print(f"Operation [bold blue]{key}[/bold blue] can be used by typing: [bold blue]{op}[/bold blue]")

#Apenas uma função para coletar os números. Provavelmente a segunda nem era necessária.
def get_number(prompt):
    while True:
#prompt aqui pega o valor e faz um strip dele removendo quaisquer espaços.        
        value = input(prompt).strip()
#Checa para possíveis virgulas.
        if "," in value:
            print("[bold red]Use '.' instead of ','.[/bold red]")
            continue
#Checa se há alphas no c, no caso c = value.
        if any(c.isalpha() for c in value):
            print("[bold red]Letters are not allowed.[/bold red]")
            continue
#Retorna sempre um float mesmo se o valor for somente int. 
        try:
            return float(value)
        except ValueError:
            print("[bold red]Invalid number.[/bold red]")


def get_operation_symbol():
    valid_ops = set(dic_operators.values())
    while True:
        op = input("Pick an operation: ").strip()
        if op in valid_ops:
            return op
        print("[bold red]Choose an operation from the list and try again.[/bold red]")


def main():
    first_number = get_number("What's your first number: ")

    while True:
        show_operations()
        operation = get_operation_symbol()
        second_number = get_number("What's your next number? ")

        try:
            result = operations_map[operation](first_number, second_number)
        except ValueError as e:
            print(f"[bold red]ERROR:[/bold red] {e}")
            continue

        print(f"[bold green]Result:[/bold green] {result}")

        if continue_calculation(result) == "no":
            break

        # Aqui está o "pulo do gato": continuar a conta com o resultado atual
        first_number = result

if __name__ == "__main__":
    print(aa.ascii_art)
    main()