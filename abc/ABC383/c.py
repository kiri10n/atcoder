import collections

def max_consecutive(l):
    max_count = 0
    count = 0

    prev = None
    for i in range(len(l)):
        if prev == l[i]:
            count += 1
        else:
            count = 1
        prev = l[i]
        if count > max_count:
            max_count = count
    
    return max_count



def main():
    n = int(input())
    h = list(map(int, input().split()))

    max_count = 1
    for interval in range(1, n):
        for mod in range(interval):
            buildings = h[mod::interval]
            count = max_consecutive(buildings)
            # c = collections.Counter(buildings)
            # count = c.most_common()[0][1]
            if count > max_count:
                max_count = count
            # print(interval, mod, buildings, count)
    
    print(max_count)

if __name__ == '__main__':
    main()
