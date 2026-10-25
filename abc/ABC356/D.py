
def main():
    n, m = map(int, input().split())

    bin_m = format(m, 'b')
    m_digits = len(bin_m)

    loop = [0 for _ in range(2**(m_digits))]
    for i in range(len(loop)):
        loop[i] = (i & m).bit_count()

    loop_num = (n+1) // len(loop)
    mod = (n+1) % len(loop)

    if mod == 0:
        ans = sum(loop) * loop_num
    elif mod == 1:
        ans = loop[0] * (loop_num+1) + sum(loop[1:]) * loop_num
    else:
        ans = sum(loop[:mod]) * (loop_num + 1) + sum(loop[mod:]) * loop_num
    print(ans)

if __name__ == '__main__':
    main()
