# encoding: utf-8
# https://atcoder.jp/contests/dp/tasks/dp_a

inf = 1e5

if __name__ == "__main__":
    n = int(input())
    h = list(map(int, input().split()))

    present = 0
    prev = 0
    prev_prev = 0

    # i = 1
    present = prev + abs(h[0] - h[1])
    prev = present

    for i in range(2, n):
        present = min(prev + abs(h[i-1] - h[i]), prev_prev + abs(h[i-2] - h[i]))
        prev_prev = prev
        prev = present
    
    print(present)