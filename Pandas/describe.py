import pandas as pd
data ={
    "Name": ["Pallavi", "Rahul", "Aman", "Sneha"],
    "Age" : [21,23,25,22],
    "Salary": [50000, 60000, 70000, 55000],
    "Performance Score": [50000, 70000,90000,60000],
    "City": ["Delhi", "Noida", "Agra", "Jaipur"]
}
df = pd.DataFrame(data)
print("Sample dataset")
print(df)
# print("Descriptive Statistics of the dataset")
# print(df.describe())
print('Shape: ', df.shape)
print ("Columns", df.columns)