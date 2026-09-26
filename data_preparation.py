import pandas as pd

# Public dataset: Titanic dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

# Load dataset
df = pd.read_csv(url)

print("Original dataset shape:", df.shape)
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Clean missing values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
df["Fare"] = df["Fare"].fillna(df["Fare"].median())

# Convert data types
df["Survived"] = df["Survived"].astype(int)
df["Pclass"] = df["Pclass"].astype(int)

# Remove duplicate rows
df = df.drop_duplicates()

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nCleaned dataset shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())

# Save cleaned dataset
df.to_csv("cleaned_titanic.csv", index=False)

print("\nCleaned dataset saved as cleaned_titanic.csv")