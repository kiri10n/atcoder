def main():
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a_sorted = sorted(a, reverse=True)
    b_sorted = sorted(b, reverse=True)

    a_sum_until_i = 0
    for i in range(n):
        a_sum_until_i += a_sorted[i]
        if a_sum_until_i > x:
            a_ans = i+1
            break
    else:
        a_ans = n
    
    b_sum_until_i = 0
    for i in range(n):
        b_sum_until_i += b_sorted[i]
        if b_sum_until_i > y:
            b_ans = i+1
            break
    else:
        b_ans = n
    
    print(min(a_ans, b_ans))

if __name__ == '__main__':
    main()