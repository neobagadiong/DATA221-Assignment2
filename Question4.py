import pandas as pd

studentStatsDataFrame = pd.read_csv('student.csv')

highEngagementStudentsDataFrame = (studentStatsDataFrame[studentStatsDataFrame['studytime'] > 2][studentStatsDataFrame['internet'] == 1][studentStatsDataFrame['absences'] <= 5])
highEngagementStudentsDataFrame.to_csv('high_engagement.csv',index=False)

print(f"There are {len(highEngagementStudentsDataFrame.index)} high engagement students and their average grade is {highEngagementStudentsDataFrame['grade'].mean():.2f}")