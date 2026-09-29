# Task 2 – Exploratory Data Analysis (EDA)

## Objective

The objective of this task is to analyze the prepared Titanic dataset using statistical methods and data visualizations to identify useful patterns, relationships, and insights.

## EDA Performed

The following analyses were performed:

- Basic information about the dataset
- Survival distribution
- Survival analysis by gender
- Survival analysis by passenger class
- Age distribution analysis
- Fare distribution analysis
- Correlation analysis using a heatmap
- Survival analysis by gender and passenger class

## Visualizations

The EDA includes the following visualizations:

1. Survival Count
2. Survival by Gender
3. Survival by Passenger Class
4. Age Distribution
5. Fare Distribution
6. Correlation Heatmap
7. Survival by Gender and Class

## Key Insights

1. The dataset contains passengers with different survival outcomes, allowing survival patterns to be analyzed.

2. Survival outcomes differ between male and female passengers.

3. Passenger class is associated with different survival outcomes.

4. The dataset contains passengers from different age groups, showing variation in the age distribution.

5. Fare values vary between passengers, indicating differences in ticket prices.

6. The correlation heatmap helps identify relationships between numerical variables in the Titanic dataset.

7. Survival patterns can also be compared across different combinations of gender and passenger class.

## Files

- `cleaned_titanic.csv` – Prepared and cleaned Titanic dataset.
- `data_preparation.py` – Python code used for data preparation and cleaning.
- `eda_titanic.py` – Python code used for Exploratory Data Analysis and visualizations.
- `README.md` – Documentation for the project.

## Requirements

The project uses Python with the following libraries:

- pandas
- matplotlib
- seaborn

Install the required libraries using:

```bash
pip install pandas matplotlib seaborn

How to Run

Data Preparation
Run the data preparation script:
python data_preparation.py
This prepares and cleans the Titanic dataset.
Exploratory Data Analysis

Run the EDA script:

python eda_titanic.py
The script performs statistical analysis and generates visualizations including survival count, survival by gender, survival by passenger class, age distribution, fare distribution, correlation heatmap, and survival by gender and class.

Conclusion

EDA helps identify patterns, relationships, and distributions in the Titanic dataset. The analysis provides an understanding of survival patterns, passenger characteristics, and relationships between numerical variables. These findings can support further data analysis and machine learning work.