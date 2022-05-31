import math

def divsum(num):
    result = 0
    i = 2
    while i <= (math.sqrt(num)):
        if (num % i == 0):
            if (i == (num / i)):
                result = result + i
            else:
                result = result + (i + num / i)
        i = i + 1
    return (result + 1)


assert(divsum(220) == 284)
assert(divsum(284) == 220)

def is_abundant(n):
    if divsum(n) > n:
        return True
    return False

assert(is_abundant(12) == True)
assert(is_abundant(8) == False)
assert(is_abundant(1) == False)

limit = 28123

abundant_numbers = []

for i in range(limit+1):
    if is_abundant(i) == True:
        abundant_numbers.append(i)


sums = [0]*28124
del abundant_numbers[0]

for i in range(0, len(abundant_numbers)):
    for j in range(i, len(abundant_numbers)):
        s = abundant_numbers[i]+abundant_numbers[j]
        if s <= 28123:
            if sums[s] == 0:
                sums[s] = s

count = 0

for i in range(1, len(sums)):
    if sums[i] == 0:
        count += i



print(count)
