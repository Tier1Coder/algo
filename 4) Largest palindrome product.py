results = []

for i in range(100, 1000):
    for j in range(100, 1000):
        a = i*j
        b = str(a)
        if b == b[::-1]:
            results.append(int(b))

print(max(results))

