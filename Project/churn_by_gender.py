import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r'Project/Bank Customer Churn Prediction.csv'
data = pd.read_csv(file_path)


plt.figure(figsize=(10, 5))
# ვქმნით bar chart-ს X ღერძის მნიშვნელობათა რაოდენობის გათვალისწინებით, ვშლით churn status-ის მიხედვით.
sns.countplot(x='gender', hue='churn', data=data)
plt.title('Customer Churn by Gender')
plt.xlabel('Gender')
plt.ylabel('Number of Customers')
plt.legend(title='Churn', labels=['Not Churned', 'Churned'])
plt.show()

