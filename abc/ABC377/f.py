def main():
    n, m = map(int, input().split())

    occupied_squares = set()
    queens = []
    for i in range(m):
        a, b = map(int, input().split())
        queens.append((a, b))
        occupied_squares.add((a, b))
    
    # クイーンの移動方向（x, y）
    directions = [
        (-1, 0), (1, 0),   # 縦方向
        (0, -1), (0, 1),   # 横方向
        (-1, -1), (1, 1),  # 左上↔右下の対角線
        (-1, 1), (1, -1)   # 右上↔左下の対角線
    ]

    # 各クイーンの影響範囲を計算
    for queen in queens:
        x, y = queen
        for dx, dy in directions:
            nx, ny = x, y
            # チェス盤の端にぶつかるまで現在の方向に進む
            while 1 <= nx <= n and 1 <= ny <= n:
                occupied_squares.add((nx, ny))
                nx += dx
                ny += dy
    
    # 占領されていないマスの数を計算
    print(n**2 - len(occupied_squares))

if __name__ == '__main__':
    main()
