# Uses python3
import sys


def takesecond(elem):
    return elem[1]


def get_optimal_value(capacity, weights, values):
    a = value = 0
    vals = [x/y for x, y in zip(values, weights)]

    unit_vals=[]
    for i,val in enumerate(vals):
        unit_vals.append((i,val))

    unit_vals = sorted(unit_vals,reverse=True,key=takesecond)

    for x in unit_vals:
        i = x[0]
        if capacity == 0:
            return value
        a = min(weights[i], capacity)
        capacity = capacity - a
        value += a * x[1]

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
