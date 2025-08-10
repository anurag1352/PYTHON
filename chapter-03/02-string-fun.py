# STRING FUNCTIONS.
info = "i Anurag, and i learn python for devops."
print(info.endswith("ops.")) # if end with ops. then print if not then print false.

info_up = info.capitalize() # capitalize first or zero index.
print(info_up)

# REPLACING
print(info.replace("i" ,"I'm"))

# FIND
print(info.find("Anurag"))
print(info.find("p"))

# COUNT.
print(info.count("o"))