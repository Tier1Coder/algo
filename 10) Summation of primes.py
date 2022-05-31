def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int((n**0.5)+1)):
            if n % i == 0:
                return False
    return True

assert(is_prime(3) == True)
assert(is_prime(2) == True)
assert(is_prime(4) == False)
assert(is_prime(5) == True)

s = 0
for i in range(2, 2000000+1):
    if is_prime(i) == True:
        s += i

print(s)