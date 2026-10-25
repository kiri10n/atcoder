def main():
    h, w = map(int, input().split())
    s_i, s_j = map(int, input().split())
    c = []
    for i in range(h):
        c_i = list(input())
        c.append(c_i)
    x = list(input())

    t_i = s_i - 1
    t_j = s_j - 1
    for char in x:
        if char == "L":
            if t_j - 1 >= 0:
                if c[t_i][t_j-1] == ".":
                    t_j -= 1
        elif char == "R":
            if t_j + 1 < w:
                if c[t_i][t_j+1] == ".":
                    t_j += 1
        elif char == "U":
            if t_i - 1 >= 0:
                if c[t_i-1][t_j] == ".":
                    t_i -= 1
        elif char == "D":
            if t_i + 1 < h:
                if c[t_i+1][t_j] == ".":
                    t_i += 1
    print(t_i+1, t_j+1)

if __name__ == '__main__':
    main()


