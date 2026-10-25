def main():
    a, b, c = map(int, input().split())

    if a == b + c:
        print("Yes")
    elif b == a + c:
        print("Yes")
    elif c == a + b:
        print("Yes")
    elif a == b and b == c:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()