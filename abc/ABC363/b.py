def main():
    n, t, p = map(int, input().split())
    l = list(map(int, input().split()))

    for i in range(150):
        num_over_t = sum([1 for l_i in l if l_i >= t])
        if num_over_t >= p:
            print(i)
            return
        l = [l_i + 1 for l_i in l]

if __name__ == '__main__':
    main()
