import pandas as pd 
csv_file_path = 'C:\\ML_Projects\\sample_data.csv' 
excel_file_path = 'C:\\ML_Projects\\sample_data.xlsx'

data_csv = pd.read_csv(csv_file_path) 
print("CSV File Data:") 
print(data_csv) 
 
data_excel = pd.read_excel(excel_file_path) 
print("\nExcel File Data:") 
print(data_excel) 
 
print("\nData Descriptions:") 
print("CSV Data Description:") 
print(data_csv.describe()) 

print("\nExcel Data Description:") 
print(data_excel.describe())

print("\nData Types in CSV File:") 
print(data_csv.dtypes) 

print("\nData Types in Excel File:") 
print(data_excel.dtypes) 
