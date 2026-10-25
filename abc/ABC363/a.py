def main():
    r = int(input())

    if 1 <= r and r <= 99:
        print(100 - r)
    elif 100 <= r and r <= 199:
        print(200 - r)
    elif 200 <= r and r <= 299:
        print(300 - r)

if __name__ == '__main__':
    main()