# f = open("chapter-08/demo.txt", "r")
# read data.
data = f.read()
print(data)
print(type(data))
# f.close()

# read one line at a time.
line1 = f.readline()
print(line1)

# WRITE IN A FILE
f = open("chapter-08/demo.txt", "w")
data = f.write("This is new line")
print(data)

# APPEND IN FILE
f = open("chapter-08/demo.txt", "a")
data = f.write("\nAppend a new data")
print(data)

# READ + OVERWRITE.
f = open("chapter-08/demo.txt", "r+")
data = f.write("This data is read and overwite using R+")
print(data)

# READ + OVERWRITE USING (w+)
f = open("chapter-08/demo.txt", "w+")
data = f.write("I learn python")
print(data)

# READ + APPEND
f = open("chapter-08/demo.txt", "a+")
data = f.write("\nAppend new data")
print(data)

# DELETE FILE 
import os
os.remove("chapter-08/demo.txt")