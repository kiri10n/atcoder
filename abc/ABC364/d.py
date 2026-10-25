import numpy as np

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    a = sorted(a)
    a = [[a] * q]
    a = np.array(a)

    b = []
    k = []
    for i in range(q):
        b_i, k_i = map(int, input().split())
        b.append(b_i)
        k.append(k_i)
    b = np.array(b)
    k = np.array(k)

    dist = np.linalg.norm(a-b, axis=0)
    dist = dist.argsort()

    for i in range(q):
        print(dist[k[i]-1])
    
if __name__ == '__main__':
    main()