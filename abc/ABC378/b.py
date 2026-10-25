def main():
    n = int(input())
    qr = []
    for i in range(n):
        q_i, r_i = map(int, input().split())
        qr.append((q_i, r_i))

    q = int(input())
    for i in range(q):
        t, d = map(int, input().split())
        qq = qr[t-1][0]
        rr = qr[t-1][1]
        days_to_add = (rr - d % qq) % qq
        # if days_to_add == 0:
        #     days_to_add = qq
        print(d + days_to_add)
        
    
if __name__ == '__main__':
    main()