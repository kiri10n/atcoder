def main():
    s, t = input().split()

    for w in range(1, len(s)):
        for c in range(1, w+1):
            sub = []
            for i in range(c-1, len(s), w):
                sub.append(s[i])
            #print(f"w: {w}, c: {c}, sub: {sub}")
            if "".join(sub) == t:
                print("Yes")
                return
    print("No")

if __name__ == '__main__':
    main()