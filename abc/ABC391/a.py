def main():
    d = input()
    if d == "N":
        print("S")
    elif d == "S":
        print("N")
    elif d == "W":
        print("E")
    elif d == "E":
        print("W")
    elif d == "NE":
        print("SW")
    elif d == "NW":
        print("SE")
    elif d == "SE":
        print("NW")
    elif d == "SW":
        print("NE")

if __name__ == '__main__':
    main()