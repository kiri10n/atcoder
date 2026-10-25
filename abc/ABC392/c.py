def main():
    n, m = map(int, input().split())
    graph = [[] for i in range(n)]
    for i in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
    
    num_self_loop = 0
    num_multi_edge = 0
    for i in range(n):
        for v in graph[i]:
            if i == v:
                num_self_loop += 1
            elif graph[v].count(i) > 0:
                num_multi_edge += 1