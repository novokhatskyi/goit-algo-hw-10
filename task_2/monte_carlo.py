from rich import print
import numpy as np
import random

def is_inside(x, y):
    """Перевіряє, чи знаходиться точка (x, y) всередині трикутника."""
    return y <= np.sin(x**2) + np.log(x + 1)

def monte_carlo_simulation(a, b, num_experiments):
    """Виконує серію експериментів методом Монте-Карло."""
    average_area = 0

    for _ in range(num_experiments):
        # Генерація випадкових точок
        points = [(random.uniform(0, a), random.uniform(0, b)) for _ in range(15000)]
        # Відбір точок, що знаходяться всередині трикутника
        inside_points = [point for point in points if is_inside(point[0], point[1])]

         # Розрахунок площі за методом Монте-Карло
        M = len(inside_points)
        N = len(points)
        area = (M / N) * (a * b)

        # Додавання до середньої площі
        average_area += area

        # Обчислення середньої площі
    average_area /= num_experiments
    return average_area


if __name__ == "__main__":
    # Розміри прямокутника
    x = 3  # ширина прямокутника
    y = 2.5  # висота прямокутника
    S = (x * y) / 2  # Теоретична площа

# Кількість експериментів
    num_experiments = 100

# Виконання симуляції
    average_area = monte_carlo_simulation(x, y, num_experiments)
    print(f"\n[bold green]Середня площа трикутника за [/bold green]{num_experiments} [bold green]експериментів:[/bold green] \n{average_area:.2f}\n")