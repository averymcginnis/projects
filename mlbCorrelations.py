# Creates a graph to display correlation between 2 mlb statistics
# Downlaod csv files from Baseball Savant with 2 different stats

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
from csv import reader

# CSV file name
file = str(input('Enter the file name: '))
# Exact column heading from csv file
xVarHeader = str(input('Enter the first variable header: '))
# Exact column heading from csv file
yVarHeader = str(input('Enter the second variable header: '))

data = pd.read_csv(str(file))

xCol = data.columns.to_list().index(xVarHeader) + 1
yCol = data.columns.to_list().index(yVarHeader) + 1

# Make a list of the x and y variables
xVar = []
yVar = []
count = 0
with open(str(file), 'r') as read_obj:
	csv_reader = reader(read_obj)
	for row in csv_reader:
		if count == 0:
			count += 1
			continue
		xVar.append(float(row[xCol - 1]))
		yVar.append(float(row[yCol - 1]))
xVar.pop(0)
yVar.pop(0)

# Calculate the stats data for the two variables 
importantStats = linregress(xVar,yVar)

# Plot the data
data.plot.scatter(x=str(xVarHeader),y=str(yVarHeader),s=3,c='blue')

# Print the R value on the plot (use cursor on graph to adjust x & y values in code below)
# plt.text(61,.39,'R-value:' + str(round(importantStats[2],3)))

# Format the plot
plt.title(str(yVarHeader) + ' vs ' + str(xVarHeader),c='red')
plt.xlabel(str(xVarHeader),c='red')
plt.ylabel(str(yVarHeader),c='red')

# Show the plot
plt.show()

# Analyze Stats if Necessary
print('\n')
print(importantStats)
