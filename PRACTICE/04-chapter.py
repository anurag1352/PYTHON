# ==== CHAPTER TASKS =====

# TASK .1
# WAP TO ASK THE USER TO ENTER NAMES OF THEIR 3 FAVORITE MOVIES AND STORE THEN IN A LIST.
 # === METHOD 1st. ====

movies = []
# movie1 = input("Enter First Favorite Movie : ")
# movie2 = input("Enter Second Favorite Movie : ")
# movie3 = input("Enter Third Favorite Movie : ")

# movies.append(movie1)
# movies.append(movie2)
# movies.append(movie3)

 # === METHOD 2nd. ====
# movies.append(input("Enter First Favorite Movie : "))
# movies.append(input("Enter Second Favorite Movie : "))
# movies.append(input("Enter Third Favorite Movie : "))

# print(movies)

# TASK .2
# WAP TO CHECK IF A LIST CONTAINS A PALINDRONE OF ELEMENTS. 
list1 = [1,2 ,1]
list2 = [1 ,2 ,3]

copt_list2 = list2.copy()
copt_list2.reverse()

if(list2 == copt_list2):
    print("this is PALINDRONE.")
else:
    print("Not a PALINDRONE")

# TASK 3.
"""
WAP TO COUNT THE NUMBER OF STUDENTS WITH THE "A" GRADE IN THE FOLLOWING TUPLE.
["C" , "D", "A", "A","B","B","A"]
"""
list = ("C","D","A", "A","B","B","A")
print(list.count("A"))


# TASK 4.
# STORE THE ABOVE VALUES IN A LIST & SORT THEM FROM "A" TO "D"
data = ["d","c","b","a"]
print(data.sort())
print(data)