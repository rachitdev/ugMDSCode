# Set Operations
# Description
# In a school, there are total 20 students numbered from 1 to 20. You’re given three lists named ‘C’, ‘F’, and ‘H’,
# representing students who play cricket, football, and hockey, respectively. Based on this information,
# find out and print the following:
# 1. Students who play all the three sports
# 2. Students who play both cricket and football but don’t play hockey
# 3. Students who play exactly two of the sports
# 4. Students who don’t play any of the three sports
# Format:
# Input:
# 3 lists containing numbers (ranging from 1 to 20) representing students who play cricket, football and hockey
# respectively.
# Output:
# 4 different lists containing the students according to the constraints provided in the questions.

# Read the three input lists, i.e. 'C', 'F', and 'H'.
input_list = [[2, 5, 9, 12, 13, 15, 16, 17, 18, 19], [2, 4, 5, 6, 7, 9, 13, 16, 20], [1, 2, 5, 9, 10, 11, 12, 13, 15, 20]]
C = input_list[0]
F = input_list[1]
H = input_list[2]


# Function to remove the duplicates
def remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list


# all students
u = list(map(lambda x: x, range(1, 21)))


# students who don't play sports
x = (set(C)|set(F)|set(H))
y = remove(x)
d = list(set(u)-set(y))

# 1. Students who play all the three sports
u_s = set(u)-set(d)
sports3 = (set(C) & set(F) & set(H))
print(sorted(list(sports3)))

# 2. Students who play both cricket and football but don’t play hockey
C_F = u_s - set(H)
only_C = u_s - (set(F) & set(H))
only_F = u_s - (set(C) & set(H))
print(list(sorted(C_F - (only_C & only_F))))

# 3. Students who play exactly two of the sports
C_H = list(set(u_s)-set(F))
only_CH = list(set(C_H) & (set(C) | set(H)))
H_F = list(set(u_s)-set(C))
only_HF = list(set(H_F) & (set(H) | set(F)))
#print(remove(sorted(list(only_CF+only_CH+only_HF))))

# 4. Students who don’t play any of the three sports
print(d)









