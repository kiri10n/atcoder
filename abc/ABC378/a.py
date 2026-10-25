from collections import Counter
def main():
    a1, a2, a3, a4 = map(int, input().split())
    a = [a1, a2, a3, a4]
    print(sum(v // 2 for v in Counter(a).values()))
    

if __name__ == '__main__':
    main()

