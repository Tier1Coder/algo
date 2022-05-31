for a in range(3, 999):
    for b in range(4, 999):
        for c in range(5, 999):
            if a**2 + b**2 == c**2:
                if a + b + c == 1000:
                    print(a*b*c)