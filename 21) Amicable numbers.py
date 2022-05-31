def d(n):
    if n <= 1:
        return 1
    else:
        s = 0
        for i in range(1, n):
            if n % i == 0:
                s += i
        return s

assert(d(220) == 284)
assert(d(284) == 220)

amicable_sum = 0

for i in range(1, 10001):
    number1 = d(i)
    number2 = d(number1)
    if number2 == i and number1 != number2:
        amicable_sum += i


print(amicable_sum)