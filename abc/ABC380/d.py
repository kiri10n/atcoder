def same_as_0(block_i):
    if block_i == 0:
        return True
    if block_i == 1:
        return False
    
    # blocks_iを超えない最大の２の累乗
    max_power_of_2 = 1
    while max_power_of_2 <= block_i:
        max_power_of_2 *= 2
    max_power_of_2 //= 2
    return same_as_0(block_i - max_power_of_2)

def main():
    s = input()
    q = int(input())
    k = list(map(int, input().split()))

    for i in range(q):
        k_i = k[i]
        block_i = (k_i - 1) // len(s)

        if same_as_0(block_i):
            block = s
        else:
            block = s.swapcase()
        
        # print(f"i: {i}, block_i: {block_i}, block: {block}")
        print(block[(k_i - 1) % len(s)], end=" ")
    print()

if __name__ == '__main__':
    main()

        