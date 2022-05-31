entry = []

def multiples_of_3_below(number):
    for i in range(3, number):
        if i % 3 == 0:
            entry.append(i)

def multiples_of_5_below(number):
    for i in range(5, number):
        if i % 5 == 0:
            entry.append(i)

multiples_of_5_below(1000)
multiples_of_3_below(1000)

print(sum(set(entry)))