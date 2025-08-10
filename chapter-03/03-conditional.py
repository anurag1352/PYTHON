# CONDITIONAL STATEMENT.

# 1. if Statement.
age = 70

if(age >= 18):
    print("You Can Vote.")
    print("You can Drive.")

# 2. elif Statement.
light = "purpule"

if(light == "Red"):
    print(" Stop! Signal is red.")

elif(light == "yellow"):
    print("Drive Slow.")

elif(light == "green"):
    print("You Can Go.")

# 3. else statement.
else:
    print("Light Broken.")


# QUS. ===== GRADE STUDENTS BASED ON MARKS. ======
marks = 88

if(marks >= 90):
    print("A")
elif(marks >= 80 and marks < 90):
    print("B")
elif(marks >= 70 and marks < 80):
    print("C")
elif(marks >= 60 and marks < 70):
    print("D")
else:
    print("FAIL")