import pandas as pd
data ={
    "Name": ["Pallavi", "Rahul", "Aman"],
    "Age" : [21,23,25],
    "City": ["Delhi", "Noida", "Agra"]
}

df = pd.DataFrame(data)
print('Displaying the info of the dataset')
print(df.info())