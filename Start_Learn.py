import pandas as pd

#df = pd.read_excel('student_data.xlsx')
#df = pd.read_excel('student_data.xlsx', sheet_name='Data_2')
#df = pd.read_excel('student_data.xlsx', usecols=['Name', 'Age'])
df1 = pd.read_excel('student_data.xlsx', sheet_name='Data_1')
df2 = pd.read_excel('student_data.xlsx', sheet_name='Data_2')
comparison = pd.merge(df1, df2, how='outer', indicator=True)
both = comparison[comparison['_merge'] == 'both']
#only_sheet1 = comparison[comparison['_merge'] == 'left_only']
#print(both)
#print(only_sheet1)
#print(df)
subject =df1['subject']
print(subject)
marks =df1['marks']
print(marks)