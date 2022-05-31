from functools import lru_cache


@lru_cache()
def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

assert(fibo(4) == 3)
assert(fibo(3) == 2)
assert(fibo(12) == 144)

for i in range(1, 199999999999):
    a = fibo(i)
    if len(str(a)) >= 1000:
        print(i)
        break