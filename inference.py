import joblib
from sklearn.datasets import load_iris

# Load the model
model = joblib.load("model.joblib")

# Load the iris dataset
iris = load_iris()
X = iris.data

# Perform classification
predictions = model.predict(X)

# Print out the result string
result_string = f"Predictions: {predictions}"
print(result_string)
