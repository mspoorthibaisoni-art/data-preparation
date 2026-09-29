# Task 2 – Exploratory Data Analysis (EDA)

## Objective

The objective of this task is to analyze the prepared Titanic dataset using statistical methods and data visualizations to identify useful patterns, relationships, and insights that can support further analysis and machine learning.

## EDA Performed

The following analyses were performed:

- Basic information about the dataset
- Statistical summary of numerical variables
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

1. **Survival varies between passengers.**  
   The survival distribution shows that passengers belong to two different outcome groups: survived and did not survive. This makes `Survived` an important target variable for predictive modeling.

2. **Gender is strongly associated with survival.**  
   The survival-by-gender analysis shows different survival patterns between male and female passengers. Therefore, `Sex` can be an important feature for a machine learning model.

3. **Passenger class is associated with survival.**  
   Survival patterns differ across first, second, and third passenger classes. Therefore, `Pclass` can provide useful information when predicting survival.

4. **Age shows variation across passengers.**  
   The age distribution contains passengers from different age groups. Age may therefore contribute useful information to a survival prediction model.

5. **Fare values vary considerably between passengers.**  
   The fare distribution shows differences in ticket prices. Fare can provide additional information about passenger characteristics and may be useful for modeling.

6. **Numerical variables have different relationships.**  
   The correlation heatmap helps identify relationships between numerical variables such as `Survived`, `Pclass`, `Age`, `SibSp`, `Parch`, and `Fare`. This can help during feature selection and model preparation.

7. **Gender and passenger class together provide additional information.**  
   Comparing survival across both gender and passenger class shows that survival patterns can change when multiple features are considered together. This is useful when building a model using more than one predictor.

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

The Exploratory Data Analysis identifies important patterns and relationships in the Titanic dataset. Gender, passenger class, age, fare, and combinations of features provide useful information about survival outcomes. These findings can support feature selection, predictive modeling, and further machine learning analysis.