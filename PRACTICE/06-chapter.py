# WAP TO FIND THE SUM OF FIRST N NATURAL NUMBERS USING (WHILE LOOP).
n = 5

sum = 0
count = 1

while count <= n:
    sum += count
    count += 1

    print("Sum of first",n, "natural number is:",sum)

# WAP TO FIND THE FACTORIAL OF FIRST N NUMBERS (FOR LOOP).
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    factorial = 1
    for j in range(1, i + 1): 
        factorial *= j
    print(f"Factorial of {i} is {factorial}")
