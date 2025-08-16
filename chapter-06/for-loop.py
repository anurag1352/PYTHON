# ======== FOR LOOP IN PYTHON =========
x = {1,2,3,4,5}

for i in x:
    print(i)

text = ("apple", "mango")

for x in text:
    print(x)


# print the elements of the following list using aloop:
# [1,2,4,5,6,7,90,100]
# search a x number

num = [1,2,4,5,6,7,90,100,5]
x = 5

idx = 0
for n in num:
    if(n == x):
        print("num exist", idx)
        break
    idx += 1

# Range function
for i in range(10):
    print(i)

# print 1 to 100 number
for x in range(1,101):
    print(x)

# print number 100 to 1
for y in range(101 , 0, -1):
    print(y)

# print multiplication table of n
n = int(input("Enter a number :"))

for i in range(1, 11):
    print(n * i)

 # PASS STATEMENT
for i in range(5):
    pass
print("Some useful work")