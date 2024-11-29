import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report
import pickle

# Load dataset
df = pd.read_csv('data/emails.csv')  # Ensure your CSV has 'Email Text' and 'Email Type' columns

# Handle missing or invalid data
df['Email Text'] = df['Email Text'].fillna('')  # Replace NaN with an empty string
df['Email Type'] = df['Email Type'].fillna('')  # Ensure no missing labels

# Prepare features and labels
X = df['Email Text']
y = df['Email Type'].map({'Safe Email': 0, 'Phishing Email': 1})  # Convert labels to binary

# Text preprocessing and vectorization
vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X_vectorized = vectorizer.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.3, random_state=42)

# Model training
model = GradientBoostingClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Save the model and vectorizer
with open('backend/model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

with open('backend/vectorizer.pkl', 'wb') as vectorizer_file:
    pickle.dump(vectorizer, vectorizer_file)

print("Model and vectorizer saved!")
