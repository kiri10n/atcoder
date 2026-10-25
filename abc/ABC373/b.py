def main():
    s = input()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    dist = 0
    present = s.index('A')
    for i in range(1, len(alphabet)):
        char = alphabet[i]
        dist += abs(s.index(char) - present)
        present = s.index(char)
    print(dist)

if __name__ == '__main__':
    main()