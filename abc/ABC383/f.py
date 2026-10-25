def main():
    n = int(input())
    xh = []
    for i in range(n):
        x, h = map(int, input().split())
        xh.append((x, h))
    
    sections = []
    if n == 1:
        print(-1)
        return
    for i in range(n-1):
        x_i, h_i = xh[i]
        x_i_next, h_i_next = xh[i+1]
        if x_i == x_i_next:
            b = max(h_i, h_i_next)
        elif h_i == h_i_next:
            b = h_i
        else:
            b = (h_i * x_i_next - x_i * h_i_next) / (x_i_next - x_i)
        sections.append(b)
    
    max_b = max(sections)
    if max_b < 0:
        print(-1)
    else:
        print(max_b)

if __name__ == '__main__':
    main()