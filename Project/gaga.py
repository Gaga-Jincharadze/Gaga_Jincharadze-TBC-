import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load the dataset
file_path = r'Project/Bank Customer Churn Prediction.csv'  # Corrected file path
data = pd.read_csv(file_path)

# Extract customer IDs for later use
customer_ids = data['customer_id']

# Drop the unnecessary column
data = data.drop(columns=['customer_id'])

# Encode categorical variables
label_encoder_gender = LabelEncoder()
label_encoder_country = LabelEncoder()

data['gender'] = label_encoder_gender.fit_transform(data['gender'])  # Encode 'gender'
data['country'] = label_encoder_country.fit_transform(data['country'])  # Encode 'country'

# Split features and target variable
X = data.drop(columns=['churn'])
y = data['churn']

# Normalize numerical variables using StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test, customer_ids_train, customer_ids_test = train_test_split(
    X_scaled, y, customer_ids, test_size=0.2, random_state=42
)

# Train the logistic regression model
logistic_model = LogisticRegression(random_state=42, max_iter=1000)
logistic_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = logistic_model.predict(X_test)

# Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

# Display the results
print("Model Accuracy:", accuracy)
print("\nConfusion Matrix:\n", conf_matrix)
print("\nClassification Report:\n", class_report)

# Predict churn probabilities
churn_probabilities = logistic_model.predict_proba(X_test)[:, 1]  # Probabilities for 'churn = 1'
predicted_classes = logistic_model.predict(X_test)  # Binary predictions (0 or 1)

# Create a table with Customer IDs, Predicted Class, and Churn Probabilities
customers_with_probabilities = pd.DataFrame({
    'Customer ID': customer_ids_test.reset_index(drop=True),
    'Predicted Class': predicted_classes,  # Add predicted classes (0 or 1)
    'Churn Probability': churn_probabilities  # Keep raw probabilities for sorting
})

# Sort by raw churn probabilities in descending order
customers_with_probabilities = customers_with_probabilities.sort_values(by='Churn Probability', ascending=False)

# Format the probabilities as percentages for display
customers_with_probabilities['Churn Probability (%)'] = customers_with_probabilities['Churn Probability'].apply(lambda x: f'{x * 100:.2f}%')

# Drop the raw probabilities if you don't need them in the final output
customers_with_probabilities = customers_with_probabilities[['Customer ID', 'Predicted Class', 'Churn Probability (%)']]

# Display the sorted table
print("\nTable of Customer IDs, Predicted Classes, and Churn Probabilities (Sorted by Descending Order):")
print(customers_with_probabilities)

# Save the table to a CSV file
customers_with_probabilities.to_csv('customers_with_churn_predictions.csv', index=False)
print("\nTable has been saved to 'customers_with_churn_predictions.csv'.")



