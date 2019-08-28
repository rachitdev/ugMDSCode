import pandas as pd
pd.set_option('display.max_columns', 500)
url = "https://media-doselect.s3.amazonaws.com/generic/E4QbGd18ORJpbZZkndZ5bdKBn/googleplaystore_user_reviews.csv"
df = pd.read_csv(url)


numeric = df.groupby(df.select_dtypes(exclude=['float64', 'int64', 'float', 'int']).columns)
print(df(numeric).mean().head(5))