"""Vectors."""

# +
# 1


import math
import numpy as np


def main_1() -> None:
    """Compute vector linear combinaion."""
    k_var = int(input().strip())
    lambdas = list(map(float, input().split()))

    vectors = [list(map(float, input().split())) for _ in range(k_var)]

    n_var = len(vectors[0])

    result = [0.0] * n_var

    for i_var in range(k_var):
        for j_var in range(n_var):
            result[j_var] += lambdas[i_var] * vectors[i_var][j_var]

    print(" ".join(f"{x:.1f}" for x in result))


if __name__ == "__main__":
    main_1()

# +
# 2


def main_2() -> None:
    """Check vector orthogonality."""
    m_var = int(input().strip())  # размерность векторов
    u_var = list(map(int, input().split()))
    v_var = list(map(int, input().split()))

    dot_product = sum(u_var[i] * v_var[i] for i in range(m_var))

    if dot_product == 0:
        print("ORTHOGONAL")
    else:
        print("NON-ORTHOGONAL")


if __name__ == "__main__":
    main_2()

# +
# 3


def main_3() -> None:  # pylint: disable=too-many-branches
    """Detect linear combination and basis."""
    v1 = list(map(int, input().split()))
    v2 = list(map(int, input().split()))
    v3 = list(map(int, input().split()))

    a_var, b_var = v1
    c_var, d_var = v2
    x_var, y_var = v3

    det = a_var * d_var - b_var * c_var

    if det != 0:
        lam1 = (x_var * d_var - y_var * c_var) / det
        lam2 = (y_var * a_var - x_var * b_var) / det
        if lam1.is_integer() and lam2.is_integer():
            print(int(lam1), int(lam2))
        else:
            print("NO_SOLUTION")
    else:
        if a_var == c_var == 0 and b_var == d_var == 0:
            print("NO_SOLUTION")
            return

        if a_var != 0:
            t_var = x_var / a_var
            if b_var * t_var == y_var:
                if t_var.is_integer():
                    print(int(t_var), 0)
                else:
                    print("NO_SOLUTION")
            else:
                print("NO_SOLUTION")
        elif c_var != 0:
            t_var = x_var / c_var
            if d_var * t_var == y_var:
                if t_var.is_integer():
                    print(0, int(t_var))
                else:
                    print("NO_SOLUTION")
            else:
                print("NO_SOLUTION")
        else:
            print("NO_SOLUTION")


if __name__ == "__main__":
    main_3()

# +
# 4


def main_4() -> None:
    """Find an angle between vectors in degrees."""
    n_var = int(input().strip())
    v1 = list(map(int, input().split()))
    v2 = list(map(int, input().split()))

    dot = sum(v1[i] * v2[i] for i in range(n_var))
    norm1 = math.sqrt(sum(x * x for x in v1))
    norm2 = math.sqrt(sum(x * x for x in v2))

    if norm1 == 0 or norm2 == 0:
        print(0)
        return

    cos_theta = dot / (norm1 * norm2)
    cos_theta = max(-1, min(1, cos_theta))

    angle = math.degrees(math.acos(cos_theta))
    print(int(angle))


if __name__ == "__main__":
    main_4()

# +
# 5


def main_5() -> None:
    """Check if a set of vectors is linearly independent."""
    m_smpl, n_smpl = map(int, input().split())  # pylint: disable=unused-variable
    vectors = [list(map(int, input().split())) for _ in range(m_smpl)]

    matrix = np.array(vectors, dtype=int)
    rank = np.linalg.matrix_rank(matrix)

    if rank < m_smpl:
        print("LINEARLY_DEPENDENT")
    else:
        print("LINEARLY_INDEPENDENT")


if __name__ == "__main__":
    main_5()
