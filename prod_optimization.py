from rich import print
import pulp

model = pulp.LpProblem("Максимальна загальна кількість продуктів: ", pulp.LpMaximize)

# Визначення змінних
x = pulp.LpVariable("limonad", lowBound=0, cat="Integer")
y = pulp.LpVariable("fruit_juice", lowBound=0, cat="Integer")

# Цільова функція
model += x + y, "Загальна кількість продуктів"

# Обмеження
model += 2 * x + y <= 100, "Water"
model += x  <= 50, "Sugar"
model += x  <= 30, "Lemon juice"
model += 2 * y <= 40, "Fruit puree"

# Розвязання
model.solve()

# Вивід результатів
print(f"\n[bold green]Статус рішення:[/bold green] {pulp.LpStatus[model.status]}")
print("[bold green]Оптимальна кількість виготовлення Лимонаду:[/bold green]", x.varValue)
print("[bold red]Оптимальна кількість виготовлення Фрутового соку:[/bold red]", y.varValue)
print(f"[bold blue]Загальна кількість продуктів:[/bold blue] {int(x.varValue + y.varValue)}")


