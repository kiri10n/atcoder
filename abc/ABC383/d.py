import numpy as np

def main():
    n, m, sx, sy = map(int, input().split())
    poinrts = []
    for i in range(n):
        poinrts.append(list(map(int, input().split())))
    d = []
    c = []
    for i in range(m):
        d_i, c_i = map(int, input().split())
        d.append(d_i)
        c.append(c_i)
    
    x = sx
    y = sy

    houses = set()

    for i in range(m):
        if d[i] == "U":
            count = len([point for point in poinrts if point[0] == x and point[1] > y and point[1] <= y + c[i]])
            y = y + c[i]