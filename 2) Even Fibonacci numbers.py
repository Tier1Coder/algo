def fibonacci_sequence(n):
    result = []
    a = 1
    b = 2
    result.append(a)
    result.append(b)
    for i in range(n-2):
        c = a + b
        a = b
        b = c
        result.append(c)
    return result

entry = fibonacci_sequence(100)
score = 0

for a in entry:
    if a > 4000000:
        break
    else:
        if a % 2 == 0:
            score += a

print(score)