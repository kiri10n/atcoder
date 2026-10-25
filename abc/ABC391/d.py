def main():
    n, w = map(int, input().split())
    points = [[] for i in range(w)]
    points_xy = []
    for i in range(n):
        x, y = map(int, input().split())
        points[x-1].append(y)
        points_xy.append((x, y))
    
    q = int(input())
    for i in range(q):
        t, a = map(int, input().split())
        l -= 1
        r -= 1
        ans = 0
        for j in range(l, r):
            if points[j]:
                ans += max(points[j]) - min(points[j])
        print(ans)
        