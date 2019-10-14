import pandas as pd

# Opens and reads a csv file
df = pd.read_csv('biostats_test.csv')

# Prints all data from the csv file
print(df)

# Prints the first 5 rows from the csv file
print(df.head(5))

# Opens and reads a xlsx file
df_xlsx = pd.read_excel('people_test.xlsx')

# Prints all data from the xlsx file
print(df_xlsx)

# Prints the first 5 rows from the csv file
print(df_xlsx.head(5))