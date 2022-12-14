from math import *
def fast_fib(n):
    sqr=sqrt(5)
    pli=(sqr+1.0)/2.0
    phi=(sqr+1.0)/2.0
    return((pli**n)-(-phi**n))/sqr
print(fast_fib(5))