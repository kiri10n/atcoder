def main():
    h, w, x_start, y_start = map(int, input().split())
    s = []
    for i in range(h):
        s.append(list(input()))
    t = input()

    x = x_start
    y = y_start
    houses = set()

    if s[x-1][y-1] == "@":
        houses.add((x, y))
    
    for char in t:
        if char == "U":
            next_x = x - 1
            next_y = y
        elif char == "D":
            next_x = x + 1
            next_y = y
        elif char == "L":
            next_x = x
            next_y = y - 1
        elif char == "R":
            next_x = x
            next_y = y + 1
        
        if next_x < 0 or next_x >= h or next_y < 0 or next_y >= w:
            next_x = x
            next_y = y
        if s[next_x-1][next_y-1] == "#":
            next_x = x
            next_y = y
        
        x = next_x
        y = next_y

        if s[x-1][y-1] == "@":
            houses.add((x, y))
    
    print(f"{x} {y} {len(houses)}")

if __name__ == '__main__':
    main()