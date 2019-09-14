#Uses python3

import sys

def largest_number(a):

    ans=[]
    while a:
        maxim = 0
        for digit in a:
            if int(str(digit)+str(maxim))>=int(str(maxim)+str(digit)):
                maxim = digit
        ans.append(maxim)
        a.remove(maxim)
    return ans


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    b = data[1:]
    print("".join(largest_number(a)))

