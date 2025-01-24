print("Hello World")
print("Despicable AI")
print("Hello Mama")

import pandas as pd
df= pd.read_csv(r'C:\Users\SRCD\Desktop\Devops Git\github_demo\ag_news.csv')
df.head()

# Perform summary statistics
summary_stats = df.describe()
print("Summary Statistics:")
print(summary_stats)

# Check for missing values
missing_values = df.isnull().sum()
print("Missing Values:")
print(missing_values)

# Check for duplicates
duplicates = df.duplicated().sum()
print("Number of Duplicates:")
print(duplicates)
