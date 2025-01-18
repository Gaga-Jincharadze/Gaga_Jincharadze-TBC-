import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset directly in chart.py
file_path = r'Project/Bank Customer Churn Prediction.csv'
data = pd.read_csv(file_path)

numeric_df = data.select_dtypes(include=['number'])

# Calculate the correlation matrix
correlation_matrix = numeric_df.corr()
plt.figure(figsize=(20, 12))
# Create a heatmap using seaborn
sns.heatmap(correlation_matrix, annot=True, fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()

sns.scatterplot(x='products_number', y='balance', data=data)
plt.title("Relationship Between Number of Products and Balance")
plt.xlabel("Number of Products")
plt.ylabel("Balance")
sns.lmplot(x='products_number', y='balance', hue='churn', data=data, palette='Set1', scatter_kws={'alpha':0.6})
plt.show()

