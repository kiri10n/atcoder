import sys
# set recursion limit up
sys.setrecursionlimit(1000000)

h, w = map(int, input().split())

field = []
for i in range(h):
    row = [s for s in input()]
    field.append(row)
    for j in range(w):
        if row[j] == "s":
            s = [i, j]

visited = [[0 for i in range(w)] for j in range(h)]

def dfs(i, j):
    if i < 0 or h <= i or j < 0 or w <= j:
        return
    if visited[i][j] == 1:
        return
    if field[i][j] == "g":
        print("Yes")
        exit()
    if field[i][j] == "#":
        return
    
    visited[i][j] = 1

    dfs(i-1, j)
    dfs(i, j-1)
    dfs(i+1, j)
    dfs(i, j+1)
    
dfs(s[0], s[1])
print("No")

