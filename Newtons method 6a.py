import math


def f(x):
    return math.exp(x) + 2**(-x) - 2*math.cos(x) - 6

# derivative calc
def fprime(x):
    return math.exp(x) + math.log(2) * 2**(-x) + 2*math.sin(x)


def newtmethod(p0,TOL,n0):
    i = 1
    while i <= n0:
        p = p0 - f(p0)/fprime(p0)
        if abs(p - p0) < TOL:
            print(f"The procedure was successful after {i} iterations.")
            return p
        i += 1
        p0 = p

    print(f"The method failed after {n0} iterations.")
    return None

# Guess on interval 1 <= 2
p0 = 1.5

TOL = 1e-5

n0 = 100

root = newtmethod(p0,TOL,n0)

if root is not None:
    print (f"The root found is: {root}")
else:
    print ("Root not found!")


