import pandas as pd
df = pd.read_csv("https://media-doselect.s3.amazonaws.com/generic/BgyRrKq0xex8B0N3GJxbXv5WZ/test.csv")
col1 = input("Sex")
col2 = input("Name")


def df_column_switch(df, col1, col2):
    i = list(df.columns)
    a, b = i.index(col1), i.index(col2)
    i[b], i[a] = i[a], i[b]
    df = df[i]
    return df


print(df_column_switch(df, col1, col2).head(3))