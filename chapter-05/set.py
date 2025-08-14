# ====== SET IN PYTHON =======

set1 = {1,2,3}
set2 = {1,1,2,2,3,3} # repeted not print 
print(set2)
print(set1)

set2.add("hello")
print(set2)

# empty set
khali = set()
print(type(khali))

#===== SET METHODS ======
range = {1,2,3,"python",4,5,5,1,"hello"}
print(range)
print(range.add("Devops"))
print(range)

# remove element.
range.remove(2)
print(range)

# delete random value.
print(range.pop())
print(range)

#print(range[2]) # not allowed by index

# clear set.
range.clear()
print(range)