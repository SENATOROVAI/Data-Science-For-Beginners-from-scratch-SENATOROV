"""Matrices."""

# +
# 1


import math


def main_1() -> None:
    """Read a square matrix from input and prints its type."""
    n_var = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n_var)]

    is_diagonal = True
    is_upper = True
    is_lower = True

    for i_var in range(n_var):
        for j_var in range(n_var):
            if i_var != j_var and matrix[i_var][j_var] != 0:
                is_diagonal = False
            if i_var > j_var and matrix[i_var][j_var] != 0:
                is_upper = False
            if i_var < j_var and matrix[i_var][j_var] != 0:
                is_lower = False

    if is_diagonal:
        print("DIAGONAL")
    elif is_upper:
        print("UPPER_TRIANGULAR")
    elif is_lower:
        print("LOWER_TRIANGULAR")
    else:
        print("OTHER")


if __name__ == "__main__":
    main_1()

# +
# 2


def main_2() -> None:
    """Read two matrices A and B from input and print their product."""
    m_smpl, n_smpl = map(int, input().split())
    a_var = [list(map(int, input().split())) for _ in range(m_smpl)]

    h_var, k_var = map(int, input().split())
    b_var = [list(map(int, input().split())) for _ in range(h_var)]

    if n_smpl != h_var:
        print("NOT_DEFINED")
        return

    c_var = [[0 for _ in range(k_var)] for _ in range(m_smpl)]

    for i_smpl in range(m_smpl):
        for j_smpl in range(k_var):
            for t_var in range(n_smpl):
                c_var[i_smpl][j_smpl] += a_var[i_smpl][t_var] * b_var[t_var][j_smpl]

    for row in c_var:
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    main_2()

# +
# 3


def main_3() -> None:
    """Read a square matrix and prints the smallest k (1 <= k <= 100)."""
    n_obj = int(input())
    a_smpl = [list(map(int, input().split())) for _ in range(n_obj)]

    def mat_mult(x_var: list[list[int]], y_var: list[list[int]]) -> list[list[int]]:
        """Multiply two square matrices and return the result."""
        result = [[0] * n_obj for _ in range(n_obj)]
        for i_obj in range(n_obj):
            for j_obj in range(n_obj):
                for t_smpl in range(n_obj):
                    result[i_obj][j_obj] += x_var[i_obj][t_smpl] * y_var[t_smpl][j_obj]
        return result

    def is_zero_matrix(m_obj: list[list[int]]) -> bool:
        """Return True if the matrix is a zero matrix, False otherwise."""
        for row in m_obj:
            if any(x != 0 for x in row):
                return False
        return True

    power = a_smpl
    for k_smpl in range(1, 101):
        if is_zero_matrix(power):
            print(k_smpl)
            return
        power = mat_mult(power, a_smpl)

    print("NOT_FOUND")


if __name__ == "__main__":
    main_3()

# +
# 4


def main_4() -> None:
    """Read a matrix A of size m x n and print its transpose n x m."""
    m_obj, n_val = map(int, input().split())
    a_obj = [list(map(int, input().split())) for _ in range(m_obj)]

    at = [[0] * m_obj for _ in range(n_val)]
    for i_lm in range(m_obj):
        for j_lm in range(n_val):
            at[j_lm][i_lm] = a_obj[i_lm][j_lm]

    for row in at:
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    main_4()

# +
# 5


def main_5() -> None:
    """Read a matrix A (m x n) and normalize each column."""
    m_val, n_lm = map(int, input().split())
    a_lm = [list(map(int, input().split())) for _ in range(m_val)]

    result = [[0] * n_lm for _ in range(m_val)]

    for j_mc in range(n_lm):
        col = [a_lm[i_mc][j_mc] for i_mc in range(m_val)]
        mean = sum(col) / m_val
        variance = sum((x - mean) ** 2 for x in col) / m_val
        std_dev = math.sqrt(variance)
        if std_dev == 0:
            std_dev = 1
        for i_pl in range(m_val):
            normalized = (a_lm[i_pl][j_mc] - mean) / std_dev
            result[i_pl][j_mc] = int(normalized)

    for row in result:
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    main_5()
