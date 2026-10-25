from collections import Counter

def main():
    n = int(input())
    a = list(map(int, input().split()))
    w = list(map(int, input().split()))

    weights = [[] for _ in range(n)]
    for i in range(n):
        weights[a[i]-1].append(w[i])
    #print(f"weights: {weights}")
    
    ans = 0
    for i in range(n):
        if len(weights[i]) > 1:
            ans += sum(sorted(weights[i])[:-1])
    print(ans)

    # ans = 0
    # overlap = [k for k, v in Counter(a).items() if v > 1]
    # #print(f"overlap: {overlap}")
    # for box_i in overlap:
    #     overlap_weights = [w[i] for i, x in enumerate(a) if x == box_i]
    #     #print(f"overlap_weights: {overlap_weights}")
    #     ans += sum(sorted(overlap_weights)[:-1])
    # print(ans)

if __name__ == '__main__':
    main()