import pandas as pd
studentStatsDataFrame = pd.read_csv('student.csv')
highEngagementStudentsDataFrame = studentStatsDataFrame[studentStatsDataFrame['studytime']]
print(studentStats)