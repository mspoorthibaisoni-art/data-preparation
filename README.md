## Exploratory Data Analysis

Exploratory Data Analysis (EDA) was performed on the cleaned Titanic dataset using Python, Pandas, Matplotlib and Seaborn.

### Analysis Performed

- Dataset shape and data types
- Missing-value analysis
- Descriptive statistics
- Survival distribution
- Survival by gender
- Survival by passenger class
- Age distribution
- Fare distribution
- Correlation analysis

### Key Insights

1. Survival was not evenly distributed among passengers, showing that survival status is an important outcome to analyze.

2. Survival rates differed between male and female passengers, indicating that gender could be an important feature for a predictive model.

3. Passenger class showed differences in survival outcomes, suggesting that Pclass may be an important predictive feature.

4. Passenger ages were distributed across a wide range, so Age can provide useful information for understanding passenger groups and survival patterns.

5. Fare values showed variation between passengers, which may provide information related to passenger class and socioeconomic differences.

6. The correlation analysis helps identify relationships between numerical variables and can guide feature selection for future machine-learning models.

### Model/Decision Impact

The EDA suggests that variables such as Sex, Pclass, Age and Fare should be considered when developing a Titanic survival prediction model. The visualizations also help identify patterns and relationships before applying machine-learning algorithms.