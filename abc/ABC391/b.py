def main():
    n, m = map(int, input().split())
    s = []
    t = []
    for i in range(n):
        s.append(input())
    for i in range(m):
        t.append(input())

    for i in range(n-m+1):
        for j in range(n-m+1):
            for k in range(m):
                if s[i+k][j:j+m] != t[k]:
                    break
            else:
                print(f"{i+1} {j+1}")

if __name__ == '__main__':
    main()