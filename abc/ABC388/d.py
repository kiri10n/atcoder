import numpy as np

def main():
    n = int(input())
    a = list(map(int, input().split()))

    b = []

    for i in range(n):
        last_year_b = b.copy()
        last_year_b = np.array(last_year_b)
        for j in range(i):
            last_year_b[j] = max(last_year_b[j] + j - i + 1, 0)
        b.append(a[i] + np.count_nonzero(last_year_b))
    
    ans = b.copy()
    for i in range(n):
        ans[i] = max(ans[i] - n + i + 1, 0)
    
    print(*ans)

if __name__ == '__main__':
    main()
