import pandas as pd
pd.set_option('display.max_columns', 500)
df = pd.read_csv('https://media-doselect.s3.amazonaws.com/generic/wkyk2AWYdJbqgXoRo3Y8w42nX/test.csv')
input_list = [['Pclass','Age'], [3,13]]
cols = input_list[0]#the columns to group the dataframe by
values = input_list[1]# The group to print
#Write your code here

df = df.groupby([cols[0], cols[1]])
df = df.apply(lambda row: row[df[cols[0]].isin([values[0]])])


print(df.head(5))