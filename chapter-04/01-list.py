# LIST IN PYTHON (SIMILAR TO ARRAY)
marks = [33 , 77 , 75 , 68 , 49]
print(marks[3])
print(marks)
print(type(marks))

# === LIST OF STUDENT ===
student = ["Anurag" , 85 , "Noida"]
print("Before Edit : ", student)
student[0] = "Angel"
print("After Edit : ", student)

# length of student
print(len(student))

 # === LIST SLICING ===
num = [1,2,3,4,5,6,7]
print(num[1:4])

# ==== LIST METHODS ====
data = [7,5,6,4,3,2,1]
print(data.append(8)) # add element at the end
print(data)

# Sorting = assending
print(data.sort())
print(data)

# Sorting = desending
print(data.sort(reverse=True))
print(data)

# Revere
print(data.reverse())
print(data)

# INSERT
print(data.insert(8,9))
print(data)

# REMOVE
print(data.remove(9))
print(data)

# POP
print(data.pop(7))
print(data)