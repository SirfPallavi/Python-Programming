import pandas as pd
data ={
    "Name": ["Pallavi", None, "Aman", "Sneha"],
    "Age" : [21,23,None,22],
    "Salary": [None, 60000, 70000, 55000],
    "Performance Score": [50000, 70000,90000,60000],
    "City": ["Delhi", "Noida", "Agra", "Jaipur"]
}

df = pd.DataFrame(data)
print(df)

print(df.isnull())