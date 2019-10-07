# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result

def optimal_weight2(W, w):

    filas = [x for x in w if x <= W]
    bags = [[0 for _ in range(W + 1)] for _ in range(len(filas) + 1)]
    for f in range(1, len(bags)):
        wi = filas.pop(0)
        for c in range(1, len(bags[0])):
            optimal = bags[f - 1][c - wi] + wi

            if bags[f - 1][c] <= optimal <= c:
                bags[f][c] = optimal
            else:
                bags[f][c] = bags[f - 1][c]
    print(bags)
    return bags[len(bags)-1][len(bags[0])-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight2(W, w))
