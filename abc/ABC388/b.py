def main():
    n, d = map(int, input().split())
    tl = []
    for i in range(n):
        t_i, l_i = map(int, input().split())
        tl.append((t_i, l_i))
    
    for d_i in range(1, d+1):
        max_w = 0
        for i in range(n):
            t_i, l_i = tl[i]
            w = t_i * (l_i + d_i)
            if w > max_w:
                max_w = w
        print(max_w)

if __name__ == '__main__':
    main()