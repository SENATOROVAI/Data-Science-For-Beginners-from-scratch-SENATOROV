"""Limits and continuity of functions."""

# +
# 1


import math
from typing import Callable, cast


def sequence_term(n_var: int) -> float:
    """Compute the value of the sequence term defined as n / (n + 1)."""
    return n_var / (n_var + 1)


def main_1() -> None:
    """Evaluate the corresponding sequence term."""
    n_var = int(input())
    result = sequence_term(n_var)
    print(f"{result:.6f}")


if __name__ == "__main__":
    main_1()


# +
# 2

# fmt: off

def evaluate(expr: str, x_var: float) -> float:
    """Evaluate a mathematical expression at a given point."""
    return cast(
        float,
        eval(  # pylint: disable=eval-used
            expr,
            {
                "__builtins__": None,
                "x": x_var,
                "abs": abs,
                "max": max,
                "min": min,
                "math": math,
            },
        ),
    )


def main_2() -> None:
    """Check continuity within the function around a given point."""
    expr = input().strip()
    x0 = float(input().strip())
    delta = float(input().strip())

    eps = 5 * delta

    f_x0 = evaluate(expr, x0)
    left = evaluate(expr, x0 - delta)
    right = evaluate(expr, x0 + delta)

    if abs(left - f_x0) < eps and abs(right - f_x0) < eps:
        print("CONTINUOUS")
    else:
        print("DISCONTINUOUS")


if __name__ == "__main__":
    main_2()
# fmt: on

# +
# 3

# fmt: off

def make_function(expr: str) -> Callable[[float], float]:
    """Construct a callable function f(x) from a string expression."""
    return cast(
        Callable[[float], float],
        eval(  # pylint: disable=eval-used
            "lambda x, e=math.e: " + expr, {"math": math}
        ),
    )


def is_lipschitz_on_interval(
    f_var: Callable[[float], float],
    a_var: float,
    b_var: float,
    l_var: float,
    epsilon: float = 1e-6,
) -> bool:
    """Check whether a function satisfies the Lipschitz condition."""
    m_var = 10000
    dx = (b_var - a_var) / m_var

    xs = [a_var + i * dx for i in range(m_var + 1)]
    f_values = [f_var(x) for x in xs]

    max_quot = 0.0
    for i_var in range(m_var):
        q_var = abs(f_values[i_var + 1] - f_values[i_var]) / dx
        max_quot = max(max_quot, q_var)

    return max_quot <= l_var + epsilon


def main_3() -> None:
    """Verify the Lipschitz condition on the specified interval."""
    expr = input().strip()
    a_var, b_var = map(float, input().split())
    l_input = input().strip()

    try:
        l_var = float(
            eval(l_input, {"math": math, "e": math.e})  # pylint: disable=eval-used
        )
    except (NameError, SyntaxError, TypeError, ValueError):
        l_var = float(l_input)

    f_var = make_function(expr)
    if is_lipschitz_on_interval(f_var, a_var, b_var, l_var):
        print("LIPSCHITZ")
    else:
        print("NOT LIPSCHITZ")


if __name__ == "__main__":
    main_3()
# fmt: on
