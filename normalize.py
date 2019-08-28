import pandas as pd
pd.set_option('display.max_columns', 500)
colsToNormalize = ['Serial No.', 'GRE Score', 'TOEFL Score']
df = pd.read_csv("https://media-doselect.s3.amazonaws.com/generic/GVj4YrNpJwOvL7gBe2B53wJy/Admission_Predict.csv")


# Lambda function to normalize a dataset
df[colsToNormalize] = df[colsToNormalize].apply(lambda x: (x-x.min()) / (x.max()-x.min()))


# prints the whole dataset with the required columns normalized.
print(df.describe())