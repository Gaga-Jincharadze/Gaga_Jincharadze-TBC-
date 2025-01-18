import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset directly in chart.py
file_path = r'Project/Bank Customer Churn Prediction.csv'
df = pd.read_csv(file_path)



# Plotting the age distribution
plt.figure(figsize=(10, 5))
sns.histplot(df['age'], bins=25, kde=True, color='skyblue')
plt.title('Age Distribution', fontsize=14)
plt.xlabel('Age', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.show()