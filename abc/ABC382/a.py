def main():
    n = int(input())
    t_list = []
    v_list = []
    for i in range(n):
        t, v = map(int, input().split())
        t_list.append(t)
        v_list.append(v)
    
    volume = 0
    for time in range(1, t_list[-1]+1):
        if volume > 0:
            volume -= 1
        
        if time in t_list:
            volume += v_list[t_list.index(time)]
    
    print(volume)

if __name__ == '__main__':
    main()