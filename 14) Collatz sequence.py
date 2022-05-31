def collatz_sequence(n, chain = 0):
    if n == 1:
        return chain + 1
    else:
        if n % 2 == 0:
            chain += 1
            return collatz_sequence(n/2, chain)
        else:
            chain += 1
            return collatz_sequence(3*n+1, chain)


maxi = 0
max_number = 0

for i in range(1, 1000001):
    if collatz_sequence(i) > maxi:
        maxi = collatz_sequence(i)
        max_number = i

print(max_number)
