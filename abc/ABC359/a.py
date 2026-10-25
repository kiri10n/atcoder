def main():
    n = int(input())
    count = 0
    for i in range(n):
        s = input()
        if s == "Takahashi":
            count += 1
    print(count)

if __name__ == '__main__':
    main()