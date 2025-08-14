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
