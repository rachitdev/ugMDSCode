array=[1,2,3,4,5,6,7,8,9]
print("Please enter a positive, single decimal digit floating number: ")
n = float(input())

for x in range(0, len(array)):
    if 1 > n-array[x] > 0.5:
        print(array[x+1])

    if 0 < n-array[x] < 0.5:
        print(array[x])
