"""ДЗ 1. Блок 4. Основы линейной алгебры и матана для машинного обучения.

Курс ня Яндекс "Математический анализ".
"""

# +
import numpy as np
import pandas as pd

# fmt: off
# isort: skip_file        
# pyupgrade: disable      
# pylint: skip-file       
# flake8: noqa           
# mypy: ignore-errors     
# codespell:disable

# +
# 3.2 Задача A
import sys


# def main():
#     input = sys.stdin.read()
def main(input):
    """Запуск."""    
    input_1 = input.split('\n')
    
    line = input_1[0].split(' ')

    N = int(line[0])
    approximation = N / (N + 1)
    print(f"{approximation:.6f}")

if __name__ == "__main__":
    # main()
    
    input = '1000'
    main(input)


# +
# 3.2 Задача B

# def main():
#     input = sys.stdin.read()
def main(input):
    """Запуск."""
    input_1 = input.split('\n')
    
    # Считываем входные данные
    f_expr = input_1[0].strip()
    x0     = float(input_1[1].strip())
    delta  = float(input_1[2].strip())
    
    # Определяем допуск
    epsilon = 5 * delta
    
    # Создаем функцию из строки
    def f(x):
        return eval(f_expr, {'x': x, 'abs': abs, 'max': max, 'min': min})
    
    # Вычисляем значения функции в ключевых точках
    try:
        f_x0 = f(x0)
        f_left = f(x0 - delta)
        f_right = f(x0 + delta)
    except:
        # По условию задачи исключений не должно быть, но на всякий случай
        print("DISCONTINUOUS")
        return
    
    # Проверяем условия непрерывности
    left_continuous = abs(f_left - f_x0) < epsilon
    right_continuous = abs(f_right - f_x0) < epsilon
    
    # Выводим результат
    if left_continuous and right_continuous:
        print("CONTINUOUS")
    else:
        print("DISCONTINUOUS")

if __name__ == "__main__":
    # main()
    
    input = 'abs(x)' + '\n' + \
            '0' + '\n' + \
            '0.001'
    main(input)

# +
# 3.2 Задача C

import math
import numpy as np

# def main():
#     input = sys.stdin.read()
def main(input):
    """Запуск."""
    input_1 = input.split('\n')
    # Считываем входные данные
    f_expr = input_1[0].strip()
    a, b   = map(float, input_1[1].split())
    L      = float(input_1[2].strip())
    
    epsilon = 1e-6
    
    # Создаем функцию
    def f(x):
        return eval(f_expr, {'x': x, 'e': math.e, 'exp': math.exp, 'math': math})
    
    # Более эффективная проверка: ищем максимальное отношение |f(x)-f(y)|/|x-y|
    n_points = 500
    x_values = np.linspace(a, b, n_points)
    f_values = np.array([f(x) for x in x_values])
    
    # Вычисляем все попарные разности
    max_ratio = 0
    for i in range(n_points):
        for j in range(i + 1, n_points):
            if abs(x_values[i] - x_values[j]) > epsilon:
                ratio = abs(f_values[i] - f_values[j]) / abs(x_values[i] - x_values[j])
                max_ratio = max(max_ratio, ratio)
    
    # Проверяем условие
    if max_ratio <= L + epsilon:
        print("LIPSCHITZ")
    else:
        print("NOT LIPSCHITZ")

if __name__ == "__main__":
    # main()
    
    input = 'x ** 2' + '\n' + \
            '0 1' + '\n' + \
            '2'
    main(input)
