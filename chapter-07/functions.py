# ====== FUNCTIONS IN PYTHON =======
# CREATE OUR FIRST FUNCTION
def calc_sum(a,b):
    sum = a + b
    print(sum)
    return sum

calc_sum(7,10)
calc_sum(10,70)
calc_sum(12,17)

# MULTIPLICATION FUNCTION
# def mult_sum(x,y):
#     return x * y

# mul = mult_sum(20,99)
# print(mul)

# PRINT HELLO FUNCTION
def print_hello():
    print("Hello")

print_hello()

# average of 3 numbers

def calc_avg(x,y,z):
    sum = x + y + z
    avg = sum / 3
    print(avg)
    return avg
calc_avg(99,98,97)