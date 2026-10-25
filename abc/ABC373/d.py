import numpy as np
from sympy import Matrix, symbols, Eq, solve
from sympy.solvers.diophantine import diophantine

def main():
    n, m = map(int, input().split())
    A = []
    b = [0 for _ in range(m)]
    for i in range(m):
        u, v, w = map(int, input().split())
        row = [0 for _ in range(n)]
        row[u-1] = -1
        row[v-1] = 1
        A.append(row)
        b[i] = w
    A = Matrix(A)
    b = Matrix(b)
    print(A)
    print(b)

    x = symbols('x1:{0}'.format(n+1), integer=True)
    equations = [Eq(A[i, :]*Matrix(x), b[i]) for i in range(n)]
    solution = diophantine(equations)
    # x = np.linalg.lstsq(A, b, rcond=None)
    print(solution)

    # x = np.round(x).astype(int)

    # print(*x)

if __name__ == '__main__':
    main()