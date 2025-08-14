# ==== DICTIONARY & SET PRACTICE =====
"""
TASK.1 
STATE FOLLOWING WORD MEANING IN A PYTHON DICTIONARY:
TABLE : "a piece of furniture", "list of facts & figures"
cat : "a small animal" 
"""
dict = {
    "table" : ["a piece of furniture", "list of facts &figures"], 
    "cat" : "a small animal"
}

print(dict)

"""
TASK 2.
YOU ARE GIVEN A LIST OF SUBJECTS FOR STUDENTS.ASSUME ONE CLASSROOM IS REQUIRED FOR 1 SUBJECT.HOW MANY CLASSROOM ARE NEEDED BY ALL STUDENTS.

"PYTHON", "JAVA", "C++", "PYTHON", "JS",
"JAVA", "PYTHON", "JAVA", "C++", "C"
"""

sub = {"PYTHON", "JAVA", "C++", "PYTHON", "JS",
"JAVA", "PYTHON", "JAVA", "C++", "C"}
print(len(sub))

"""
TASK 4.
WAP to enter marks of 3 subjects from the user and store them in a dictionary. start with an empty dictionary & add one by one. use subject name as key & marks as value.
"""

# marks = {}

# x = int(input("enter phy : "))
# marks.update({"phy" : x})

# y = int(input("enter chem : "))
# marks.update({"chem" : y})

# z = int(input("enter math : "))
# marks.update({"math" : z})

# print(marks)

"""
TASK .4
figure out a way to store 9 & 9.0 as separate values in the set.
"""
store = {(9 , "int"), (9.0, "float")}
print(store)