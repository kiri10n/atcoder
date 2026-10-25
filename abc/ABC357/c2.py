def main():
    n = int(input())

    if n == 0:
        print("#")
        return

    array = [["" for _ in range(730)] for _ in range(730)]
    array[0][0] = "#"
    for depth in range(1, n+1):
        row_len = 3 ** depth
        for i in range(3):
            for j in range(3):
                if i == 0 and j == 0:
                    continue
                if i == 1 and j == 1:
                    for k in range(row_len//3):
                        for l in range(row_len//3):
                            array[i*(row_len//3)+k][j*(row_len//3)+l] = "."
                else:
                    for k in range(row_len//3):
                        for l in range(row_len//3):
                            array[i*(row_len//3)+k][j*(row_len//3)+l] = array[k][l]
    print("\n".join("".join(array[i]) for i in range(3**n)))

if __name__ == '__main__':
    main()