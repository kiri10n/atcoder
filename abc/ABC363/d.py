def main():
    n = int(input())

    min_in_x_digit = 0
    for i in range(19):
        min_in_x_digit += 10**i
        if min_in_x_digit <= n and n < min_in_x_digit + 10**i:
            digit = i+1
            break
    
    start = 10**(digit)
