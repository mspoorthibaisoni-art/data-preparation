 import pandas as pd

# Load the Titanic dataset
input_file = "Titanic-Dataset.csv"
output_file = "cleaned_titanic.csv"

df = pd.read_csv(input_file)

# Display basic information
print("Original dataset shape:", df.shape)
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing Age values with the median
if "Age" in df.columns:
    df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill missing Embarked values with the mode
if "Embarked" in df.columns:
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Fill missing Fare values with the median
if "Fare" in df.columns:
    df["Fare"] = df["Fare"].fillna(df["Fare"].median())

# Drop Cabin because it contains many missing values
if "Cabin" in df.columns:
    df = df.drop(columns=["Cabin"])

# Save the cleaned dataset
df.to_csv(output_file, index=False)

print("\nCleaned dataset shape:", df.shape)
print("\nMissing values after cleaning:")
print(df.isnull().sum())
print(f"\nCleaned dataset saved as: {output_file}")