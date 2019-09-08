# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def fibonacci_huge(n,m):
    f="0 1 1 "
    if (n <= 1): return n
    if (n == 2): return 1

    start=end=1
    while f.count("0 1 1 ")<=1:
        fib=start+end
        start=end
        end=fib
        f+=str(fib%m)+" "
    fibmods=f.split()
    return fibmods[n%(len(fibmods)-3)]

if __name__ == '__main__':
    input = input()
    n, m = map(int, input.split())
    #print(get_fibonacci_huge_naive(n, m))
    print(fibonacci_huge(n, m))
