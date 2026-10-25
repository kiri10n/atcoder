import re
import itertools

def main():
    s = input()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # num = 0
    # for char in alphabet:
    #     matches = re.finditer(char, s)
    #     matches = [match.start() for match in matches]

    # for i in range(len(s)-2):
    #     sub = s[i+1:]
    #     matches = re.finditer(s[i], sub)
    #     for match in matches:
    #         num += match.start()
    # print(num)

    total_distance = 0
    # 'A'から'Z'までのアルファベットを順に探索
    for ch in range(ord('A'), ord('Z') + 1):
        char = chr(ch)
        positions = [i for i, c in enumerate(s) if c == char]  # 文字の出現位置をリストに格納

        # 出現位置が複数ある場合、位置の間の距離を合計
        # if len(positions) > 1:
        #     for pos1, pos2 in itertools.combinations(positions, 2):
        #         total_distance += abs(pos2 - pos1 - 1)
        if len(positions) > 1:
            sum_pos = sum(positions)
            prefix_sum = 0

            for i, pos in enumerate(positions):
                # i個目までの累積和を prefix_sum に保存
                total_distance += (pos * i - prefix_sum) - i  # 距離 - 1 を加算
                prefix_sum += pos
    print(total_distance)

if __name__ == '__main__':
    main()