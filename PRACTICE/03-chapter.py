# TASK.1
#WAP TO INPUT USER'S FIRST NAME & PRINT IT'S  LENGTH.

fname = input("Enter your first Name : ")
print(len(fname))

# TASK.2
# WAP TO FIND THE OCCURENCE OF '$' IN A STRING.
data = "In Inda , we use Ruppes & in USA use $."
print(data.count("$"))

# TASK .3
# WAP TO CHECK IF A NUMBER ENTERED BY THE USER IS ODD OR EVEN.
num = int(input("Enter a value : "))

if(num % 2 == 0):
    print("Even.")
else:
    print("Odd")

# TASK .4
#WAP TO FIND THE GREATEST OF 3 NUMBERS ENTERED BY USER.
num1 = int(input("Enter first value : "))
num2 = int(input("Enter second value : "))
num3 = int(input("Enter third value : "))

if(num1 >= num2 and num1 >= num3):
    print("num1 is greatest.")
elif(num2 >= num1 and num2 >= num3):
    print("num2 is greatest.")
else:
    print("num3 is greatest.")

# TASK.5
# WAP TO CHECK IF A NUMBER IS A MULTIPLE OF 7 OR NOT.
mul = int(input("Enter value : "))

if(mul % 7 == 0):
    print("Multiplication of 7.")
else:
    print("Not multiple of 7.")