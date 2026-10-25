n = int(input())

all = {}
sum = 0
for i in range(n):
    s, c = input().split()
    c = int(c)
    sum += c

    all[s] = c

sorted_list = list(sorted(all))
print(sorted_list[sum % n])