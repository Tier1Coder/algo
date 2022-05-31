def factorial(n):
    if n <= 1:
        return 1
    return n*factorial(n-1)

assert(factorial(4) == 24)
assert(factorial(1) == 1)
assert(factorial(5) == 120)

f = []
for i in range(0, 10):
    f.append(factorial(i))

def curious_number(n):
    a = str(n)
    s = 0
    for i in a:
        s += f[int(i)]
    if s == n:
        return True
    else:
        return False

assert(curious_number(145) == True)
assert(curious_number(144) == False)


sum_of_all_curious_numbers = 0

for i in range(10, 1854721):
    if curious_number(i) == True:
        sum_of_all_curious_numbers += i

print(sum_of_all_curious_numbers)