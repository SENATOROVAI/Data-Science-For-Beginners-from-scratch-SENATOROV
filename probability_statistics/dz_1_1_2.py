"""ДЗ 1. Блок 1. Введение в теорию вероятностей. Раздел 2. Курс Яндекс 5.
Теория вероятностей.

Курс Математика для анализа данных. п.5 Теория вероятностей.
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
import sys
import itertools

# Задание 5.2.1

def calculate_probability(N, K, p):    
    """Рассчет вероятности."""
    total_outcomes = 0
    favorable_outcomes = 0
    
    # Генерируем все возможные исходы (орёл - 'H', решка - 'T')
    for outcome in itertools.product(['H', 'T'], repeat=N):
        total_outcomes += 1
        heads = outcome.count('H')
        if heads >= K:
            favorable_outcomes += 1
    
    # Вероятность каждого благоприятного исхода: p^heads * (1-p)^(N-heads)
    probability = 0.0
    for outcome in itertools.product(['H', 'T'], repeat=N):
        heads = outcome.count('H')
        if heads >= K:
            prob = (p ** heads) * ((1 - p) ** (N - heads))
            probability += prob
    
    return probability

def main():    
    """Запуск."""
    # Чтение входных данных
    N, K = map(int, input().split())
    p = float(input())

    # Вычисление и вывод вероятности
    result = calculate_probability(N, K, p)
    print(f"{result:.5f}")


if __name__ == '__main__':
    # input
    # ["20 5", 
    #  "0.8"]
    
    main()

# +
import sys

# Задание 5.2.2

def calculate_probability(C, D): 
    """Рассчет вероятности."""
    if D <= 0:
        return 0.0
    elif D >= 2 * C:
        return 1.0
    elif D <= C:
        probability = (D ** 2) / (2 * C ** 2)
    else:
        probability = 1 - ((2 * C - D) ** 2) / (2 * C ** 2)
    return probability

def main():
    """Запуск."""
    # Чтение входных данных
    C, D = map(float, input().split())

    # Вычисление и вывод вероятности
    result = calculate_probability(C, D)
    print(f"{result:.5f}")


if __name__ == '__main__':
    # input
    # ["20 40"]
    main()

# +
import sys

import math

# Задание 5.2.3

def calculate_probabilities(R, G, B):
    """Рассчет вероятности."""
    total_balls = R + G + B

    total_ways = math.comb(total_balls, 3)
   
    # 1. Вероятность хотя бы одного зелёного
    no_green_ways = math.comb(R + B, 3)

    prob_at_least_one_green = 1 - (no_green_ways / total_ways) if total_ways != 0 else 0.0

    

    # 2. Вероятность, что все три одного цвета
    prob_all_red = math.comb(R, 3) / total_ways if R >= 3 else 0.0
    prob_all_green = math.comb(G, 3) / total_ways if G >= 3 else 0.0
    prob_all_blue = math.comb(B, 3) / total_ways if B >= 3 else 0.0
    prob_all_same_color = prob_all_red + prob_all_green + prob_all_blue    

    return prob_at_least_one_green, prob_all_same_color

def main():
    """Запуск."""
    # Чтение входных данных
    R, G, B = map(int, input().split())

    # Вычисление вероятностей
    prob1, prob2 = calculate_probabilities(R, G, B)

    # Вывод с точностью до 5 знаков
    print(f"{prob1:.5f} {prob2:.5f}")

if __name__ == '__main__':
    # input
    # ["6 1 1"]
    main()

# +
import sys
import math
from itertools import combinations

# Задание 5.2.4

def calculate_confidence_interval(N, I):
    """Рассчет вероятности."""
    # Находим максимальное K, такое что P(K <= heads <= N-K) >= I
    total_outcomes = 2 ** N
    for K in range(N // 2, -1, -1):
        favorable_outcomes = 0
        for heads in range(K, N - K + 1):
            favorable_outcomes += math.comb(N, heads)
        probability = favorable_outcomes / total_outcomes
        if probability >= I:
            return K, N - K
    return 0, N

def check_coin_fairness(N, I, tosses):
    """Проверка честности монеты."""
    heads = sum(tosses)
    K, upper = calculate_confidence_interval(N, I)
    if K <= heads <= upper:
        return "fair"
    else:
        return "biased"

def main():
    """Запуск."""
    # Чтение входных данных
    N, I = input().split()
    N = int(N)
    I = float(I)
    tosses = list(map(int, input().split()))

    # Вычисление доверительного интервала
    K, upper = calculate_confidence_interval(N, I)

    # Проверка честности монетки
    result = check_coin_fairness(N, I, tosses)

    # Вывод результатов
    print(K, upper)
    print(result)


if __name__ == '__main__':
    # input    
    # ["13 0.6",
    #  "0 0 0 0 0 0 0 0 0 0 0 0 0"]
    main()

# +
import sys

# Задание 5.3.1


def calculate_probability(p, s1, f1, s2, f2, test1, test2):
    """Рассчет вероятности."""
    # Вероятность результатов тестов если пациент болен
    if test1 == 1 and test2 == 1:
        p_results_given_sick = s1 * s2
    elif test1 == 1 and test2 == 0:
        p_results_given_sick = s1 * (1 - s2)
    elif test1 == 0 and test2 == 1:
        p_results_given_sick = (1 - s1) * s2
    else:  # 0 0
        p_results_given_sick = (1 - s1) * (1 - s2)
    
    # Вероятность результатов тестов если пациент здоров
    if test1 == 1 and test2 == 1:
        p_results_given_healthy = f1 * f2
    elif test1 == 1 and test2 == 0:
        p_results_given_healthy = f1 * (1 - f2)
    elif test1 == 0 and test2 == 1:
        p_results_given_healthy = (1 - f1) * f2
    else:  # 0 0
        p_results_given_healthy = (1 - f1) * (1 - f2)
    
    # Полная вероятность наблюденных результатов
    p_results = p * p_results_given_sick + (1 - p) * p_results_given_healthy
    
    # Применяем теорему Байеса
    if p_results == 0:
        return 0.0  # чтобы избежать деления на ноль
    p_sick_given_results = (p * p_results_given_sick) / p_results
    
    return p_sick_given_results

def main():
    """Запуск."""
    # Чтение входных данных
    p, s1, f1, s2, f2 = map(float, input().split())
    test1, test2 = map(int, input().split())

    # Вычисление вероятности
    result = calculate_probability(p, s1, f1, s2, f2, test1, test2)

    # Вывод с точностью до 5 знаков
    print(f"{result:.5f}")


if __name__ == '__main__':
    # input
    # ["0.05 0.9 0.1 0.9 0.1",
    #  "1 1"]
    main()

# +
import sys

# Задание 5.3.2


def main():
    """Запуск."""
    input = sys.stdin.read
    data = input().split()
    
    M = int(data[0])
    experiments = []
    index = 1
    for _ in range(M):
        xA, xB, xC = map(int, data[index:index+3])
        experiments.append((xA, xB, xC))
        index += 3
    
    # Вычисляем вероятности отдельных событий
    count_A = sum(1 for exp in experiments if exp[0] == 1)
    count_B = sum(1 for exp in experiments if exp[1] == 1)
    count_C = sum(1 for exp in experiments if exp[2] == 1)
    
    P_A = count_A / M
    P_B = count_B / M
    P_C = count_C / M
    
    # Вычисляем вероятности пересечений
    count_AB = sum(1 for exp in experiments if exp[0] == 1 and exp[1] == 1)
    count_AC = sum(1 for exp in experiments if exp[0] == 1 and exp[2] == 1)
    count_BC = sum(1 for exp in experiments if exp[1] == 1 and exp[2] == 1)
    count_ABC = sum(1 for exp in experiments if exp[0] == 1 and exp[1] == 1 and exp[2] == 1)
    
    P_AB = count_AB / M
    P_AC = count_AC / M
    P_BC = count_BC / M
    P_ABC = count_ABC / M
    
    # Проверяем попарную независимость
    pairwise_independent = True
    if not (abs(P_AB - P_A * P_B) < 1e-9):
        pairwise_independent = False
    if not (abs(P_AC - P_A * P_C) < 1e-9):
        pairwise_independent = False
    if not (abs(P_BC - P_B * P_C) < 1e-9):
        pairwise_independent = False
    
    # Проверяем независимость в совокупности
    joint_independent = False
    if pairwise_independent:
        if abs(P_ABC - P_A * P_B * P_C) < 1e-9:
            joint_independent = True
    
    # Определяем результат
    if pairwise_independent and joint_independent:
        print("ALL_INDEPENDENT")
    elif pairwise_independent:
        print("PAIRWISE_ONLY")
    else:
        print("NOT_INDEPENDENT")


if __name__ == '__main__':
    # input
    # ["6",
    #  "1 1 0",
    #  "1 1 1",
    #  "0 0 0",
    #  "1 0 1",
    #  "1 0 1",
    #  "0 1 0"]
    main()

# +
import sys

# Задание 5.3.3


def main():
    """Запуск."""
    input = sys.stdin.read().split()
    ptr = 0
    
    M, N, K = map(int, input[ptr:ptr+3])
    ptr += 3
    
    # Чтение тренировочных данных
    train_data = []
    for _ in range(M):
        row = list(map(int, input[ptr:ptr+K+1]))
        ptr += K+1
        train_data.append(row)
    
    # Чтение тестовых данных
    test_data = []
    for _ in range(N):
        row = list(map(int, input[ptr:ptr+K]))
        ptr += K
        test_data.append(row)
    
    # Подсчет статистик
    spam_count = 0
    ham_count = 0
    spam_word_counts = [0] * K
    ham_word_counts = [0] * K
    
    for row in train_data:
        is_spam = row[0]
        words = row[1:]
        
        if is_spam:
            spam_count += 1
            for i in range(K):
                spam_word_counts[i] += words[i]
        else:
            ham_count += 1
            for i in range(K):
                ham_word_counts[i] += words[i]
    
    # Вычисление вероятностей без сглаживания
    P_spam = spam_count / M
    P_ham = ham_count / M
    
    spam_word_probs = []
    ham_word_probs = []
    
    for i in range(K):
        # Вероятность слова в спаме (без сглаживания)
        spam_prob = spam_word_counts[i] / spam_count if spam_count > 0 else 0.0
        # Вероятность слова в не-спаме (без сглаживания)
        ham_prob = ham_word_counts[i] / ham_count if ham_count > 0 else 0.0
        
        spam_word_probs.append(spam_prob)
        ham_word_probs.append(ham_prob)
    
    # Классификация тестовых данных
    results = []
    for test_row in test_data:
        # Вычисление вероятностей без учета знаменателя
        p_spam = P_spam
        p_ham = P_ham
        
        for i in range(K):
            word = test_row[i]
            if word == 1:
                p_spam *= spam_word_probs[i] if spam_word_probs[i] > 0 else 0.0
                p_ham *= ham_word_probs[i] if ham_word_probs[i] > 0 else 0.0
            else:
                p_spam *= (1 - spam_word_probs[i]) if spam_word_probs[i] < 1 else 0.0
                p_ham *= (1 - ham_word_probs[i]) if ham_word_probs[i] < 1 else 0.0
        
        # Определение класса
        if abs(p_spam - p_ham) < 1e-5:
            results.append(-1)
        elif p_spam > p_ham:
            results.append(1)
        else:
            results.append(0)
    
    print(' '.join(map(str, results)))

if __name__ == '__main__':
    # input
    # ["100 20 4",
    #  "1 0 0 0 0",
    #  "1 1 0 1 0",
    #  "1 0 0 0 0",
    #  "1 1 0 0 0",
    #  "1 0 0 1 0",
    #  "1 1 0 0 1",
    #  "1 0 0 0 0",
    #  "1 0 0 0 1",
    #  "1 0 0 1 0",
    #  "1 0 0 1 1",
    #  "1 0 0 1 0",
    #  "1 0 0 0 1",
    #  "1 1 0 1 0",
    #  "1 0 0 1 0",
    #  "1 1 0 0 0",
    #  "1 0 0 0 1",
    #  "1 1 0 0 0",
    #  "1 1 0 1 1",
    #  "1 0 0 0 0",
    #  "1 0 0 1 0",
    #  "1 0 0 0 0",
    #  "1 0 0 0 0",
    #  "1 0 0 0 0",
    #  "1 1 0 0 0",
    #  "1 1 0 0 1",
    #  "1 1 0 1 1",
    #  "1 0 0 1 1",
    #  "1 0 0 0 1",
    #  "1 1 0 0 0",
    #  "1 0 0 1 0",
    #  "1 0 0 0 1",
    #  "1 0 0 0 0",
    #  "1 1 0 1 0",
    #  "1 1 0 0 0",
    #  "1 0 0 0 0",
    #  "1 0 0 0 1",
    #  "1 1 0 0 0",
    #  "1 0 0 0 0",
    #  "1 0 0 0 0",
    #  "1 0 0 0 1",
    #  "1 1 0 0 0",
    #  "1 0 0 0 1",
    #  "1 0 0 0 1",
    #  "1 1 0 0 1",
    #  "1 0 0 0 1",
    #  "1 1 0 1 1",
    #  "1 1 0 0 0",
    #  "1 1 0 0 0",
    #  "1 0 0 1 0",
    #  "1 0 0 0 1",
    #  "0 1 1 1 1",
    #  "0 1 0 1 1",
    #  "0 1 1 1 1",
    #  "0 1 1 1 1",
    #  "0 1 1 1 1",
    #  "0 1 1 0 1",
    #  "0 1 1 1 0",
    #  "0 1 1 1 1",
    #  "0 1 1 1 1",
    #  "0 1 0 0 1",
    #  "0 1 1 1 1",
    #  "0 1 1 1 1",
    #  "0 1 1 1 1",
    #  "0 1 0 1 1",
    #  "0 0 1 0 1",
    #  "0 1 1 1 1",
    #  "0 1 1 0 1",
    #  "0 1 1 1 1",
    #  "0 1 1 1 1",
    #  "0 1 1 1 1",
    #  "0 1 1 1 1",
    #  "0 1 1 1 0",
    #  "0 1 1 1 1",
    #  "0 1 1 1 1",
    #  "0 1 1 1 1",
    #  "0 1 1 0 1",
    #  "0 1 1 1 1",
    #  "0 1 1 1 1",
    #  "0 1 1 1 1",
    #  "0 1 1 1 1",
    #  "0 1 1 1 1",
    #  "0 1 1 1 1",
    #  "0 0 1 1 0",
    #  "0 1 1 1 1",
    #  "0 1 1 1 1",
    #  "0 1 1 0 0",
    #  "0 1 1 1 1",
    #  "0 1 1 1 1",
    #  "0 1 1 0 1",
    #  "0 1 1 1 1",
    #  "0 1 1 1 1",
    #  "0 1 1 1 1",
    #  "0 0 1 1 1",
    #  "0 1 1 1 1",
    #  "0 1 1 1 0",
    #  "0 1 1 1 1",
    #  "0 1 1 1 0",
    #  "0 1 1 1 1",
    #  "0 0 1 1 1",
    #  "0 1 0 1 1",
    #  "1 0 1 1",
    #  "0 1 1 0",
    #  "1 0 1 0",
    #  "0 1 1 1",
    #  "0 1 1 0",
    #  "0 0 1 0",
    #  "0 1 0 1",
    #  "0 1 1 0",
    #  "0 0 0 1",
    #  "1 0 1 0",
    #  "0 1 1 0",
    #  "0 1 0 1",
    #  "1 0 1 0",
    #  "1 1 1 1",
    #  "0 1 0 1",
    #  "1 0 1 1",
    #  "0 0 0 0",
    #  "1 0 1 0",
    #  "0 0 1 0",
    #  "0 0 1 1"]
    main()
