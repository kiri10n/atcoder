def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    sorted_a = sorted(a)
    #diff_a = [sorted_a[i+1] - sorted_a[i] for i in range(n-1)]

    b_num = n-k
    pair_dist = b_num - 1

    min_dist = 2*10**9
    for i in range(n-pair_dist):
        if sorted_a[i+pair_dist] - sorted_a[i] < min_dist:
            min_dist = sorted_a[i+pair_dist] - sorted_a[i]
        #print(f"i {i}, pair_dist: {pair_dist}, min_dist: {min_dist}, sorted_a[i+pair_dist]: {sorted_a[i+pair_dist]}, sorteda[i]: {sorted_a[i]}")
        
    print(min_dist)

if __name__ == '__main__':
    main()