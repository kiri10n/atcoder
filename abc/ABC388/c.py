def binary_search(a, v):
    left = 0
    right = len(a) - 1
    while left < right:
        middle_i = (left + right) // 2
        middle_v = a[middle_i]

        if middle_v < v:
            left = middle_i + 1
        else:
            right = middle_i

    if a[left] < v:
        return left + 1
    else:
        return left
    

def main():
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        top = a[i]
        left = binary_search(a, 2*top)
        # print(f"top: {top}, left: {left}")
        ans += n - left
    print(ans)

if __name__ == '__main__':
    main()