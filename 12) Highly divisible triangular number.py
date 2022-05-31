from functools import reduce

def triangular_number(n):
    return int(n*(n+1)/2)

def factors(n):
    step = 2 if n % 2 else 1
    return len(set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1, step) if n % i == 0))))


assert(triangular_number(7) == 28)
assert(factors(28) == 6)


for i in range(2, 99999999999):
    a = triangular_number(i)
    if factors(a) > 500:
        print(a)
        break

