#pip install pandas

import pandas as pd

# series -> 1D
dt = [10,20,30,40,50]
ser = pd.Series(dt)
print(ser)

#dataframes -> 2D
dt = {
    'Name' : ['Alice', 'Bob', 'Charlie'],
    'Age' : [25, 30, 35],
    'City': ['NY' , 'San Fransisco', 'Chicago']
}

df=pd.DataFrame(dt)
print(df)



#df=pd.read_csv('data.csv')
#print(df)

# Read Excel Files
# df = pd.read_excel('data.xlsx', sheet_name = 'Sheet1')
# print(df)

selected_data = df.loc[df['City'] == 'NY', ['Name', 'Age']]
print(selected_data)

selected_data1 = df.loc[df['Name'] == 'Bob', ['City', 'Age']]
print(selected_data1)

grouped_data = df.groupby('Name')['Age'].mean()
print(grouped_data)
