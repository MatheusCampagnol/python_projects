from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Pokemon Name", "Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Charizard", "Fire/Flying"])
table.add_row(["Charmander", "Fire"])
table.align = "l"           
print(table)


