# ====== FUNCTIONS TASKS ========
# WAF TO PRINT THE LENGTH OF A LIST. (LIST IS THE PARAMETER)
cities = ["delhi", "gurgaon", "noida", "mumbai"]
hero = ["thor", "batman","spiderman"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(hero)

# WAF TO PRINT THE ELEMENTS OF ALIST IN A SINGLE LINE. (LIST IS THE PARAMETER)
def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(hero)
print_list(cities)