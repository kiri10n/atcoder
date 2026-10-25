def main():
    n, k = map(int, input().split())
    s = input()

    # blocks = []
    # prev = None
    # for i in range(n):
    #     if s[i] == "1":
    #         if prev == "1":
    #             blocks[-1] += "1"
    #         else:
    #             blocks.append("1")
    #     else:
    #         if prev == "0":
    #             blocks[-1] += "0"
    #         else:
    #             blocks.append("0")
                
    #     prev = s[i]
    
    
    # index_of_kth_ones = 2*k-1 if s[0] == "0" else 2*k-2
    # blocks[index_of_kth_ones - 1], blocks[index_of_kth_ones] = blocks[index_of_kth_ones], blocks[index_of_kth_ones - 1]
    # ans = "".join(blocks)

    one_blocks_i = 0
    in_ones = False
    index_of_kth_ones_end = len(s)
    prev = None
    for i in range(n):
        if s[i] == "1" and prev != "1":
            one_blocks_i += 1
            if one_blocks_i == k:
                index_of_kth_ones = i
                in_ones = True
        
        if in_ones and s[i] != "1":
            index_of_kth_ones_end = i
            break
        
        if in_ones == False and s[i] == "0" and prev != "0":
            index_of_prev_zeros = i
        prev = s[i]

    # print(f"index_of_kth_ones: {index_of_kth_ones}")
    # print(f"index_of_kth_ones_end: {index_of_kth_ones_end}")
    # print(f"index_of_prev_zeros: {index_of_prev_zeros}")
    # print(f"{s[:index_of_prev_zeros]} {s[index_of_kth_ones:index_of_kth_ones_end]} {s[index_of_prev_zeros:index_of_kth_ones]} {s[index_of_kth_ones_end:]}")
    ans = s[:index_of_prev_zeros] + s[index_of_kth_ones:index_of_kth_ones_end] + s[index_of_prev_zeros:index_of_kth_ones] + s[index_of_kth_ones_end:]

    print(ans)

if __name__ == '__main__':
    main()
    

