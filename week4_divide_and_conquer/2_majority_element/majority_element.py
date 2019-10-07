# Uses python3
import sys
import math
def get_majority_element(a, left, right):
    a.sort()
    x = count = 0
    for num in a:
        if x != num:
            if count > math.floor(right/2): return 1
            x = num
            count = 1
        else:
            count += 1
    return 1 if count > math.floor(right/2) else -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
