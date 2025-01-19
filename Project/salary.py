import pandas as pd

# Load the dataset
file_path = r'Project/Bank Customer Churn Prediction.csv'
data = pd.read_csv(file_path)

# სქესის მიხედვით ვითვლით ხელფასების: საშუალოს, მინიმუმს, მაქსიმუმს, მედიანას და სტანდარტულ გადახრას
salary_stats_by_gender = data.groupby('gender')['salary'].agg(
    Mean='mean',
    Min='min',
    Max='max',
    Median='median',
    StdDev='std'
).reset_index()

# ყველა სვეტს ვაფორმატებ წაკითხვადობისთვის
for col in ['Mean', 'Min', 'Max', 'Median',  'StdDev']:
    salary_stats_by_gender[col] = salary_stats_by_gender[col].apply(lambda x: f"{x:,.0f}")

print("\nSalary Statistics by Gender:")
print(salary_stats_by_gender)



