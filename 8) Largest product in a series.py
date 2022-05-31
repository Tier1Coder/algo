""" odczyt z pliku """
temp = open("8) Largest product in a series - file.txt", "r")
sign = temp.readline()

greatest_product = 0
current_product = 0

""" 5832 
for i in range(3, len(sign)):
    current_product = int(sign[i])*int(sign[i-1])*int(sign[i-2])*int(sign[i-3])
    if current_product > greatest_product:
        greatest_product = current_product

print(greatest_product)
"""

for i in range(13, len(sign)):
    current_product = int(sign[i])*int(sign[i-1])*int(sign[i-2])*int(sign[i-3])*int(sign[i-4])*int(sign[i-5])*int(sign[i-6])*int(sign[i-7])*int(sign[i-8])*int(sign[i-9])*int(sign[i-10])*int(sign[i-11])*int(sign[i-12])
    if current_product > greatest_product:
        greatest_product = current_product

print(greatest_product)