a = 2**1000
a = str(a)

sum_of_power_digit = 0
for number in a:
    sum_of_power_digit += int(number)

print(sum_of_power_digit)