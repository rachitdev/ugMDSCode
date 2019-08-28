import pandas as pd
import sys,ast

input_list = [['c1','c2','c3'],[1,2,3],[4,5,6],[7,8,9]]


data = {input_list[0][0]:[input_list[1][0], input_list[2][0], input_list[3][0]], input_list[0][1]:[input_list[1][1], input_list[2][1], input_list[3][1]], input_list[0][2]:[input_list[1][2], input_list[2][2], input_list[3][2]]}
df = pd.DataFrame(data)
#print(df)
print(df.describe())