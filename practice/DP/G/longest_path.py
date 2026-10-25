import sys
sys.setrecursionlimit(10**7)

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
    
    dp = [-1 for _ in range(n+1)]

    def rec(v):
        if dp[v] != -1:
            return dp[v]
        
        res = 0
        if graph[v]:
            for u in graph[v]:
                res = max(res, rec(u)+1)
        dp[v] = res
        return res
    
    res = 0
    for i in range(1, n+1):
        res = max(res, rec(i))

    print(res)

if __name__ == '__main__':
    main()