import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


file_path = r'Project/Bank Customer Churn Prediction.csv'
data = pd.read_csv(file_path)

# data-დან ვტოვებთ მხოლო რიცხვითი მნიშვნელობის მქონე სვეტებს/ცვლადებს.
numeric_data = data.select_dtypes(include=['number'])

# ვნახულობთ როგორი კავშირია ცვლადებს შორის.
correlation_matrix = numeric_data.corr()
plt.figure(figsize=(8, 10))
# ვქმინთ კორელაციის მატრიცას, heatmap-ის გამოყენებით. გამოგვაქ რიცხვითი მნიშვნელობები "annot" 
sns.heatmap(correlation_matrix, annot=True, fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()

