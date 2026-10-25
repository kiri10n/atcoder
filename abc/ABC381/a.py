def main():
    n, d = map(int, input().split())
    s = input()

    num_at = s.count("@")
    print(n - num_at + d)

if __name__ == '__main__':
    main()