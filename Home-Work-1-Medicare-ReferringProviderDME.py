# Read data from a csv file
# import pandas module for use
print("Home work-1 Python Jan 28 2017 ")
import pandas as pd
from pandas import ExcelWriter

# Read csv or xls as data frame
df = pd.read_csv("Medicare_Referring_Provider_DMEPOS_PUF_CY2013.csv", low_memory=False)
print("Shape of Dataframe : ")
print(df.shape)  # size of the data
print("Data types are:")
print((df.dtypes))  # data types
print("Coulmns are:")
print(df.columns)  # column names

#df = df[["HCPCS Code","HCPCS Description","Number of Supplier Claims"]] # pick columns for the dataframe
df = df[["HCPCS Code","HCPCS Description"]] # pick columns for the dataframe

#MedicareDME_detail = df.groupby("Referring Provider Street Address 1")
#MedicareDME_detail = df.groupby("Referring NPI")
MedicareDME_detail = df.groupby("HCPCS Code")
df = MedicareDME_detail.sum()

print("New dataframe ")
print(df)

# save to new CSV file
df.to_csv('MedicareDME_provider_detail.csv', encoding='utf-8')
print("New csv file saved")
# save to xls

#writer = ExcelWriter('products.xlsx')
#df.to_excel(writer, 'Sheet1')
#writer.save()
