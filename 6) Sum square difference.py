def sum_of_squares(n):
    s = 0
    for i in range(1, n+1):
        s += i**2
    return s

def square_of_sum(n):
    s = 0
    for i in range(1, n+1):
        s+=i
    return s**2

print(square_of_sum(100) - sum_of_squares(100))