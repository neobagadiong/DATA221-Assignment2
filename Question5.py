import pandas 
import numpy
studentStatsDataFrame = pandas.read_csv('student.csv')
#print (studentStatsDataFrame)

studentStatsDataFrame['grade_band'] = numpy.select([(studentStatsDataFrame['grade'] >= 15),(studentStatsDataFrame['grade'] >= 10),(studentStatsDataFrame['grade'] <= 9)],['High','Medium','Low'],default='None')

#print (studentStatsDataFrame)

studentStatsSummaryDataFrame = pandas.DataFrame(index=studentStatsDataFrame['grade_band'].unique(),columns=['student_count','average_absences','internet_access'])

print(len(studentStatsDataFrame[studentStatsDataFrame['grade_band'] == 'None'].index))

for gradeBand in studentStatsSummaryDataFrame.index:
    studentStatsSummaryDataFrame.at[gradeBand,'student_count'] = len(studentStatsDataFrame[studentStatsDataFrame['grade_band'] == gradeBand].index)
    studentStatsSummaryDataFrame.at[gradeBand,'average_absences'] = round(studentStatsDataFrame[studentStatsDataFrame['grade_band'] == gradeBand]['absences'].mean(),2)
    studentStatsSummaryDataFrame.at[gradeBand,'internet_access'] = round(studentStatsDataFrame[studentStatsDataFrame['grade_band'] == gradeBand]['internet'].mean(),2)

studentStatsSummaryDataFrame.index
studentStatsSummaryDataFrame.to_csv('student_bands.csv',index_label='')