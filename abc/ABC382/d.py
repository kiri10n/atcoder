def prime_factorize(n):
    res = []
    for i in range(2, int(n**0.5)+1):
        if n%i != 0:
            continue
        cnt = 0
        while n%i == 0:
            cnt += 1
            n //= i
        res.append((i, cnt))
    if n != 1:
        res.append((n, 1))
    return res

def main():
    n = int(input())

    ans = 0

    # 2*10**6までのすべての素数を求める
    primes = []
    for i in range(2, 2*10**6):
        is_prime = True
        for j in range(2, int(i**0.5)+1):
            if i%j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)

    # x^8
    for x in range(2, 54):
        if x**8 <= n:
            ans += 1
    
    # x^2 * y^2
    for x in primes:
        for y in primes:
            if y < n**0.5 / x and x > y:
                ans += 1
            else:
                break
    
    print(ans)

if __name__ == '__main__':
    main()