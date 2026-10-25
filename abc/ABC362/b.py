def main():
    x_a, y_a = map(int, input().split())
    x_b, y_b = map(int, input().split())
    x_c, y_c = map(int, input().split())

    if (x_b - x_a) * (x_c - x_b) + (y_b - y_a) * (y_c - y_b) == 0 \
        or (x_c - x_b) * (x_a - x_c) + (y_c - y_b) * (y_a - y_c) == 0 \
        or (x_a - x_c) * (x_b - x_a) + (y_a - y_c) * (y_b - y_a) == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()