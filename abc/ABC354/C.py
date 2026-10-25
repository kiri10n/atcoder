n = int(input())

deck = []
for i in range(n):
    a, c = map(int, input().split())
    deck.append([a, c, i+1])

sorted_deck = sorted(deck, key=lambda x: x[0], reverse=True)
m = 0
i_list = []
prev_c = 1e10
for j in range(n):
    a, c, i = sorted_deck[j]
    if c < prev_c:
        i_list.append(i)
        m += 1
    prev_c = c

print(m)
print(" ".join(map(str, sorted(i_list))))