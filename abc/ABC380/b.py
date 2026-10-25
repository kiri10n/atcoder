def main():
    s = input()
    splitted = s.split("|")
    del splitted[0]
    del splitted[-1]
    for part in splitted:
        print(len(part), end=" ")
    print()

if __name__ == '__main__':
    main()