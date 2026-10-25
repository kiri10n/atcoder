# encoding: utf-8
# https://atcoder.jp/contests/dp/tasks/dp_a

import sys
sys.setrecursionlimit(10**7)

inf = int(1e6)

if __name__ == "__main__":
    n = int(input())
    h = list(map(int, input().split()))

    dp = [inf for i in range(n)]

    def cost(i):
        if i == 0:
            return 0
        elif i == 1:
            return abs(h[0] - h[1])
        elif dp[i] < inf:
            return dp[i]
        
        cost_i = min(cost(i-1) + abs(h[i-1] - h[i]), cost(i-2) + abs(h[i-2] - h[i]))
        dp[i] = cost_i
        return cost_i

    print(cost(n-1))