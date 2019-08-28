import pandas as pd
import matplotlib.pyplot as plt

# the commonly used alias for seaborn is sns
import seaborn as sns

# set a seaborn style of your taste
sns.set_style("whitegrid")

# data
df = pd.read_csv("C:/Users/rachit/Downloads/PythonNotebooks/Session2+-+Plotting+Distributions/global_sales_data/market_fact.csv")

sns.distplot(df['Sales'][:1000], rug=True)
plt.show()