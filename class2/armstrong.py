n = input("Enter a number: ")
arms = 0
length = len(n)
for digit in n:
    arms = arms + int(digit) ** length

print("Armstrong number is ", arms)
