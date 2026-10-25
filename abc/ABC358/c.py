def main():
    n, m = map(int, input().split())

    s = []
    for i in range(n):
        row = input()
        row = row.replace('o', '1')
        row = row.replace('x', '0')
        s.append(int(row, 2))
    
    ans = 11
    for i in range(2**n):
        pattern = i
        binary = 0
        for j in range(n):
            if pattern % 2 == 1:
                binary |= s[j]
            pattern //= 2
        if binary == (2**m)-1:
            if ans > i.bit_count():
                ans = i.bit_count()
    print(ans)

if __name__ == '__main__':
    main()