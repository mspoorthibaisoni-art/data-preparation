import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned Titanic dataset
df = pd.read_csv("cleaned_titanic.csv")

# Display basic information
print("First 5 rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

# Insight 1: Survival count
print("\nSurvival Count:")
print(df["Survived"].value_counts())

plt.figure(figsize=(6, 4))
df["Survived"].value_counts().plot(kind="bar")
plt.title("Survival Count")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Number of Passengers")
plt.show()

# Insight 2: Survival by gender
if "Sex" in df.columns:
    print("\nSurvival by Gender:")
    print(pd.crosstab(df["Sex"], df["Survived"]))

    pd.crosstab(df["Sex"], df["Survived"]).plot(kind="bar")
    plt.title("Survival by Gender")
    plt.xlabel("Gender")
    plt.ylabel("Number of Passengers")
    plt.show()

# Insight 3: Survival by passenger class
if "Pclass" in df.columns:
    print("\nSurvival by Passenger Class:")
    print(pd.crosstab(df["Pclass"], df["Survived"]))

    pd.crosstab(df["Pclass"], df["Survived"]).plot(kind="bar")
    plt.title("Survival by Passenger Class")
    plt.xlabel("Passenger Class")
    plt.ylabel("Number of Passengers")
    plt.show()

# Insight 4: Age distribution
if "Age" in df.columns:
    plt.figure(figsize=(7, 4))
    df["Age"].plot(kind="hist", bins=20)
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.show()

# Insight 5: Fare distribution
if "Fare" in df.columns:
    plt.figure(figsize=(7, 4))
    df["Fare"].plot(kind="hist", bins=20)
    plt.title("Fare Distribution")
    plt.xlabel("Fare")
    plt.ylabel("Frequency")
    plt.show()

print("\nEDA completed successfully!")