# encoding: utf-8
# https://atcoder.jp/contests/dp/tasks/dp_a

inf = 1e5

if __name__ == "__main__":
    n = int(input())
    h = list(map(int, input().split()))

    dp = [inf for i in range(n)]
    dp[0] = 0

    dp[1] = dp[0] + abs(h[0] - h[1])

    for i in range(2, n):
        dp[i] = min(dp[i-1] + abs(h[i-1] - h[i]), dp[i-2] + abs(h[i-2] - h[i]))
    
    print(dp[n-1])