# Read data from a csv file
# import pandas module for use
print("Home work-1 Python Jan 28 2017 ")
import pandas as pd
from pandas import ExcelWriter

# Read csv or xls as data frame
df = pd.read_csv("Revalidation_Due_Date_List.csv", low_memory=False)
print("Shape of Dataframe : ")
print(df.shape)  # size of the data
print("Data types are:")
print((df.dtypes))  # data types
print("Coulmns are:")
print(df.columns)  # column names

df = df[["Enrollment ID","First Name","Receiving Benefits Reassignments"]]  # pick columns for the dataframe

revalidate = df.groupby("Enrollment ID")

df = revalidate.sum()

print("New dataframe ")
print(df)

# save to new CSV file
df.to_csv('HW1-Revalidate-DueDate-output.csv', encoding='utf-8')
print("New csv file saved")
# save to xls

#writer = ExcelWriter('products.xlsx')
#df.to_excel(writer, 'Sheet1')
#writer.save()
