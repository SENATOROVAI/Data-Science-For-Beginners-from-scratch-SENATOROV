"""Differentiation of single variable functions."""

# +
# 1


import math


def main_1() -> None:
    """Find and classify critical points of a cubic polynomial."""
    a_var, b_var, c_var, d_var = map(float, input().split())
    p_var, q_var = map(float, input().split())

    critical_points = []

    if a_var != 0:
        d_var = b_var**2 - 3 * a_var * c_var
        if d_var > 0:
            x1 = (-b_var + math.sqrt(d_var)) / (3 * a_var)
            x2 = (-b_var - math.sqrt(d_var)) / (3 * a_var)
            critical_points.extend([x1, x2])
        elif d_var == 0:
            x_var = -b_var / (3 * a_var)
            critical_points.append(x_var)
    elif b_var != 0:
        x_var = -c_var / (2 * b_var)
        critical_points.append(x_var)

    critical_points = [x for x in critical_points if p_var <= x <= q_var]

    if not critical_points:
        print("No critical points found.")
    else:
        results = []
        for x_var in critical_points:
            fxx = 6 * a_var * x_var + 2 * b_var
            if fxx > 0:
                kind = "Local minimum"
            elif fxx < 0:
                kind = "Local maximum"
            else:
                kind = "Saddle point"
            fx = a_var * x_var**3 + b_var * x_var**2 + c_var * x_var + d_var
            results.append((x_var, kind, fx))

        results.sort(key=lambda item: item[0])

        for x_var, kind, fx in results:
            print(f"{kind} at x_var = {x_var:.5f}")
            print(f"f(x_var) = {fx:.5f}")


if __name__ == "__main__":
    main_1()

# +
# 2


def main_2() -> None:
    """Find a root of a quadratic function using Newton's method."""
    a_smpl, b_smpl, c_smpl = map(float, input().split())
    x_smpl = float(input()) 
    epsilon = float(input())  

    max_iter = 1000
    iteration = 0

    while iteration < max_iter:
        fx = a_smpl * x_smpl**2 + b_smpl * x_smpl + c_smpl
        fpx = 2 * a_smpl * x_smpl + b_smpl  

        if abs(fpx) < 1e-12:  
            print("Solution not found")
            return

        x_new = x_smpl - fx / fpx
        iteration += 1

        if abs(a_smpl * x_new**2 + b_smpl * x_new + c_smpl) < epsilon:
            print(f"Root found: x = {x_new:.6f}")
            print(f"Number of iterations: {iteration}")
            return

        x_smpl = x_new

    print("Solution not found")


if __name__ == "__main__":
    main_2()
