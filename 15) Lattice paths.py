def factorial(n):
    if n <= 1:
        return n
    else:
        return factorial(n-1) * n

assert(factorial(2) == 2)
assert(factorial(3) == 6)

def lattice_path(n):
    return factorial(2*n) / factorial(n) / factorial(n)

print(int(lattice_path(20)))