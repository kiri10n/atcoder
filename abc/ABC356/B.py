
def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    today = [0 for _ in range(m)]

    for i in range(n):
        food_i = list(map(int, input().split()))
        for j in range(m):
            today[j] += food_i[j]
    
    if all([today[j] >= a[j] for j in range(m)]):
        print("Yes")
    else:    
        print("No")

if __name__ == '__main__':
    main()
