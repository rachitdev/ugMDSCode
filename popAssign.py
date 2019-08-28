import pandas as pd
import numpy as np
df = pd.read_csv("C:/Users/rachit/Downloads/popularity.csv")
col_shares = df[' shares']

#print(col_shares.max())
#print(df.describe())

#print(np.percentile(col_shares, 78))

# def calcPercentile():
#     for i in range(0, 10):
#         print(np.percentile(col_shares, i*10))
#
# print(calcPercentile())


mean = np.mean(col_shares, axis=0)
sd = np.std(col_shares, axis=0)
min_out = mean - 2 * sd
max_out = mean + 2 * sd

final_list = [x for x in col_shares if (x > min_out)]
final_list = [x for x in final_list if (x < max_out)]
df_1 = pd.DataFrame(final_list)
# print(np.std(df_1))
print(((len(col_shares) - len(df_1)) / len(col_shares)) * 100)
#print(df_1.mean())