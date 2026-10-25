n = int(input())

deck = []
for i in range(n):
    a, c = map(int, input().split())
    deck.append([a, c, i+1])

sorted_deck = sorted(deck, key=lambda x: x[0], reverse=True)
m = 0
i_list = []
for j in range(n-1):
    a, c, i = sorted_deck[j]
    for k in range(j+1, len(sorted_deck)):
        a_2, c_2, i_2 = sorted_deck[k]
        if c_2 > c:
            del sorted_deck[k]

print(len(sorted_deck))
i_list = [i for a,c,i in sorted_deck]
print(" ".join(map(str, sorted(i_list))))