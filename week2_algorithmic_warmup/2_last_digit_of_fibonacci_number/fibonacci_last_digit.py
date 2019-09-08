# Uses python3
import sys


def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


def last_digit_fib(n):
    if n<=1:
        return n

    if n==2: return 1

    start = end = 1

    for _ in range(n-2):
        start=start%10
        end=end%10
        fib = (start + end) % 10
        start=end
        end=fib

    return fib

if __name__ == '__main__':
    input = input()
    n = int(input)
    print(last_digit_fib(n))
    #for x in list(np.random.randint(1,301,100)):
    #    if(get_fibonacci_last_digit_naive(x)==last_digit_fib(x)):
    #        print('IGUALES')
    #    else:
    #        print('DIFERENCIA')
    #        print(" El número es: {} get_fibonacci: {}   last_digit: {} ".format(x,get_fibonacci_last_digit_naive(x),last_digit_fib(x)))



