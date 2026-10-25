def main():
    n, a = map(int, input().split())
    t = list(map(int, input().split()))

    prev = 0
    for i in t:
        if i < prev:
            print(prev + a)
            prev = prev + a
        else:
            print(i + a)
            prev = i + a

if __name__ == '__main__':
    main()
