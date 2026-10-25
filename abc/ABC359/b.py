def main():
    n = int(input())
    a = list(map(int, input().split()))

    count = 0
    for i in range(2, 2*n):
        if a[i] == a[i-2]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()