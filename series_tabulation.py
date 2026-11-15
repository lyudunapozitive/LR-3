"""
Лабораторна робота № 3. Модуль 2.
Модуль розгалужених обчислень, чисельного табулювання та рекурентних рядів Тейлора.
Освітній компонент: Програмування на Python.
"""

import math
import sys
import time

def compute_taylor_series_var20(x: float, epsilon: float = 1e-7, max_iterations: int = 1000) -> tuple:
    """
    Обчислює суму ряду 1/(1+x^2) через розклад у ряд Тейлора
    за допомогою циклу while та рекурентного співвідношення.
    Повертає кортеж: (обчислена_сума, кількість_ітерацій, еталонне_значення, абсолютна_похибка).
    """
    if epsilon <= 0.0:
        raise ValueError("Параметр точності epsilon повинен бути строго більшим за нуль.")
   
    # Ініціалізація нульового члена ряду: a_0 = 1.0
    k = 0
    a_k = 1.0
    series_sum = a_k

    # Ітераційне накопичення доданків за рекурентною формулою
    while math.fabs(a_k) >= epsilon and k < max_iterations:
        k += 1
        # Рекурентний коефіцієнт R(k, x) = -x^2
        recurrence_ratio = -x * x
        a_k *= recurrence_ratio
        series_sum += a_k
    else:
        # Специфіка блоку else у циклах Python
        if k >= max_iterations:
            print(f"Попередження: Досягнуто ліміт ітерацій ({max_iterations}) для x = {x:.4f}!")

    reference_val = 1.0 / (1.0 + x**2)
    absolute_error = math.fabs(series_sum - reference_val)

    return series_sum, k, reference_val, absolute_error

def main() -> None:
    """Головна функція демонстрації циклічних процесів."""
    print("\n" + "=" * 80)
    print(f"{'ОБЧИСЛЕННЯ РЯДУ 1/(1+x^2) ІЗ ТОЧНІСТЮ eps = 1e-7 (ВАРІАНТ 20)':^80}")
    print("=" * 80)
    print(f"| {'Аргумент x':^10} | {'Сума ряду S(x)':^18} | {'Еталон':^18} | {'Ітерацій':^8} | {'Похибка':^14} |")
    print("-" * 80)

    # Тестові точки в межах області збіжності
    test_points = [-0.9, -0.5, -0.1, 0.0, 0.1, 0.5, 0.9]
    target_eps = 1e-7

    for x_test in test_points:
        calc_s, steps, ref_s, err = compute_taylor_series_var20(x_test, target_eps)    
        print(f"| {x_test:^10.2f} | {calc_s:^18.10f} | {ref_s:^18.10f} | {steps:^8} | {err:^14.4e} |")

    print("=" * 80 + "\n")

if __name__ == "__main__":
    t_start = time.perf_counter()
    main()
    t_elapsed = time.perf_counter() - t_start
    print(f"Загальний час виконання розрахунків: {t_elapsed * 1000:.3f} мс\n")