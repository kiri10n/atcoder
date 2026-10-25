def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())

    for i in range(n-2):
        if s[i] == "sweet" and s[i+1] == "sweet":
            print("No")
            return

    print("Yes")

if __name__ == '__main__':
    main()
    
