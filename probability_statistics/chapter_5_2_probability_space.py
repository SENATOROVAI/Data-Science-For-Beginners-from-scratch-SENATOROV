"""Probability space."""

# +
# 1


import math
from itertools import product


def main_1() -> None:
    """Compute prob-ty of getting k_var heads in n_var biased coin tosses."""
    n_var, k_var = map(int, input().split())
    p_var = float(input().replace(",", "."))

    prob = 0.0
    for outcome in product((0, 1), repeat=n_var):
        h_var = sum(outcome)
        if h_var >= k_var:
            prob += (p_var**h_var) * ((1 - p_var) ** (n_var - h_var))

    print(prob)


if __name__ == "__main__":
    main_1()

# +
# 2


def main_2() -> None:
    """Compute probability that sum of two uniforms is below a threshold."""
    c_var, d_var = map(float, input().replace(",", ".").split())

    if d_var <= 0:
        asym = 0.0
    elif d_var >= 2 * c_var:
        asym = 1.0
    elif d_var <= c_var:
        asym = (d_var * d_var) / (2.0 * c_var * c_var)
    else:  # C < D < 2C
        asym = 1.0 - ((2.0 * c_var - d_var) ** 2) / (2.0 * c_var * c_var)

    print(f"{asym:.10f}")


if __name__ == "__main__":
    main_2()

# +
# 3


def comb(n_smpl: int, k_smpl: int) -> int:
    """Return binomial coefficient with safe handling of invalid arguments."""
    if n_smpl < k_smpl:
        return 0
    return math.comb(n_smpl, k_smpl)


def main_3() -> None:
    """Compute probabilities of at least one green and all same color balls."""
    r_var, g_var, b_var = map(int, input().split())
    num = r_var + g_var + b_var

    total = comb(num, 3)

    # 1. хотя бы один зелёный
    p1 = 1 - comb(r_var + b_var, 3) / total

    # 2. все три одного цвета
    p2 = (comb(r_var, 3) + comb(g_var, 3) + comb(b_var, 3)) / total

    print(f"{p1:.15f} {p2:.15f}")


if __name__ == "__main__":
    main_3()

# +
# 4


def main_4() -> None:  # pylint: disable=too-many-locals
    """Determine symmetric confidence band for coin test and classify sample."""
    # 1) читаем и парсим первую строку в ТАКИЕ ЖЕ по смыслу, но новые имена
    first_line: str = input()
    n_token, conf_token = first_line.split()
    n_qwe: int = int(n_token)
    conf: float = float(conf_token.replace(",", "."))

    # 2) читаем вторую строку и преобразуем в список int
    second_line: str = input()
    seq_tokens: List[str] = second_line.split()
    seq: List[int] = [int(x) for x in seq_tokens]
    heads: int = sum(seq)

    # 3) вычисления без изменения типов
    max_k: int = (n_qwe - 1) // 2

    combs: List[int] = [math.comb(n_qwe, h) for h in range(n_qwe + 1)]
    pref: List[int] = [0]
    s_var: int = 0
    for h_var in range(n_qwe + 1):
        s_var += combs[h_var]
        pref.append(s_var)  # pref[h+1] = sum_{t=0}^h C(n,t)

    total: int = 1 << n_qwe
    eps: float = 1e-12

    best_k: int = 0
    for k_xmp in range(0, max_k + 1):
        central: int = total - 2 * pref[k_xmp]
        if central + eps >= conf * total:
            best_k = k_xmp

    l_var: int = best_k
    r_var: int = n_qwe - best_k
    print(f"{l_var} {r_var}")
    print("fair" if l_var <= heads <= r_var else "biased")


if __name__ == "__main__":
    main_4()
