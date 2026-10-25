def main():
    s = input()
    l = []
    for c in s:
        l.append(c)
    
    if l.index("M") > l.index("R"):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

    