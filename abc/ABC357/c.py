import pprint

def fractal(depth):
    if depth == 0:
        return ["#"]
    elif depth == 1:
        return ["###", "#.#", "###"]
    
    array = [[0 for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                array[i][j] = ["."*(3**(depth-1)) for _ in range(3**(depth-1))]
            else:
                array[i][j] = fractal(depth-1)
    return array

def main():
    n = int(input())

    ans = fractal(n)
    for k in range(3):
        for j in range(3):
            for i in range(3):
                print(ans[k][i][j], end="")
            print()



if __name__ == '__main__':
    main()