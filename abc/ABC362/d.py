from collections import deque

# def dfs(graph, visited, target, a, v):
#     #visited[v] = True
#     min_weight = float('inf')
#     for u, b in graph[v]:
#         # if visited[u]:
#         #     continue
#         if u == target:
#             weight = a[v-1] + b + a[u-1]
#         else:
#             weight = a[v-1] + b + dfs(graph, visited, target, a, u)
#         if weight < min_weight:
#             min_weight = weight
#     return min_weight

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    graph = [[] for i in range(n+1)]
    d = [0 for _ in range(n+1)]
    for i in range(m):
        u, v, b = map(int, input().split())
        graph[u].append((v, b))
        graph[v].append((u, b))

    d[1] = 0
    q = deque()

    q.append(1)
    while q:
        v = q.popleft()
        for u, b in graph[v]:
            weight = a[v-1] + b + d[v]
            
    
    for i in range(2, n+1):

if __name__ == '__main__':
    main()
