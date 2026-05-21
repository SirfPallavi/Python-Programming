import pandas as pd

# Load dataset
df = pd.read_csv(
    "Pandas/QS_World_University_Rankings_2025_Top_global_universities (1).csv",
    encoding='latin1'
)

# Display first 5 rows
df.head()