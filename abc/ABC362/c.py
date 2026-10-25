def main():
    n = int(input())
    l = []
    r = []
    l_sum = 0
    r_sum = 0
    for i in range(n):
        l_i, r_i = map(int, input().split())
        l.append(l_i)
        r.append(r_i)
        l_sum += l_i
        r_sum += r_i
    
    if l_sum <= 0 and 0 <= r_sum:
        print("Yes")
    else:
        print("No")
        exit()

    diff = -l_sum
    for i in range(n):
        if r[i] - l[i] <= diff:
            print(f"{r[i]} ", end="")
            diff -= r[i] - l[i]
        else:
            print(f"{l[i] + diff} ", end="")
            diff = 0

    
if __name__ == '__main__':
    main()