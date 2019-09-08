# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    start=end=1
    if n==2: return end
    for i in range(n-2):
        fib=start+end
        start=end
        end=fib
    return fib

if __name__ =='__main__':
    n = int(input())
    print(calc_fib(n))
   # print(calc_fib(n))
