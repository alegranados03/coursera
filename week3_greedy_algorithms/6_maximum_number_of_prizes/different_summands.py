# Uses python3
import sys

def optimal_summands(n):
    summands = []
    sums = term = 0
    if n <= 2:
        summands.append(n)
    else:
        while sums != n:
            term = term + 1
            sums += term

            if sums > n:
                dif = sums - n
                fix = term - dif
                dropped = summands.pop()
                last = dropped + fix
                summands.append(last)
                sums = sums -(dropped + term)
                sums += last
            else:
                summands.append(term)

    return summands

if __name__ == '__main__':
    input = input()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')

