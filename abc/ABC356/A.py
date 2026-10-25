
def main():
    n, l, r = map(int, input().split())
    a = [i for i in range(1, n+1)]

    reverse_a = sorted(a[l-1:r], reverse=True)
    #print(reverse_a)

    print(" ".join(map(str, a[:l-1] + reverse_a + a[r:])))

if __name__ == '__main__':
    main()