import pandas as pd

df = pd.read_csv("final_property_data.csv")
print("Available columns in dataset:\n")
print(df.columns.tolist())
