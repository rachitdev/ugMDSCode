# For the analysis below, use Data I-B. You can also use Data I-B along with Data I-A if required.
# Also, perform the analysis only for the duration 2014-15.
# Filter out the union territories (Delhi, Chandigarh, Andaman and Nicobar Islands, etc.) for further analysis,
# as they are governed directly by the centre, not state governments.
# Plot the GDP per capita for all the states.
# Identify the top 5 and the bottom 5 states based on the GDP per capita.
# Find the ratio of the highest per capita GDP to the lowest per capita GDP.

# Packages required
from IPython.display import Image
import matplotlib.pyplot as plt
import pandas as pd
import glob, os
import warnings
import numpy as np

warnings.filterwarnings("ignore")

# Path where all the files are stored
path = r'C:\Users\rachit\Downloads\GDP_Ass\data\GSVA_all'
# Reading all the paths
all_files = glob.glob(path + r"/*.csv")

# Empty list to add all the dataframes
l = []

# Loop to read each file with the path given in the filename variable.
for filename in all_files:
    # Reading each file as a pandas dataframe
    data = pd.read_csv(filename, index_col=None, header=0, encoding="latin-1")
    # As we have to perform the analysis only for the duration 2014-15.
    data = data[['Item','2014-15']]
    # Transpose the data
    data = data.T
    # Taking the header row
    new_header = data.iloc[0] #grab the first row for the header
    data = data[1:] #take the data minus the header row
    # Assign the new header
    data.columns = new_header
    # Add the section name from the filename
    data['State'] = filename.split('-')[1].split('_')[0]
    # Append the final DF to the list
    l.append(data)

# Creating a final DF by joining all the df's in the list li
df = pd.concat(l, axis=0, ignore_index=True)

# Bringing state names as the first column
state_Names = df['State'] # List to save the content of column state.
df.drop(labels=['State'], axis=1,inplace = True) # Dropping off the column.
df.insert(0, 'State', state_Names) # Reinserting the column.

# Filter out the union territories (Delhi, Chandigarh, Andaman and Nicobar Islands, etc.) for further analysis,
# as they are governed directly by the centre, not state governments.

df_1 = df[df.State != 'Delhi']
df_1 = df_1[df_1.State != 'Chandigarh']
df_1 = df_1[df_1.State != 'Puducherry']

# Getting the required data to plot the graph for the GDP per capita for all the states.
df_2 = df_1[['State', 'Per Capita GSDP (Rs.)']]
df_3 = df_2.T

# Taking the header row
new_headerT = df_3.iloc[0] # grab the first row for the header
df_3 = df_3[1:] # take the data minus the header row

# Assign the new header
df_3.columns = new_headerT

# Bar plot code starts from here:
A = list(df_3.columns) # list of states which will be shown on the x axis.

# set height of bar
SBars = df_3.iloc[[0], 0:].values[0] # SBars is for the year 2015-16

# new bar width
barWidth = 0.3

# Set position of bar on X axis
r = np.arange(len(SBars))

# Make the bar plots for 2015-16.
plt.bar(r, SBars, color='#2d7f5e', width=barWidth, edgecolor='white')

# Add xticks on the middle of the group bars
plt.xlabel('States', fontweight='bold') # X label is set as states.
plt.ylabel('Per Capita GSDP (Rs.)', fontweight='bold') # Y label is set as GSDP in crores.

# Setting the x.ticks for each bar.
plt.xticks([(r-0.3) + barWidth for r in range(len(SBars))], [A[0], A[1], A[2], A[3], A[4], A[5], A[6], A[7], A[8], A[9],
                                                          A[10], A[11], A[12], A[13], A[14], A[15], A[16], A[17], A[18],
                                                          A[19], A[20], A[21], A[22], A[23], A[24], A[25], A[26], A[26]])

# Create legend & Show graphic
plt.rcParams["figure.figsize"] = 30, 15
plt.show() # This generates the plot which shows the GDP of the states for year 2015-16 which are available and not NaN.
# Bar plot code ends here.