# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    a = value = 0
    unit_vals = [x / y for x,y in zip(values,weights)]

    for _ in range(len(weights)):
        i = weights.index(min(weights))

        if (capacity == 0): return value
        a = min(weights[i],capacity)
        capacity = capacity - a
        value += a * unit_vals[i]

        weights.pop(i)
        unit_vals.pop(i)
    return value


if __name__ == "__main__":
    data = list(map(int, input().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
