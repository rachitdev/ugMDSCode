import pandas as pd
submissions = pd.read_csv('C:/Users/rachit/Downloads/grades.csv')
df = submissions['submit_time']
# new data frame with split value columns
df_dt = df.str.split("-", n=1, expand=True)

# making separate Date column from new data frame
df["Date"] = df_dt[0]

# making separate Time column from new data frame
df["Time"] = df_dt[1]
# Dropping old Name columns
#df.drop(columns=["submit_time"], inplace=True)

# If submitted on time column
#df["FirstDeadSub"] = df['Date'].dt.day

print(df_dt.head(10))