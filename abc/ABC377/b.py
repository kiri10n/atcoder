def main():
    attacked_rows = set()
    attacked_cols = set()
    for i in range(8):
        s = input()
        for j in range(8):
            if s[j] == "#":
                attacked_rows.add(i)
                attacked_cols.add(j)
    
    safe_squares = 0
    for i in range(8):
        for j in range(8):
            if i not in attacked_rows and j not in attacked_cols:
                safe_squares += 1
    
    print(safe_squares)

if __name__ == '__main__':
    main()