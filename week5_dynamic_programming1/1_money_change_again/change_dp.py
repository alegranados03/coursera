# Uses python3
import sys

def get_change(m):
    denominations = [1, 3, 4]
    changes = [0]+[m+1]*m

    for i in range(1,m+1):
        coins = changes[i]
        for j in denominations:
            if i>=j:
                c = changes[i-j]+1
                if coins > c:
                    changes[i] = c
                    coins = changes[i]

    return changes[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
