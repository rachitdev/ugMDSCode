import pandas as pd
df = pd.read_csv("C:/Users/rachit/Downloads/currencies.csv")

#print(df.head(5))

# retaining the rows having <= 5 NaNs
df = df[df.isnull().sum(axis=1) <= 2]
df = df.drop('Kuwaiti Dinar', axis=1)
# look at the summary again
print(round(100*(df.isnull().sum()/len(df.index)), 2))


corr = df.corr()
corr.style.background_gradient(cmap='coolwarm').set_precision(2)