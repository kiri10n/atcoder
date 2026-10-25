def main():
    ans=0
    for i in range(12):
        s = input()
        if len(s) == i+1:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
