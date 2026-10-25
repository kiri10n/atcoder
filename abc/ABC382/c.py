def dfs(i, j, h, w, d, dist, s, wet_floors, visited):
    if i < 0 or i >= h or j < 0 or j >= w:
        return
    if s[i][j] == '#':
        return
    if dist > d:
        return
    if visited[i][j]:
        return
    

    wet_floors.add((i, j))
    visited[i][j] = True
    dist += 1
    dfs(i-1, j, h, w, d, dist, s, wet_floors, visited)
    dfs(i+1, j, h, w, d, dist, s, wet_floors, visited)
    dfs(i, j-1, h, w, d, dist, s, wet_floors, visited)
    dfs(i, j+1, h, w, d, dist, s, wet_floors, visited)

def main():
    h, w, d = map(int, input().split())

    start = []
    s = []
    for i in range(h):
        s.append(list(input()))
        for j in range(w):
            if s[i][j] == 'H':
                start.append((i, j))
    
    wet_floors = set()
    for humidifier in start:
        i, j = humidifier
        visited = [[False for _ in range(w)] for _ in range(h)]
        dfs(i, j, h, w, d, 0, s, wet_floors, visited)

    print(len(wet_floors))

if __name__ == '__main__':
    main()


    