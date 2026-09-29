import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned Titanic dataset
df = pd.read_csv("cleaned_titanic.csv")

# 1. Basic information
print("Dataset shape:", df.shape)
print("\nDataset information:")
df.info()

print("\nStatistical summary:")
print(df.describe())

# 2. Survival distribution
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="Survived")
plt.title("Survival Distribution")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Number of Passengers")
plt.tight_layout()
plt.show()

# 3. Survival by gender
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="Sex", hue="Survived")
plt.title("Survival by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of Passengers")
plt.tight_layout()
plt.show()

# 4. Survival by passenger class
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="Pclass", hue="Survived")
plt.title("Survival by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Number of Passengers")
plt.tight_layout()
plt.show()

# 5. Age distribution
plt.figure(figsize=(7, 4))
sns.histplot(data=df, x="Age", bins=30, kde=True)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Passengers")
plt.tight_layout()
plt.show()

# 6. Fare distribution
plt.figure(figsize=(7, 4))
sns.histplot(data=df, x="Fare", bins=30, kde=True)
plt.title("Fare Distribution")
plt.xlabel("Fare")
plt.ylabel("Number of Passengers")
plt.tight_layout()
plt.show()

# 7. Correlation heatmap
numeric_df = df.select_dtypes(include="number")

plt.figure(figsize=(8, 6))
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

# 8. Survival by gender and class
g = sns.catplot(
    data=df,
    x="Sex",
    hue="Survived",
    col="Pclass",
    kind="count",
    height=4,
    aspect=0.9
)

g.set_axis_labels("Gender", "Number of Passengers")
g.set_titles("Passenger Class {col_name}")
g.fig.suptitle("Survival by Gender and Class", y=1.05)

plt.show()

# Survival percentage by gender and passenger class
gender_class = pd.crosstab(
    [df["Sex"], df["Pclass"]],
    df["Survived"],
    normalize="index"
) * 100

print("\nSurvival percentage by gender and passenger class:")
print(gender_class)