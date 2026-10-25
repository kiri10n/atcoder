import itertools

def main():
    n, k = map(int, input().split())
    s = list(input())

    pattern = list(set(itertools.permutations(s)))

    num_not_palindrome = 0
    for p in pattern:
        for i in range(n - k + 1):
            sub_str = "".join(p[i:i + k])
            if sub_str == sub_str[::-1]:
                break
        else:
            num_not_palindrome += 1
    
    print(num_not_palindrome)

if __name__ == '__main__':
    main()

