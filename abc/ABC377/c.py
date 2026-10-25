def main():
    n, m = map(int, input().split())

    occupied_squares = set()
    knights = []
    for i in range(m):
        a, b = map(int, input().split())
        knights.append((a, b))
        occupied_squares.add((a, b))
    
    # ナイトの移動パターン（x, y）
    moves = [
        (-2, -1), (-2, 1),
        (-1, -2), (-1, 2),
        (1, -2), (1, 2),
        (2, -1), (2, 1)
    ]

    
    for knight in knights:
        x, y = knight
        for dx, dy in moves:
            nx = x + dx
            ny = y + dy
            if 1 <= nx <= n and 1 <= ny <= n:
                occupied_squares.add((nx, ny))
    
    print(n**2 - len(occupied_squares))

if __name__ == '__main__':
    main()