n = int(input())#find the sum of primes from 2 to n
l = []
for num in range(0, n + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            l.append(num)
a = sum(x for x in l)
print(a)