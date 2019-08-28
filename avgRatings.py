import pandas as pd
cust_rating = pd.read_csv('https://query.data.world/s/ILc-P4llUraMaYN6N6Bdw7p6kUvHnj')

cust_rating['avg_rating'] = round(cust_rating.iloc[:, [2, 3, 4]].mean(axis=1))

print(cust_rating.head(10))