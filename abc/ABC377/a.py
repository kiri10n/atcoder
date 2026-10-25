def main():
    s = input()
    if s == "ABC" or s == "ACB" or s == "BAC" or s == "BCA" or s == "CAB" or s == "CBA":
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()