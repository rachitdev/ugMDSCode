from functools import reduce
print("Please input the number whose factorial is required to be calculated: ")
n = int(input())


# Function to define factorial handling 0 as well.
def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return reduce(lambda x, y: x*y, range(1, (n+1)))


print(factorial(n))