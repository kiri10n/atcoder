def main():
    n, d = map(int, input().split())
    s = input()

    num_at = s.count("@")

    ans_str = ""
    num_added_at = 0
    for i in range(n-1, -1, -1):
        if s[i] == "@":
            if num_added_at < d:
                ans_str = "." + ans_str
                num_added_at += 1
            else:
                ans_str = "@" + ans_str
        else:
            ans_str = "." + ans_str
    
    print(ans_str)

if __name__ == '__main__':
    main()