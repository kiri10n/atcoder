def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [-1 for _ in range(n)]

    last_seen = {a[0]: 0}
    for i in range(1, n):
        if a[i] in last_seen:
            b[i] = last_seen[a[i]] + 1
        last_seen[a[i]] = i
    
    print(*b)

if __name__ == '__main__':
    main()