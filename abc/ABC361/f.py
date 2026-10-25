import math

def main():
    n = int(input())

    ans = 0
    for i in [2, 3, 5, 7, 11, 13, 17]:
        ans += math.floor(math.pow(n, 1/i)) - 1
        print(f"i: {i}, math.pow(n, 1/i): {math.pow(n, 1/i)}, math.floor(math.pow(n, 1/i)): {math.floor(math.pow(n, 1/i))}")

    print(ans)

if __name__ == '__main__':
    main()