import math

def main():
    n = int(input())
    dist = 0
    prev_x = 0
    prev_y = 0
    for i in range(n):
        x, y = map(int, input().split())
        dist += math.sqrt((x-prev_x)**2 + (y-prev_y)**2)
        prev_x = x
        prev_y = y
    dist += math.sqrt((prev_x)**2 + (prev_y)**2)
    print(dist)

        

if __name__ == '__main__':
    main()