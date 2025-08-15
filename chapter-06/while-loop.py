# ===== WHILE LOOP IN PYTHON ======
count = 1

while count <= 5:
    count += 1
    print("hello")

# print counting
# count = 5

# while count >= 1:
#     print(count)
#     count -= 1

# infinite loop (don't use )
# while True:
#     print("Hello World")

# print numbers 1 to 100.
i = 1

while i <= 100:
    print(i)
    i += 1

# print 100 to 1.
x = 100

while x >= 1:
    print(x)
    x -= 1

# Table print
i = 1
n = 3

while i <= 10:
    print(n * i)
    i += 1

# print square 1 to 10.
a = 1

while a <= 10:
    print(a * a)
    a += 1
    
# print elements
val = [1,4,9,16,25,36,49,64,81,100]

idx = 0
while idx < len(val):
    print(val[idx])
    idx += 1

# search for number
n = (1,4,9,16,25,36,49,64,81,100)

x = 36

i = 0 # initialization
while i < len(n):
    if(n[i] == x):
        print("Found at idx ",i)
    i+= 1