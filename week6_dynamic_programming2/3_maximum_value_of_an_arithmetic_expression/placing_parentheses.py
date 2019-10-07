# Uses python3
import sys
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(dataset):
    nums = dataset
    # separating numbers and symbols
    numbers = [int(x) for x in dataset if x.isdigit()]
    symbols = [x for x in dataset if x.isdigit() == False]

    # initialize matrix
    m = [[0 for _ in numbers] for _ in numbers]
    M = [[0 for _ in numbers] for _ in numbers]
    for i in range(len(m)):
        m[i][i] = numbers[i]
        M[i][i] = numbers[i]

    for s in range(len(numbers)):
        for i in range(len(numbers) - s - 1):
            j = i + s + 1
            minimal = sys.maxsize
            maximal = -sys.maxsize
            for k in range(i, j):
                a = evalt(M[i][k], M[k + 1][j], symbols[k])
                b = evalt(M[i][k], m[k + 1][j], symbols[k])
                c = evalt(m[i][k], M[k + 1][j], symbols[k])
                d = evalt(m[i][k], m[k + 1][j], symbols[k])
                minimal = min(minimal, a, b, c, d)
                maximal = max(maximal, a, b, c, d)
            M[i][j] = maximal
            m[i][j] = minimal

    return M[0][len(numbers) - 1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
