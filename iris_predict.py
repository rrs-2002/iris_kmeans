from sklearn. datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pickle

# Train and save the model
def train_model():
	data = load_iris()
	X, y = data.data, data.target
	model = RandomForestClassifier()
	model.fit(X, y)
	with open('model.pkl', 'wb') as f:
		pickle.dump(model, f)
	print("Model trained and saved as model.pkl")

# Load model and make a predickion
def predict():
	with open('model.pkl', 'rb') as f:
		model = pickle.load(f)
	test_data = [6.2, 3.5, 1.4, 0.2]
	prediction = model.predict([test_data])
	print(f"Prediction for {test_data}: {int(prediction[0])}")

if __name__ == '__main__':
	train_model()
	predict()
