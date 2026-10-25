def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    a_mod = [ai % m for ai in a]

    print(sum(a_mod) * n * (n + 1) // 2)

if __name__ == '__main__':
    main()