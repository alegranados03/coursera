# Uses python3
import sys
import itertools

def partition3(A):
    total = sum(A)
    if len(A) < 3 or total%3!=0: return 0
    splits = total//3

    print(A)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

