import pandas as pd

# Read csv files
data_csv = pd.read_csv('sample.csv', index_col=0,na_values=["??", "###"])
print(data_csv)
# Attributes of data
print(data_csv.index)
print(data_csv.columns)
print(data_csv.size)
print(data_csv.shape)
print(data_csv.memory_usage())
print(data_csv.ndim)

# Indexing and selecting data
print(data_csv.head(7))
print(data_csv.tail(7))
print(data_csv.at[3,'activity'])
print(data_csv.iat[3,2])
print(data_csv.loc[:,:])


# Read Excel files
data_excel = pd.read_excel('sample.xlsx',sheet_name='Iris_data')
print(data_excel)

# Read Text format
data_txt = pd.read_table('sample.txt',delimiter="\t")
print(data_txt)