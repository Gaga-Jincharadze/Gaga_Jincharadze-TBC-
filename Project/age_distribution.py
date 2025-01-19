import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


file_path = r'Project/Bank Customer Churn Prediction.csv'
data = pd.read_csv(file_path)


# ვაგებთ ასაკის სიხშირის რუკას და მის გადანაწილებას
# განვსაზღვრავთ ფანჯრის ზომას
plt.figure(figsize=(10, 5)) 
#ვაგებთ ჰისტოგრამას და ვუწერთ პარამეტრებს.
sns.histplot(data['age'], bins=25, kde=True, color='blue')
plt.title('Age Distribution', fontsize=14)
plt.xlabel('Age', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.show()