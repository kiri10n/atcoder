import numpy as np

def main():
    n = int(input())
    a = []
    for i in range(n):
        row = list(input())
        a.append(row)
    a = np.array(a)
    
    for i in range(n//2):
        sub = a[i:n-i, i:n-i]
        sub90 = np.rot90(sub, -1)
        a[i:n-i, i:n-i] = sub90

        #print(f"i={i}")
    for k in range(n):
        print("".join(a[k]))

if __name__ == '__main__':
    main()
