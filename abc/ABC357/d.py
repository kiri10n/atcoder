MOD = 998244353

def power_func(a,n,p):
    bi = str(format(n,"b"))
    res = 1
    for i in range(len(bi)):
        res = (res*res) %p
        if bi[i] == "1":
            res = (res*a) %p
    return res

def main():
    n_str = input()
    n = int(n_str)

    ans = 0
    for i in range(n):
        mod_i = (n * power_func(10, i, MOD)) % MOD
        ans = (ans + mod_i) % MOD
        #print(f"mod_{i}: {mod_i}, ans: {ans}")

    print(ans)


if __name__ == '__main__':
    main()