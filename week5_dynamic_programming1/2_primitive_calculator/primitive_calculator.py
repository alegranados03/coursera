# Uses python3
import sys
import math


def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)


def optimal_sequence2(n):
    num_operations = [0, 0] + [math.inf] * (n - 1)

    for i in range(2, n + 1):
        t1, t2, t3 = [math.inf] * 3

        t1 = num_operations[i - 1] + 1
        if i % 2 == 0: t2 = num_operations[i // 2] + 1
        if i % 3 == 0: t3 = num_operations[i // 3] + 1
        min_ops = min(t1, t2, t3)
        num_operations[i] = min_ops

    print(num_operations[n])

    # Backtracking the numbers leading to n
    nums = [n]
    while n != 1:
        if n % 3 == 0 and num_operations[n] - 1 == num_operations[n // 3]:
            nums += [n // 3]
            n = n // 3
        elif n % 2 == 0 and num_operations[n] - 1 == num_operations[n // 2]:
            nums += [n // 2]
            n = n // 2
        else:
            nums += [n - 1]
            n = n - 1

    print(' '.join([str(i) for i in nums][::-1]))


input = sys.stdin.read()
n = int(input)
optimal_sequence2(n)

