import ast, sys
print("Please enter a list of lists to be flattened")
input_str = input()
input_list = ast.literal_eval(input_str)
flat_list = []

for subLists in input_list:
    for item in subLists:
        flat_list.append(item)


print(flat_list)