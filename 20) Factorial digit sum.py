n = 100

def factorial(n):
    s = 1
    for i in reversed(range(2, n+1)):
        s *= i

    return s

assert(factorial(10) == 3628800)

score = factorial(n)
score = str(score)
cnt = 0

for i in score:
    cnt += int(i)

print(cnt)