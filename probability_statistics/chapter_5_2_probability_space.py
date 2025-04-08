"""Probability Space."""

# +
# 1

import math
import sys
from itertools import combinations
from math import comb

data: list[str] = sys.stdin.readlines()
n_val: int
k_val: int
n_val, k_val = map(int, data[0].split())
p_val: float = float(data[1].strip())


def binomial_probability(n_v: int, k_v: int, p_v: float) -> float:
    """Calculate the binomial probability for given n, k and p values."""
    combination_counts = math.factorial(n_v) / (
        math.factorial(k_v) * math.factorial(n_v - k_v)
    )
    return combination_counts * (p_v**k_v) * ((1 - p_v) ** (n_v - k_v))


result_prob: float = 0.0
for num in range(k_val, n_val + 1):
    result_prob += binomial_probability(n_val, num, p_val)

print(result_prob)

# +
# 2

C_val, D_val = map(float, sys.stdin.read().split())

if D_val <= 0:
    result = 0.0
elif D_val >= 2 * C_val:
    result = 1.0
elif D_val <= C_val:
    result = (D_val**2) / (2 * C_val * C_val)
else:
    result = 1 - ((2 * C_val - D_val) ** 2) / (2 * C_val * C_val)

print(result)

# +
# 3

R_val, G_val, B_val = map(int, input().split(" "))
values = list(combinations(["R"] * R_val + ["G"] * G_val + ["B"] * B_val, 3))
green_one_val_count = 0
one_color_val_count = 0

for comb_val in values:
    if "G" in comb_val:
        green_one_val_count += 1
    if len(set(comb_val)) == 1:
        one_color_val_count += 1

print(green_one_val_count / len(values), one_color_val_count / len(values))

# +
# 4

input_str = input().split()
num_flips: int = int(input_str[0])
fairness_threshold: float = float(input_str[1])

flip_results = list(map(int, input().split()))
num_heads = sum(flip_results)

binomial_probabilities = [
    comb(num_flips, k) * (0.5**num_flips) for k in range(num_flips + 1)
]

best_margin = 0
for margin in range(num_flips // 2 + 1):
    probability_within_margin = sum(
        binomial_probabilities[margin : num_flips - margin + 1]
    )
    if probability_within_margin >= fairness_threshold:
        best_margin = margin

min_heads = best_margin
max_heads = num_flips - best_margin

print(min_heads, max_heads)
if min_heads <= num_heads <= max_heads:
    print("fair")
else:
    print("biased")
