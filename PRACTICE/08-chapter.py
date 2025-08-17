# create a new file "Practice.txt" using python. Add the following data in it:
# Hi everyone
# we are learning File I/O
# using java.
# I like Programming in java.
with open("Practice.txt", "w") as f:
          f.write("Hi everyone\nwe are learning File I/O\n")
          f.write("using java.\nI like Programming in java.")


# waf that replaces all occurence of java with python in above file.
with open("Practice.txt", "r") as f:
        data = f.read()

new_data = data.replace("java", "Python")
print(new_data)

with open("Practice.txt", "w") as f:
        f.write(new_data)

# search if the word "learning" exists in the file or not.
with open("Practice.txt", "r") as f:
        data = f.read()
        if(data.find("Learning") != -1):
                print("exists")
        else:
                print("Not found")

# WAF TO FIND IN WHICH LINE OF THE LINE OF THE FILE DOES THE WORD "LEARNING" OCCUR FIRST.
def check_line():
    word = "learning"
    data = True
    line_no = 1
    with open("Practice.txt", "r") as f:   # READ MODE
        while data:
            data = f.readline()
            if word in data:       # agar word line me hai
                print("Word found at line:", line_no)
                return
            line_no += 1
        else:
            print("-1")   # word not found

