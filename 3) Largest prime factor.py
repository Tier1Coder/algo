def is_prime(n):
    if n == 1 or n == 2:
        return True
    else:
        for i in range(2, int(n*0.5)+1):
            if n % i == 0:
                return False
        return True

assert(is_prime(10) == False)
assert(is_prime(9) == False)
assert(is_prime(2) == True)
assert(is_prime(3) == True)
assert(is_prime(4) == False)

test_case = 600851475143
factors = []
score = 1

for i in range(2, 50000):
    if is_prime(i) == True and test_case % i == 0:
        factors.append(i)
        for a in factors:
            score *= a
            if score == test_case:
                break
            else:
                score = 1

print(factors)
