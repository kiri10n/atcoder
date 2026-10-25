import math

def horizontal_cost(tx, sx, y):
    if (sx + y) % 2 == 0:
        if tx > sx:
            return math.floor(abs(tx - sx) / 2)
        else:
            return math.ceil(abs(tx - sx) / 2)
    else:
        if tx > sx:
            return math.ceil(abs(tx - sx) / 2)
        else:
            return math.floor(abs(tx - sx) / 2)

def main():
    sx, sy = map(int, input().split())
    tx, ty = map(int, input().split())

    x_dist = abs(tx - sx)
    y_dist = abs(ty - sy)

    ans = 0
    if x_dist <= y_dist:
        ans = y_dist
    else:
        if tx > sx:
            ans = y_dist + horizontal_cost(tx, sx + y_dist, ty)
        else:
            ans = y_dist + horizontal_cost(tx, sx - y_dist, ty)
    print(ans)

if __name__ == '__main__':
    main()