# Uses python3
import sys
import math

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

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

def fibonacci_partial_sum(m,n):

    rems=fibonacci_mods_array()

    m,n = m+1, n+2
    return abs(int(rems[n%len(rems)])- int(rems[m%len(rems)]))%10


if __name__ == '__main__':
    input = input()
    from_, to = map(int, input.split())
    #print(fibonacci_partial_sum_naive(from_, to))
    print(fibonacci_partial_sum(from_, to))