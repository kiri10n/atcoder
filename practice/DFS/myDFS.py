h, w = map(int, input().split())

field = []
for i in range(h):
    row = [s for s in input()]
    field.append(row)
    for j in range(w):
        if row[j] == "s":
            s = [i, j]

visited = [[0 for i in range(w)] for j in range(h)]

dir = [[-1, 0], [0, -1], [1, 0], [0, 1]]
#print(field)

def dfs(i, j):
    for d in dir:
        i_d = i + d[0]
        j_d = j + d[1]
        if 0 <= i_d and i_d < h and 0 <= j_d and j_d < w:
            if visited[i_d][j_d] == 1:
                continue
            else:
                visited[i_d][j_d] = 1
            if field[i_d][j_d] == "g":
                print("Yes")
                exit()
            elif field[i_d][j_d] == "#" or field[i_d][j_d] == "s":
                visited[i_d][j_d] = 1
            else:
                dfs(i_d, j_d)
    

visited[s[0]][s[1]] = 1
dfs(s[0], s[1])
print("No")

