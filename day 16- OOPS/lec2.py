from prettytable import PrettyTable
table=PrettyTable()
# table is the object of class PrettyTable
table.add_column("Pokemon Name",["pikachu","squirtle","charmander"])
table.add_column("Type",["Electric","Water","fire"])

#changing ttable style
print(table.align)
table.align="l"
print(table.align)
print(table)