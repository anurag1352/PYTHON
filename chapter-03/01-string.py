# TYPES OF DECLARING STRINGS IN PYTHON
str1 = 'Anurag' # single quotes.
str2 = "Sharma" # double quotes.
str3 = """Anurag Sharma""" # Triple quotes.

print(str1)
print(str2)
print(str3)

# NESTED QUOTES.
str4 = "They say i can't go for walk."
str5 = 'I"m not available.'
print(str4)
print(str5)

# ======STRING OPERATIONS.========
# 1. CONCATINATION.
fname = "Python"
lname = "Devops"
fullName = fname + " " + lname
print(fullName)

# 2. LENGTH OF STRING.
data = "My Name is Anurag i'm 20 years old. And i'm learning python."
dataLen = len(data)
print(dataLen)

# 3. INDEXING.
num = "Python for devops."
print(len(num))
print(num[2])
# num[6] = "p" # not allowed

# 4. SLICING.
name = "Anurag"
cut = name[0 : 3] # ending index not include.
print(cut)

print(name[:3]) # same as cut.
print(name[0:]) #  work as len(name).

slice = name[0 : len(name)]
print(slice)

# NEGATIVE SLICEING.
fruit = "Apple"
print(fruit[-3 : -1]) # ending index not include