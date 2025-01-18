import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset directly in chart.py
file_path = r'Project/Bank Customer Churn Prediction.csv'
data = pd.read_csv(file_path)

# Plot: Customer Churn by Gender
plt.figure(figsize=(10, 5))
sns.countplot(x='gender', hue='churn', data=data, palette='pastel')
plt.title('Customer Churn by Gender')
plt.xlabel('Gender')
plt.ylabel('Number of Customers')
plt.legend(title='Churn', labels=['Not Churned', 'Churned'])
plt.show()

