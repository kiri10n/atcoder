h=int(input())

plant_h = 0
for i in range(31):
    if plant_h > h:
        print(i)
        exit()
    plant_h += 2**i
    