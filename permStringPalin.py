from itertools import permutations
string = input()
l = []      #Empty list to append permutations of a given string.
out = []    #Empth list to append output of yes or no if the element is a palindrome or not.
# Get all permutations of string 'ABC'
permList = permutations(string)
# append all permutations to empty list l.
for perm in list(permList):
    a = ''.join(perm)
    l.append(a)
# Append yes if palindrome is possible in out or no if not.
for x in l:
    r = x[::-1] # reverse of x is r here.
    if x == r:
        out.append("Yes")
    else:
        out.append("No")

# Checking for palindrome possibility being recorded in out list.
if "Yes" in out:
    print("Yes")
else:
    print("No")