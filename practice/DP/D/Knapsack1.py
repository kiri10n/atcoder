# coding: utf-8

def main():
    n, w = map(int, input().split())
    wv = [list(map(int, input().split())) for i in range(n)]

    # dp[i][j]: i番目までの品物から重さがj以下になるように選んだ時の価値の最大値
    dp = [[0 for i in range(w+1)] for j in range(n+1)]

    for i in range(n):
        for j in range(w+1):
            if j >= wv[i][0]:
                dp[i+1][j] = max(dp[i][j-wv[i][0]] + wv[i][1], dp[i][j])
            else:
                dp[i+1][j] = dp[i][j]
        
    print(dp[n][w])

if __name__ == '__main__':
    main() 