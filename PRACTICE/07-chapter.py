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

# WAF TO FIND THE FACTORIAL OF N. (N IS THE PARAMETER)
n = 5

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
        print(fact)

cal_fact(5)

# WAF TO CONVERT USD TO INR
def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD =", inr_val, "INR")

converter(8)