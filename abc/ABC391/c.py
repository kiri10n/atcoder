from collections import Counter

def main():
    n, q = map(int, input().split())
    boxes = [i for i in range(1, n+1)]
    count = [1 for i in range(1, n+1)]

    num_overlap = 0
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            p = query[1]
            h = query[2]
            count[boxes[p-1]-1] -= 1
            if count[boxes[p-1]-1] == 1:
                num_overlap -= 1
            boxes[p-1] = h
            count[h-1] += 1
            if count[h-1] == 2:
                num_overlap += 1
        elif query[0] == 2:
            # c = Counter(boxes)
            # c = c.most_common()
            # count = 0
            # for j in range(len(c)):
            #     if c[j][1] > 1:
            #         count += 1
            #     else:
            #         break
            # print(f"boxes: {boxes}, c: {c}")
            # print(count)
            # print(f"boxes: {boxes}, set(boxes): {set(boxes)}")
            print(num_overlap)

if __name__ == '__main__':
    main()
            