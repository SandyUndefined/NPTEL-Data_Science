import pandas as pd

# Read csv files
data_csv=pd.read_csv('sample.csv', index_col=0,na_values=["??","###"])
print(data_csv)

# Read Excel files
data_excel=pd.read_excel('sample.xlsx',sheet_name='Iris_data')
print(data_excel)

# Read Text format
data_txt=pd.read_table('sample.txt',delimiter="\t")
print(data_txt)