# python3
import sys


def compute_min_refills(distance, tank, stops):
    actual = p = count = 0
    s=len(stops)
    stops.append(distance)
    while p<s:

        while p<s and stops[p+1] - stops[actual] <= tank:
            p+=1

        if actual==p: return -1

        actual=p
        if p<s: count+=1


    return count

if __name__ == '__main__':
    #d, m, _, *stops = map(int, sys.stdin.read().split())
    d, m, _, *stops = map(int, sys.stdin.read().split())
    stops.insert(0,0)
    print(compute_min_refills(d, m, stops))