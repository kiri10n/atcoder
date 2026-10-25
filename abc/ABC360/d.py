def main():
    n, t = map(int, input().split())
    s = list(input())
    x = list(map(int, input().split()))

    collision = 0
    for i in range(n):
        if s[i] == "1":
            for j in range(i, n):
                if s[j] == "0":
                    if x[i] + t >= x[j] - t:
                        collision += 1
        else:
            for j in range(i, n):
                if s[j] == "1":
                    if x[j] + t <= x[i] - t:
                        collision += 1
        #print(f"i: {i}, collision: {collision}")
    print(collision)

if __name__ == '__main__':
    main()