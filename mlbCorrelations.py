# Creates a graph to display correlation between 2 mlb statistics
# Downlaod csv files from Baseball Savant

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
from csv import reader

file = str(input('Enter the file name: '))
xVarName = str(input('What is the first variable: '))
xVarHeader = str(input('Enter the first variable header: '))
xVarCol = int(input('Enter the column number of the first variable: '))
yVarName = str(input('What is the second variable: '))
yVarHeader = str(input('Enter the second variable header: '))
yVarCol = int(input('Enter the column number of the second variable: '))

data = pd.read_csv(str(file))

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
		xVar.append(float(row[xVarCol - 1]))
		yVar.append(float(row[yVarCol - 1]))
xVar.pop(0)
yVar.pop(0)

# Calculate the stats data for the two variables 
importantStats = linregress(xVar,yVar)

# Plot the data
data.plot.scatter(x=str(xVarHeader),y=str(yVarHeader),s=3,c='blue')

# Print the R value on the plot (use cursor on graph to adjust x & y values in code below)
# plt.text(61,.39,'R-value:' + str(round(importantStats[2],3)))

# Format the plot
plt.title(str(yVarName) + ' vs ' + str(xVarName),c='red')
plt.xlabel(str(xVarName),c='red')
plt.ylabel(str(yVarName),c='red')

# Show the plot
plt.show()

# Analyze Stats if Necessary
print('\n')
print(importantStats)