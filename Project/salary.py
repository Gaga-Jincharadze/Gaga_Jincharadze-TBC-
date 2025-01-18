import pandas as pd

# Load the dataset
file_path = r'Project/Bank Customer Churn Prediction.csv'
data = pd.read_csv(file_path)

# Rename gender values for better readability if needed
data['gender'] = data['gender'].replace({0: 'Female', 1: 'Male'})  # Update if gender is encoded numerically

# Group the data by gender
salary_stats_by_gender = data.groupby('gender')['salary'].agg(
    Mean='mean',
    Min='min',
    Max='max',
    Median='median',
    Mode=lambda x: x.mode()[0],  # Extract the first mode
    StdDev='std'
).reset_index()

# Format the salary statistics for readability
salary_stats_by_gender['Mean'] = salary_stats_by_gender['Mean'].apply(lambda x: f"{x:,.0f}")
salary_stats_by_gender['Min'] = salary_stats_by_gender['Min'].apply(lambda x: f"{x:,.0f}")
salary_stats_by_gender['Max'] = salary_stats_by_gender['Max'].apply(lambda x: f"{x:,.0f}")
salary_stats_by_gender['Median'] = salary_stats_by_gender['Median'].apply(lambda x: f"{x:,.0f}")
salary_stats_by_gender['Mode'] = salary_stats_by_gender['Mode'].apply(lambda x: f"{x:,.0f}")
salary_stats_by_gender['StdDev'] = salary_stats_by_gender['StdDev'].apply(lambda x: f"{x:,.0f}")

# Print the results
print("\nSalary Statistics by Gender:")
print(salary_stats_by_gender)


