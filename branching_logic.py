"""
Лабораторна робота № 3. Модуль 1.
Програмування алгоритмів розгалуженої структури та чисельне табулювання.
Виконала: Мунтян Марина, група ЕЛ-24-1 (Варіант 20)
Освітній компонент: Програмування на Python.
"""

import math
import sys

def evaluate_piecewise_function(x: float) -> float:
    """
    Обчислює значення кусочно-неперервної функції f(x) за допомогою
    каскадної конструкції розгалуження if-elif-else. (Для 20 варіанту)
    """
    if x <= 1.0:
        # Перша аналітична гілка для x <= 1
        y = math.cos(x) + math.exp(-x)
    elif 1.0 < x < 4.0:
        # Друга аналітична гілка для 1 < x < 4
        y = math.pow(x**2 + 7.0, 1.0/3.0)
    else:
        # Третя аналітична гілка для x >= 4
        y = 1.0 / (x**2 - 15.0)
    return y

def tabulate_function(start_a: float, end_b: float, step_h: float) -> list:
    """
    Здійснює чисельне табулювання функції на проміжку [a, b] із кроком h
    за допомогою параметричного циклу for та генератора range().
    """
    if step_h <= 0.0:
        raise ValueError("Крок табулювання h повинен бути строго додатним числом.")
    if start_a > end_b:
        raise ValueError("Початкова межа інтервалу 'a' не може перевищувати кінцеву 'b'.")

    # Обчислення кількості вузлів сітки
    num_steps = int(math.floor((end_b - start_a) / step_h))
    tabulated_data = []

    for i in range(num_steps + 1):
        # Точне позиціонування координати вузла
        x_i = start_a + i * step_h

        # Корекція похибки представлення кінцевої точки
        if x_i > end_b and math.isclose(x_i, end_b, abs_tol=1e-9):
            x_i = end_b
            
        y_i = evaluate_piecewise_function(x_i)
        
        # Класифікація діапазону за допомогою тернарного оператора
        branch_tag = "Гілка 1" if x_i <= 1.0 else ("Гілка 2" if x_i < 4.0 else "Гілка 3")
        
        tabulated_data.append((x_i, y_i, branch_tag))

    return tabulated_data

def print_tabulation_table(data: list) -> None:
    """Виводить на екран відформатовану таблицю значень функції."""
    separator = "=" * 65
    sub_sep = "-" * 65

    print(separator)
    print(f"{'ТАБЛИЦЯ ТАБУЛЮВАННЯ КУСОЧНОЇ ФУНКЦІЇ f(x) (ВАРІАНТ 20)':^65}")
    print(separator)
    print(f"| {'№':^4} | {'Вузол x':^14} | {'Значення y = f(x)':^20} | {'Сегмент':^14} |")
    print(sub_sep)

    for idx, (x_val, y_val, tag) in enumerate(data, start=1):
        print(f"| {idx:^4} | {x_val:^14.4f} | {y_val:^20.8f} | {tag:^14} |")

    print(separator)

if __name__ == "__main__":
    # Параметри для 20 варіанту: інтервал [0, 6], крок h = 0.3
    tab_results = tabulate_function(0.0, 6.0, 0.3)
    print_tabulation_table(tab_results)