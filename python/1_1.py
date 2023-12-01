
with open("/home/raphael/rapni/Documents/python/input1.txt", "r") as inputfile:
    input = inputfile.readlines()

value = 0

for line in input:
    digits = []
    first = 0
    last = 0
    for index, char in enumerate(line):
        if char.isdigit():
            digits.append((index,char))
    if len(digits) == 1:
        first = last = digits[0][1]
    else:
        first = digits[0][1]
        last = digits[-1][1]
    code = first + last
    value += int(code)

print(f"The resulting value is: {value}")
