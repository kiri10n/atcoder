def main():
    n = int(input())
    s = input()
    t = input()

    s = s + ".."
    t = t + ".."

    dp = [["" for _ in range(14)] for _ in range(2**n)]
    dp[0][0] = s

    for i in range(1, 2**n):
        for j in range(1, n):
            dp[i][j] = 
