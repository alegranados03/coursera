# Uses python3
import sys

def get_change(m):
    coins = 0
    while m > 0:
        if m >= 10:
            m -= 10
        elif m >= 5:
            m -= 5
        else:
            m -=1

        coins += 1
    return coins

def get_change_2(m):
    coins = 0
    if m >= 10:
        coins = m//10
        rec = m % 10
        if rec >= 5:
            coins += rec // 5
            coins += rec % 5
        else:
            coins += rec
    elif m >= 5:
        coins = m//5
        coins += m % 5
    else:
        return m
    return coins



    return coins

if __name__ == '__main__':
    m = int(input())
    #print(get_change(m))
    print(get_change_2(m))
