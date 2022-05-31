max_digits_number = 9876543210
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

assert(is_prime(4) == False)
assert(is_prime(2) == True)
assert(is_prime(7) == True)

def is_pandigital(n):
    a = str(n)
    temp_dict = dict()
    for i in a:
        if i in temp_dict:
            temp_dict[i] += 1
        else:
            temp_dict[i] = 1

    for key, value in temp_dict.items():
        if value > 1:
            return False
    return True

assert(is_pandigital(2134) == True)
assert(is_pandigital(2222) == False)
assert(is_pandigital(215462) == False)


for i in reversed(range(2143, max_digits_number)):
    if is_pandigital(i) == True:
        if is_prime(i) == True:
            print(i)
            break

