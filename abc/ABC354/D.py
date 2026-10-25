a, b, c, d = map(int, input().split())

h = c-a
v = d-b

h_num = h//4
h_mod = h%4

v_num = v//4
v_mod = v%2

h_mod = (h_mod - a%4) %4
v_mod = (v_mod - b%2) %2

if h_mod == 0:
    if v_mod == 0:
        other = 4
    elif v_mod == 1:
        other = 2
elif h_mod == 1:
    if v_mod == 0:
        other = 1.5
    elif v_mod == 1:
        other = 1
elif h_mod == 2:
    if v_mod == 0:
        other = 3
    elif v_mod == 1:
        other = 1.5
elif h_mod == 3:
    if v_mod == 0:
        other = 3.5
    elif v_mod == 1:
        other = 1.5

if v_mod == 1:
    



print(2*(other+h_num*v_num+(h_num*v_num*4)))