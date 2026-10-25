


def main():
    h, w, k = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    # visited = [[False for _ in range(w)] for _ in range(h)]
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def dfs(x, y, length):
        # x, y: 現在地
        # length: 現在までの経路の長さ
        # Returns: 経路の数
        if length == k:
            return 1
        
        # 一時的に現在のマスを壁にして、同じ場所を通らないようにする
        temp = s[x][y]
        s[x][y] = '#'

        paths = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
            if 0 <= nx < h and 0 <= ny < w:
                if s[nx][ny] == '#':
                    continue
                paths += dfs(nx, ny, length + 1)

        # マスを元に戻す
        s[x][y] = temp
        
        return paths
    
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                continue
            ans += dfs(i, j, 0)
    print(ans)

if __name__ == '__main__':
    main()


        