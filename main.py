print("Hello World")
print("Despicable AI")
print("Hello Mama")

<<<<<<< HEAD


import pandas as pd
file_path = ""
try:
    df = pd.read_csv(file_path)
except:
    print("file_path does not exist")
=======
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
>>>>>>> b36d0fda37bb0e59fc7995861f96283535e58d47
