# encoding: utf-8
# https://atcoder.jp/contests/dp/tasks/dp_a

inf = int(1e6)

if __name__ == "__main__":
    n = int(input())
    h = list(map(int, input().split()))

    dp = [inf for i in range(n)]
    dp[0] = 0

    for i in range(0, n-1):
        dp[i+1] = min(dp[i+1], dp[i] + abs(h[i] - h[i+1]))
        if i < n-2:
            dp[i+2] = min(dp[i+2], dp[i] + abs(h[i] - h[i+2]))
        print(dp)
    
    print(dp[n-1])