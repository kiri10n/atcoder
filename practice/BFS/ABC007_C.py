from collections import deque

def bfs(field, visited, q, gy, gx):
    while q:
        y, x, count = q.popleft()
        if y == gy and x == gx:
            return count
        if visited[y][x] == 1 or field[y][x] == "#":
            continue

        visited[y][x] = 1

        q.append([y-1, x, count+1])
        q.append([y, x-1, count+1])
        q.append([y+1, x, count+1])
        q.append([y, x+1, count+1])

def main():
    r, c = map(int, input().split())
    sy, sx = map(int, input().split())
    gy, gx = map(int, input().split())

    field = []
    for i in range(r):
        row = input()
        field.append([s for s in row])

    visited = [[0 for i in range(c)] for j in range(r)]

    q = deque()
    q.append([sy-1, sx-1, 0])

    ans = bfs(field, visited, q, gy-1, gx-1)

    print(ans)


if __name__ == '__main__':
    main()