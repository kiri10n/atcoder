def main():
    n, m, q = map(int, input().split())
    role = [[False for _ in range(m+1)] for _ in range(n)]
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            x, y = query[1], query[2]
            role[x - 1][y - 1] = True
        elif query[0] == 2:
            x = query[1]
            role[x - 1][m] = True
        elif query[0] == 3:
            x, y = query[1], query[2]
            print("Yes" if role[x - 1][y - 1] or role[x - 1][m] else "No")

if __name__ == "__main__":
    main()