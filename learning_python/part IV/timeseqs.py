# File timeseqs.py
"Test the relative speed of iteration tool alternatives."

import sys, timer, math                                # Import timer functions
from functools import reduce 
n = 10000
#repslist = list(range(reps))                     # Hoist out, list in both 2.X/3.X

def recusive_(n=100):
    if n == 1:
        return 1
    else:
        return n * recusive_(n-1)

def reduce_(n=100):
    result = reduce(lambda x, y: x*y, range(1, n))
    return result

def iterate_(n=100):
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result

def factorial_(n=100):
    return math.factorial(n)

print(sys.version)
for test in (recusive_, reduce_, iterate_, factorial_):
    (bestof, (total, result)) = timer.bestoftotal(5, 1000, test)
    print ('%-9s: %.5f => [%s]' %
           (test.__name__, bestof, result))
