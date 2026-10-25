def main():
    h, w, d = map(int, input().split())
    s = []

    floor = []
    for i in range(h):
        s.append(list(input()))
        for j in range(w):
            if s[i][j] == '.':
                floor.append((i, j))
    
    wet_floors = [[] for _ in range(len(floor))]
    for i in range(len(floor)):
        for j in range(len(floor)):
            if abs(floor[i][0] - floor[j][0]) + abs(floor[i][1] - floor[j][1]) <= d:
                wet_floors[i].append(floor[j])
    
    max_floors = 0
    for i in range(len(floor)):
        for j in range(len(floor)):
            if i == j:
                continue
            if len(set(wet_floors[i] + wet_floors[j])) > max_floors:
                max_floors = len(set(wet_floors[i] + wet_floors[j]))
    
    print(max_floors)

if __name__ == '__main__':
    main()
            

