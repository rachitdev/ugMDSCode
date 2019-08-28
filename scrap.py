import pandas as pd
pd.set_option('display.max_columns', 500)
df = pd.read_csv('https://media-doselect.s3.amazonaws.com/generic/wkyk2AWYdJbqgXoRo3Y8w42nX/test.csv')

input_list = [['Pclass', 'Age'], [3, 13]]
cols = input_list[0]#the columns to group the dataframe by
values = input_list[1]# The group to print


#Write your code here
df = df.groupby(cols[0]).get_group(values[0])
df = df.groupby(cols[1]).get_group(values[1])


print(df.head(5))


