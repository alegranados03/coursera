# Uses python3
import sys
import math

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10



def fibonacci_sum(n):
    f="0 1 1 "
    if (n <= 1): return n
    if (n == 2): return 2

    m = 10
    start=end=1
    while f.count("0 1 1 ")<=1:
        start = start % m
        end = end % m
        fib = (start + end) % m
        start = end
        end = fib
        f += str(fib) + " "

    rems = f.split()

    for _ in range(3):
        rems.pop(-1)

    return (int(rems[(n+2)%(len(rems))])-1)%10






if __name__ == '__main__':
    input = input()
    n = int(input)
    #print(fibonacci_sum_naive(n))
    print(fibonacci_sum(n))
