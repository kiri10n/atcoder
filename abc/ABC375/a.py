def main():
    n = int(input())
    s = input()

    sum=0
    for i in range(n-2):
        if s[i] == "#" and s[i+1] == "." and s[i+2] == "#":
            sum += 1

    print(sum)

if __name__ == '__main__':
    main()