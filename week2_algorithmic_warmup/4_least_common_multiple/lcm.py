# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b


def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)


def lcm_opt(a,b):
    return int(abs(a*b)/gcd(a,b))


if __name__ == '__main__':
    input = input()
    a, b = map(int, input.split())
    #print(lcm_naive(a, b))
    print(lcm_opt(a, b))

