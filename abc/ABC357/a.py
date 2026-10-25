
def main():
    n, m = map(int, input().split())
    h = list(map(int, input().split()))

    for i in range(n):
        m -= h[i]
        if m < 0:
            print(i)
            return
    print(n)

if __name__ == '__main__':
    main()