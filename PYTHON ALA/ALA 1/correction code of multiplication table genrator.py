print("Multiplication Table Generator")

num = int(input("Enter number: "))
i = 1
total = 0

while i <= 10:
    result = num * i
    print(num, "x", i, "=", result)

    if result % 2 == 0:
        print("Even result")
    else:
        print("Odd result")

    total = total + result
    i = i + 1

print("Sum of table:", total)

if total > 100:
    print("Large sum")
else:
    print("Small sum")