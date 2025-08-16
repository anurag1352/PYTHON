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

