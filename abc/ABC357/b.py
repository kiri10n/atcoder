
def main():
    s = input()

    num_lower = sum(map(str.islower, s))
    num_upper = sum(map(str.isupper, s))

    if num_upper > num_lower:
        print(s.upper())
    else:
        print(s.lower())
    return

if __name__ == '__main__':
    main()