import math
def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def main():
    n, m = map(int, input().split())
    s = input()

    for k in range(n):
        comb(m, m - len(s) + 1) * 26 ** (m - len(s))