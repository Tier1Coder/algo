def prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int((n**0.5)+1)):
            if n % i == 0:
                return False
    return True

assert(prime(10) == False)
assert(prime(4) == False)
assert(prime(1) == False)
assert(prime(2) == True)
assert(prime(7) == True)

cnt = 0
for i in range(1, 99999999):
    if prime(i) == True:
        cnt += 1
    if cnt == 10001:
        print(i)
        break