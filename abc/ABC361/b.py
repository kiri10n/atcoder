def main():
    a, b, c, d, e, f = map(int, input().split())
    g, h, i, j, k, l = map(int, input().split())

    if a < j and g < d and b < k and h < e and c < l and i < f:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()