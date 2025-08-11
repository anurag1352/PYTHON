# ==== TUPLES IN PYTHON ====
tup1 = ()
tup2 = (1,)
# tup = (1) # It's a int
tup3 = (1,2,3,4,5)
print(tup1)
print(type(tup1))

print(tup2)
print(type(tup2))

print(tup3)
print(type(tup3))

# === STUDENT DATA ====
student = ("Anurag" , 75 , "Noida")
#student[0] = "Angel" # Not allowed
print(student[0:2])
print(student)

# ========== TUPLES METHODS ============
tup = (2,1,3,1)
print(tup.index(1))
print(tup.count(1))