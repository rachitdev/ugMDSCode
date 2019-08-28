# Part-1-A of GDP Assignment.
# First question description:
# Removal of rows: '(% Growth over the previous year)' and 'GSDP - CURRENT PRICES (` in Crore)' for the year 2016-17.
# Importing packages required
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
# Reading csv file as a pandas dataframe
path = r"C:\Users\rachit\Downloads\GDP_Ass\data\GSDP_comb\ab40c054-5031-4376-b52e-9813e776f65e.csv"
df = pd.read_csv(path)
# Renaming columns as some state names have been changed to fit the plot later.
df.rename(columns={'Items  Description': 'Items', 'West Bengal1': 'W.B.', 'Andhra Pradesh ': 'Andhra',
                   'Arunachal Pradesh': 'Arunachal', 'Himachal Pradesh': 'H.P.', 'Jammu & Kashmir': 'J&K',
                   'Madhya Pradesh': 'M.P.', 'Tamil Nadu': 'T.N.', 'Uttar Pradesh': 'U.P.',
                   'Andaman & Nicobar Islands': 'A&N', 'Chhattisgarh': 'Chat*garh', 'Karnataka': 'K*taka',
                   'Maharashtra': 'M*tra', 'Meghalaya': 'M*laya', 'Nagaland': 'N*land', 'Puducherry': 'P*cherry',
                   'Uttarakhand': 'U.K.'}, inplace=True)
# Dropping the required rows i.e. (% Growth over the previous year) and GSDP - CURRENT PRICES (` in Crore)
df_1 = df[df.Items != '(% Growth over previous year)'] # All rows with label (% Growth over the previous year) dropped
# df = df.drop(index = 5, axis = 0)
df_1 = df_1[df_1.Duration != '2016-17'] # Row with label 2016-17 is dropped here.
# print(df_1) # Answer to the first question in Part-1-A of GDP Assignment.

# Second Question description:
# Calculate the average growth of states over the duration 2013-14, 2014-15 and 2015-16 by taking the mean of the row
# '(% Growth over previous year)'. Compare the calculated value and plot it for the states.
# Make appropriate transformations if necessary to plot the data. Report the average growth rates of the various states:
# 1. Which states have been growing consistently fast, and which ones have been struggling?
# 2. Curiosity exercise - what has been the average growth rate of your home state, and how does it compare to the
# national average over this duration?

# Removing the unwanted rows for the second question.
df_2 = df[df.Items != 'GSDP - CURRENT PRICES (` in Crore)']
df_2 = df_2[df_2.Duration != '2012-13']
df_2 = df_2[df_2.Duration != '2016-17']
df_2 = df_2.drop('W.B.', axis=1) # Dropping the west bengal column as it has no values
df_2 = df_2.drop('Items', axis=1) # Dropping Items column as we need to take the mean
df_2 = df_2.drop('All_India GDP', axis=1) # Dropping this column as it is no state.
# print(df_2.mean(axis=1)) # Prints the mean all the states and gives the agg value of GDP growth of India.
india_grow = list(df_2.mean(axis=1)) # Calculating the mean gdp and storing it in the list.
india_growth = [round(x, 2) for x in india_grow] # Rounds off the values to 2 decimal places.
df_2['India'] = india_growth # Adding the India column to print the mean GDP
# print(df_2) # Prints the updated dataframe with Mean GDP as India GDP. This will be used to plot the figure.

# Bar plot code starts from here:
H = list(df_2.columns) # list of states which will be shown on the x axis.

# set width of bar
barWidth = 0.30

# set height of bar
bars1 = df_2.iloc[[0], 1:].values[0] # bars1 is for the year 2013-14
bars2 = df_2.iloc[[1], 1:].values[0] # bars2 is for the year 2014-15
bars3 = df_2.iloc[[2], 1:].values[0] # bars3 is for the year 2015-16

# Set position of bars on X axis
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

# Make the bar plots for all the required years.
plt.bar(r1, bars1, color='#7f6d5f', width=barWidth, edgecolor='white', label='2013-14')
plt.bar(r2, bars2, color='#557f2d', width=barWidth, edgecolor='white', label='2014-15')
plt.bar(r3, bars3, color='#2d7f5e', width=barWidth, edgecolor='white', label='2015-16')

