import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("cleaned_titanic.csv")

# -----------------------------
# 1. Basic information
# -----------------------------
print("Dataset Shape:", df.shape)
print("\nData Types:")
print(df.dtypes)

print("\nStatistical Summary:")
print(df.describe())

# -----------------------------
# 2. Survival distribution
# -----------------------------
print("\nSurvival Counts:")
print(df["Survived"].value_counts())

plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="Survived")
plt.title("Survival Distribution")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Number of Passengers")
plt.savefig("survival_distribution.png")
plt.show()

# -----------------------------
# 3. Survival by gender
# -----------------------------
gender_survival = df.groupby("Sex")["Survived"].mean()
print("\nSurvival Rate by Gender:")
print(gender_survival)

plt.figure(figsize=(6, 4))
sns.barplot(data=df, x="Sex", y="Survived")
plt.title("Survival Rate by Gender")
plt.ylabel("Survival Rate")
plt.savefig("survival_by_gender.png")
plt.show()

# -----------------------------
# 4. Survival by passenger class
# -----------------------------
class_survival = df.groupby("Pclass")["Survived"].mean()
print("\nSurvival Rate by Passenger Class:")
print(class_survival)

plt.figure(figsize=(6, 4))
sns.barplot(data=df, x="Pclass", y="Survived")
plt.title("Survival Rate by Passenger Class")
plt.ylabel("Survival Rate")
plt.savefig("survival_by_class.png")
plt.show()

# -----------------------------
# 5. Age distribution
# -----------------------------
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="Age", bins=30, kde=True)
plt.title("Age Distribution of Passengers")
plt.xlabel("Age")
plt.ylabel("Number of Passengers")
plt.savefig("age_distribution.png")
plt.show()

# -----------------------------
# 6. Fare distribution
# -----------------------------
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="Fare", bins=30, kde=True)
plt.title("Fare Distribution")
plt.xlabel("Fare")
plt.ylabel("Number of Passengers")
plt.savefig("fare_distribution.png")
plt.show()

# -----------------------------
# 7. Correlation heatmap
# -----------------------------
numeric_df = df.select_dtypes(include="number")

plt.figure(figsize=(8, 6))
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("correlation_heatmap.png")
plt.show()

# -----------------------------
# 8. Survival by gender and class
# -----------------------------
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="Pclass", y="Survived", hue="Sex")
plt.title("Survival Rate by Passenger Class and Gender")
plt.ylabel("Survival Rate")
plt.savefig("survival_gender_class.png")
plt.show()

print("\nEDA completed successfully!")