import numpy as np
import pandas as pd
# Importing dataframes
data_frame=pd.read_csv('Sample2.csv',index_col=0,na_values=["??","???"])
print(data_frame)



# info for data frames
print(f'infor :-',data_frame.info())

# Convert Data Types
data_frame['MetColor'] = data_frame['MetColor'].astype('object')
data_frame['Automatic'] = data_frame['Automatic'].astype('object')


# Category Vs Object
print(data_frame['Automatic'].nbytes)

print(data_frame['Automatic'].astype('category').nbytes)

print(f'info',data_frame.info())

# Unique values
print(np.unique(data_frame['Doors']))

# Replace

print(data_frame['Doors'].replace('three' ,3,inplace=True))
print(data_frame['Doors'].replace('four' ,4,inplace=True))
print(data_frame['Doors'].replace('five' ,5,inplace=True))

data_frame['Doors'] = data_frame['Doors'].astype('int64')

print(np.unique(data_frame['Doors']))

# Count Missing Values
print(data_frame.isnull().sum())
print(data_frame['MetColor'].isnull().sum())

# Dealing with Missing values

data_frame2 = data_frame.copy()
data_frame3 = data_frame2.copy()

print(data_frame2['Age'].isnull().sum())
missing_values = data_frame2[data_frame2.isnull().any(axis=1)]
print(missing_values)

# Approaches to fill the missing values
# For Numerical Values
# Step 1
print(data_frame2.describe())
print(data_frame2['Age'].mean())
print(data_frame2['KM'].median())

# Step 2
data_frame2['Age'].fillna(data_frame2['Age'].mean(),inplace=True)
data_frame2['KM'].fillna(data_frame2['KM'].median(),inplace=True)

# For Categorical values

# Step 1
print(f'Dtypes of FuelType',data_frame2['FuelType'].dtypes)
print(data_frame2['FuelType'].value_counts())

# Step 2
data_frame2['FuelType'].fillna(data_frame2['FuelType'].value_counts().index[0],inplace=True)
print(data_frame2['FuelType'].value_counts())
data_frame2['MetColor'].fillna(data_frame2['MetColor'].mode()[0],inplace=True)
print(data_frame2.isnull().sum())

# filling all missing value with 1 shot
data_frame3 = data_frame3.apply(lambda x:x.fillna(x.mean()) if x.dtype == 'float' else x.fillna(x.value_counts().index[0]))
print(data_frame3.isnull().sum())