# ====== PYTHON DIRECTORY =======

info = {
    "name" : "Anurag",
    "age" : 20,
    "isAdult" : True,
    "lang" : ["python", "JavaScript", "C"],
    "topic" : ("dict","set")
}

print(info)
print(info["lang"])
print(info["isAdult"])

# add/assign new value.
info["name"] = "Anurag Sharma"
print(info["name"])

# delete key:value.
del info["age"]
print(info)

# ===== NESTED DIRECTORY ======
student = {
    "name" : "Angel",
    "score" : {
        "chem" : 96,
        "phy" : 88,
        "bio" : "90"
    }
}

print(student)
print(student["name"])
print(student["score"])
print(student["score"] ["bio"]) # also access nested key:value.

# CHANGE NESTED KEY:VALUE.
student ["score"] ["chem"] = 89
print(student["score"] ["chem"])

# DELETE NESTED KEY:VALUE.
del student["score"] ["bio"]
print(student["score"])

# ===== DIRECTORY METHODS =======
data = {
    "role" : "SDE-2",
    "mode" : "WFH",
    "city" : "panchkula",
    "age" : 20
}
print(data)
print(list(data.keys()))
print(len(list(data.values())))
print(list(data.items()))

print(data.get("mode"))
print(data.update({"system" : "linux"})) # add new key:value pair.
print(data)