# Add xticks on the middle of the group bars
plt.xlabel('States', fontweight='bold') # label is set as states

# Setting the x.ticks for each bar.
plt.xticks([r + barWidth for r in range(len(bars1))], [H[1], H[2], H[3], H[4], H[5], H[6], H[7], H[8], H[9], H[10],
                                                       H[11], H[12], H[13], H[14], H[15], H[16], H[17], H[18], H[19],
                                                       H[20], H[21], H[22], H[23], H[24], H[25], H[26], H[27], H[28],
                                                       H[29], H[30], H[31], H[32], H[33]])

# Create legend & Show graphic
plt.rcParams["legend.fontsize"] = 20
plt.rcParams["legend.handlelength"] = 4
plt.rcParams['figure.dpi'] = 200
plt.legend()
plt.rcParams["figure.figsize"] = 200, 100
# plt.show() # This generates the plot which gives the exact picture of growth of states as well as our country.
# Bar plot code ends here.

# Second Question description continued:
# 1. Which states have been growing consistently fast, and which ones have been struggling?

# Answer 1: Andhra Pradesh has been growing consistently as compared to all the other states and UTs. Meghalaya and
# Mizoram had a spike growth in 2014-15 but it declined as an aberration in next year. Telangana ,Madhya Pradesh,
# Gujrat are consistent in their performance with a little change. Jammu and Kashmir gave a spike in the year 2015-16
# and we can say that it grew well from the previous year. Interesting to see that Goa had a negative growth initially
# and later it picked up.

# 2. Curiosity exercise - what has been the average growth rate of your home state, and how does it compare to the
# national average over this duration?
# Answer 2: My home state is Delhi. It compared fairly against India. From 2013-15 it was equivalent to India but in the
# next year it was better than India.

# Third Question description:
# Plot the total GDP of the states for the year 2015-16:
# Identify the top 5 and the bottom 5 states based on total GDP.

df_1 = df_1[df_1.Duration != '2011-12'] # Row with label 2011-12 is dropped here.
df_1 = df_1[df_1.Duration != '2012-13'] # Row with label 2012-13 is dropped here.
df_1 = df_1[df_1.Duration != '2013-14'] # Row with label 2013-14 is dropped here.
df_1 = df_1[df_1.Duration != '2014-15'] # Row with label 2014-15 is dropped here.
df_1 = df_1.drop('Items', axis=1) # dropping column as it won't be used in plot.
df_1 = df_1.drop('Duration', axis=1) # dropping column as it won't be used in plot.
df_1 = df_1.drop('All_India GDP', axis=1) # dropping column as it won't be used in plot.
df_1 = df_1.dropna(axis=1) # dropping columns with all null values

# Bar plot code starts from here:
A = list(df_1.columns) # list of states which will be shown on the x axis.

# set height of bar
bars4 = df_1.iloc[[0], 1:].values[0] # bars4 is for the year 2015-16

# Set position of bar on X axis
r4 = np.arange(len(bars4))

# Make the bar plots for 2015-16.
plt.bar(r4, bars4, color='#2d7f5e', width=barWidth, edgecolor='white')

# Add xticks on the middle of the group bars
plt.xlabel('States', fontweight='bold') # X label is set as states.
plt.ylabel('GSDP in Crores', fontweight='bold') # Y label is set as GSDP in crores.

# Setting the x.ticks for each bar.
plt.xticks([(r-0.3) + barWidth for r in range(len(bars4))], [A[1], A[2], A[3], A[4], A[5], A[6], A[7], A[8], A[9], A[10],
                                                          A[11], A[12], A[13], A[14], A[15], A[16], A[17], A[18], A[19],
                                                          A[20], A[21], A[22]])

# Create legend & Show graphic
plt.rcParams["legend.fontsize"] = 25
plt.rcParams["legend.handlelength"] = 4
plt.legend()
plt.rcParams["figure.figsize"] = 30, 15
plt.show() # This generates the plot which shows the GDP of the states which are available and not NaN.
# Bar plot code ends here.