# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10


def fibonacci_mods_array():
    f = "0 1 1 "
    m = 10000
    start = end = 1
    while f.count("0 1 1 ") <= 1:
        start = start % m
        end = end % m
        fib = (start + end)%m
        start = end
        end = fib
        f += str(fib) + " "

    rems = f.split()

    for _ in range(3):
        rems.pop(-1)

    return rems


def fibonacci_sum_squares(n):

    if n<=2: return n

    rems = fibonacci_mods_array()

    return int(rems[(n)%len(rems)]) * int(rems[(n+1)%len(rems)]) % 10



if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares(n))
