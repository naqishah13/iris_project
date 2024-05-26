import os
from pymongo import MongoClient
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Connect to MongoDB Atlas
mongo_uri = os.getenv("MONGODB_URI")
client = MongoClient(mongo_uri)
db = client.your_database_name
collection = db.your_collection_name

# Load Dataset
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

# Train a Model
clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train, y_train)

# Make Predictions
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# Insert Accuracy to MongoDB
result = {"model": "RandomForest", "accuracy": accuracy}
collection.insert_one(result)

print(f"Model accuracy: {accuracy}")
print(f"Results: {result}")