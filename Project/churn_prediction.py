import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


file_path = r'Project/Bank Customer Churn Prediction.csv' 
data = pd.read_csv(file_path)

# მოგვიანებით დაგვჭირდება, როგორც ცალკე სვეტი
customer_ids = data['id']

# მოდელის ასაგებად არ გვჭირდება ისეთი ინფორმაცია, რომელსაც გავლენა არ აქვს მომხმარებლის ქცევაზე.
data = data.drop(columns=['id'])


# მოდელი ითვალისწინებს მხოლოდ რიცხობრივ ცვლადებს/მონაცემებს, ამიტომ საჭიროა ტექსტის სახით 
# გამოსახულ ცვლადებს მივანიჭოთ რიცხვითი მნიშვნელობები.
label_encoder_gender = LabelEncoder()
label_encoder_country = LabelEncoder()
data['gender'] = label_encoder_gender.fit_transform(data['gender'])  
data['country'] = label_encoder_country.fit_transform(data['country']) 



# X ცვლადში ვინახავთ დამოუკიდებელ ვცლადებს
X = data.drop(columns=['churn'])
# Y ცვლადში დამოკიდებული ცვლადის მნიშვნელობები ინახება, რომლის prediction-საც ვცდილობთ
y = data['churn']

# ვაკეთებთ სკალირებას, რადგან ცვლადების რიცხვითი მნიშვნელობა განსხვავებულ რეინჯებშია გაბნეული
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ვყოფთ ჩვენს მონაცემებს 2 ნაწილად. 1-ზე გადამზადდება ML მოდელი, ხოლო მეორეზე გააკეთებს predictions-ს.
X_train, X_test, y_train, y_test, customer_ids_train, customer_ids_test = train_test_split(
    X_scaled, y, customer_ids, test_size=0.2, random_state=42
)

# "LogisticRegression" ალგორითმი, რომლის დახმარებითავ ვაკეთებთ პროგნოზს.
logistic_model = LogisticRegression(random_state=42, max_iter=1000)
logistic_model.fit(X_train, y_train)

# მას შემდეგ რაც გადამზადდა მოდელი, ახლა ვცდილობთ დანარჩენ მომხმარებელზე გავაკეთოთ prediction
# წარსულ გამოცდილებაზე დაყრდნობით.
y_pred = logistic_model.predict(X_test)

# გამოგვაქ გარკვეული პარამეტრები, რათა შევაფასოთ მოდელის მუშაობა.
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

print("Model Accuracy:", accuracy)
print("\nConfusion Matrix:\n", conf_matrix)
print("\nClassification Report:\n", class_report)

# ალბათობა იმისა, რომ კონკრეტული მომხმარებელი გახდება churn.
churn_probabilities = logistic_model.predict_proba(X_test)[:, 1]  
predicted = logistic_model.predict(X_test) 

# ვქმნით ცხრილს, სადაც მოცემულია: მომხმარებელი, რა იწინასწარმეტყველა მოდელმა და რა ალბათობით.
customers_with_probabilities = pd.DataFrame({
    'Customer ID': customer_ids_test.reset_index(drop=True),
    'Predicted Class': predicted, 
    'Churn Probability': churn_probabilities  
})

# დავალაგოთ ალბათობათა კლების მიხედვით.
customers_with_probabilities = customers_with_probabilities.sort_values(by='Churn Probability', ascending=False)

# გამოვსახოთ პროცენტულად.
customers_with_probabilities['Churn Probability (%)'] = customers_with_probabilities['Churn Probability'].apply(lambda x: f'{x * 100:.2f}%')


customers_with_probabilities = customers_with_probabilities[['Customer ID', 'Predicted Class', 'Churn Probability (%)']]

print("\nTable of Customer IDs, Predicted Classes, and Churn Probabilities (Sorted by Descending Order):")
print()
print(customers_with_probabilities)

# პროგნოზი შევინახოთ CSV ფაილად.
customers_with_probabilities.to_csv('customers_with_churn_predictions.csv', index=False)




