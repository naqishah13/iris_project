import os
from pymongo.errors import InvalidURI, ConnectionFailure, OperationFailure
from pymongo.server_api import ServerApi
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus

mongo_uri = "mongodb+srv://naqishah:lV0Age4INtyhLVQ9@cluster0.7jsdwbv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Connect to MongoDB Atlas and insert data
try:
    client = MongoClient(mongo_uri, server_api=ServerApi('1'))
    db = client['iris_database']  # Replace with your actual database name
    collection = db['iris_data_predictions']  # Replace with your actual collection name
    
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
    print("Connected to MongoDB successfully.")
    
    print("Model accuracy: {}".format(accuracy))
    print("Results: {}".format(result))
    
except InvalidURI as e:
    print(f"Invalid URI: {e}")
except ConnectionFailure as e:
    print(f"Could not connect to MongoDB: {e}")
except OperationFailure as e:
    print(f"Authentication failed or failed to insert data: {e}")
    print("Check your username and password.")
    
# INSERT DOCUMENTS
#
# You can insert individual documents using collection.insert_one().
# In this example, we're going to create four documents and then 
# insert them all with insert_many().

# recipe_documents = [{ "name": "elotes", "ingredients": ["corn", "mayonnaise", "cotija cheese", "sour cream", "lime"], "prep_time": 35 },
#                     { "name": "loco moco", "ingredients": ["ground beef", "butter", "onion", "egg", "bread bun", "mushrooms"], "prep_time": 54 },
#                     { "name": "patatas bravas", "ingredients": ["potato", "tomato", "olive oil", "onion", "garlic", "paprika"], "prep_time": 80 },
#                     { "name": "fried rice", "ingredients": ["rice", "soy sauce", "egg", "onion", "pea", "carrot", "sesame oil"], "prep_time": 40 }]

# try: 
#     result = collection.insert_many(recipe_documents)

# # return a friendly error if the operation fails
# except OperationFailure:
#     print("An authentication error was received. Are you sure your database user is authorized to perform write operations?")
#     sys.exit(1)
# else:
#     inserted_count = len(result.inserted_ids)
#     print("I inserted %x documents." %(inserted_count))

#     print("\n")
    




