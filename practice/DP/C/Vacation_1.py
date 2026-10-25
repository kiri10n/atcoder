n = int(input())

dp = [[0, 0, 0] for i in range(n)]

h = list(map(int, input().split())) 
dp[0][0] = h[0]
dp[0][1] = h[1]
dp[0][2] = h[2]

for i in range(1, n):
    h = list(map(int, input().split()))
    for j in range(3):
        dp[i][j] = h[j] + max([dp[i-1][k] for k in range(3) if j!=k])
    
print(max(dp[n-1]))