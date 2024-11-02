import math

from numpy.typing import NDArray
import numpy as np
from numpy.linalg import norm

from Simplex import solve


def interior_point_algorithm(x: NDArray, A: NDArray, c: NDArray, b: NDArray, alpha, acc=2):
    for i, constraint in enumerate(A):
        if np.sum(x.dot(constraint)) != b[i]:
            print("The method is not applicable!")
            return
    i = 1
    while True:
        try:
            v = x
            D = np.diag(x)

            AA = np.dot(A, D)
            cc = np.dot(D, c)
            I = np.eye(len(c))
            F = np.dot(AA, np.transpose(AA))
            FI = np.linalg.inv(F)
            H = np.dot(np.transpose(AA), FI)
            P = np.subtract(I, np.dot(H, AA))
            cp = np.dot(P, cc)
            nu = np.absolute(np.min(cp))
            y = np.add(np.ones(len(c), float), (alpha / nu) * cp)
            yy = np.dot(D, y)

            x = yy

            if norm(np.subtract(yy, v), ord=2) < 0.00001:
                break
            # print(f"In iteration {i}, {alpha=} we have:")
            # for j in x:
            #     print(round(j, acc), end=' ')
            # print()
            i = i + 1
        except:
            break
    for j in range(len(x)):
        x[j] = round(x[j], acc)
    print(f"In the last iteration {i}, {alpha=}, we have x:")
    for j in x:
        print(round(j, acc), end=' ')
    print()


def main():
    c = list(map(float, input("A vector of coefficients of objective function with slack variables- C: ").split()))
    nA = int(input("A number of constraint functions: "))
    A = []
    print("A matrix of coefficients of constraint function with slack variables - A:")
    for i in range(nA):
        A += [list(map(float, input(f"{i + 1}: ").split()))]
    b = list(map(float, input("A vector of right-hand side numbers - b: ").split()))
    # • Set your initial starting point (manually, or generated by program).
    x = list(map(float, input("init point: ").split()))
    acc = int(input("Accuracy: "))

    x_np = np.array(x, float)
    A_np = np.array(A, float)
    c_np = np.array(c, float)
    b_np = np.array(b, float)

    interior_point_algorithm(
        x=x_np,
        A=A_np,
        c=c_np,
        b=b_np,
        acc=acc,
        alpha=0.5
    )
    interior_point_algorithm(
        x=x_np,
        A=A_np,
        c=c_np,
        b=b_np,
        acc=acc,
        alpha=0.9
    )
    print("Simplex:")
    solve(objective_function=c, constraint_functions=A, right_hand_side=b, accuracy=acc)


if __name__ == '__main__':
    main()
    # interior_point_algorithm(
    #     x=np.array([2, 2, 4, 3], float),
    #     A=np.array([[2, -2, 8, 0], [-6, -1, 0, -1]], float),
    #     c=np.array([-2, 3, 0, 0], float),
    #     alpha=0.5
    # )

# 1 1 0 0
# 2
# 2 -2 8 0
# -6 -1 0 -1
# -2 3 0 0
# 2 2 4 3
# 2

# [2, 2, 4, 3] [[2, -2, 8, 0], [-6, -1, 0, -1]] [-2, 3, 0, 0]
