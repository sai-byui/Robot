def summation(low, high, func, excl=()):
    total = 0
    for i in range(low, high+1):
        if i in excl:
            continue
        total += func(low, high)
    return total

def product(low, high, func, excl=()):
    prod = 1
    for i in range(low, high + 1):
        if i in excl:
            continue
        prod *= func(i)

def fun2(k, n):
    return ((2 * (n ** 2)) / (k ** 2)) * (product(,,fun3) / product(,,fun4))

def fun1(k, n):
    return summation(k, n, fun2)