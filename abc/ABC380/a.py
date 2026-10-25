def main():
    n = input()

    num_one = n.count('1')
    num_two = n.count('2')
    num_three = n.count('3')

    if num_one == 1 and num_two == 2 and num_three == 3:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()