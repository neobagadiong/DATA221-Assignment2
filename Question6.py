import pandas, numpy

crimeStatDataFrame = pandas.read_csv('crime.csv')
crimeStatDataFrame["risk"] = numpy.where(crimeStatDataFrame['ViolentCrimesPerPop'] > 0.49, 'High-Crimes','LowCrime')

groupedByRiskDF = crimeStatDataFrame.groupby('risk').mean().round(4)

print(f"The high-crime group has an average unemployment rate of {groupedByRiskDF['PctUnemployed'].iloc[0] * 100:.02f}% and the low-crime group has an average unemployment rate of {groupedByRiskDF['PctUnemployed'].iloc[1] * 100:.02f}%.")