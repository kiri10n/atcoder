import itertools

def main():
    n, m, k = map(int, input().split())

    correct_keys = set()
    for i in range(m):
        row = list(input().split())
        c = int(row[0])
        a = list(map(int, row[1:-1]))
        r = row[-1]

        remove_keys = set()
        if r == "o":
            correct_keys.add(itertools.combinations(a, k))
        else:
            if c >= k:
                for pair in itertools.combinations(a, k-1):
                    for correct in correct_keys:
                        if not (set(pair) <= set(correct)):
                            remove_keys.add(correct)
        for correct in remove_keys:
            correct_keys.remove(correct)

    print(len(correct_keys))

if __name__ == '__main__':
    main()