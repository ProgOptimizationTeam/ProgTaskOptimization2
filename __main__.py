import numpy as np
from numpy.linalg import norm


def InteriorPointAlgorithm(x: np.array, A: np.array, c: np.array, alpha):
    i = 1
    while True:
        v = x
        D = np.diag(x)
        AA = np.dot(A, D)
        cc = np.dot(D, c)
        I = np.eye(4)
        F = np.dot(AA, np.transpose(AA))
        FI = np.linalg.inv(F)
        H = np.dot(np.transpose(AA), FI)
        P = np.subtract(I, np.dot(H, AA))
        cp = np.dot(P, cc)
        nu = np.absolute(np.min(cp))
        y = np.add(np.ones(4, float), (alpha / nu) * cp)
        yy = np.dot(D, y)
        x = yy
        if i == 1 or i == 2 or i == 3 or i == 4:
            print(f"In iteration {i}, we have {x=}")
            i = i + 1
        if norm(np.subtract(yy, v), ord=2) < 0.00001:
            break
    print(f"In the last iteration {i}, we have {x=}")


if __name__ == '__main__':
    InteriorPointAlgorithm(
        x = np.array([2, 2, 4, 3], float),
        A = np.array([[2, -2, 8, 0], [-6, -1, 0, -1]], float),
        c = np.array([-2, 3, 0, 0], float),
        alpha = 0.5
    )