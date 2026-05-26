import pandas as pd

data = {
    "Name": ["Basha", "Abdul", "Asheek", "Mabasha", "Jani"],
    "Age": [23, 30, 22, 35, 28],
    "City": ["Hyderabad", "Delhi", "Guntur", "Chennai", "Bangalore"],
    "Salary": [25000, 40000, 22000, 50000, 35000]
}

df = pd.DataFrame(data)

print("Original DataFrame:\n", df)

print("\n1. Select single column (Name):")
print(df["Name"])

print("\n2. Select multiple columns (Name, Salary):")
print(df[["Name", "Salary"]])

print("\n3. Select first 3 rows using iloc:")
print(df.iloc[0:3])

print("\n4. Select rows 1 to 3 and columns Name & City:")
print(df.loc[1:3, ["Name", "City"]])

print("\n5. Employees with Salary > 30000:")
print(df[df["Salary"] > 30000])

print("\n6. Age > 25 and Salary > 30000:")
print(df[(df["Age"] > 25) & (df["Salary"] > 30000)])