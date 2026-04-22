import pickle

model = pickle.load(open("models/model.pkl", "rb"))
vectorizer = pickle.load(open("models/vectorizer.pkl", "rb"))

def predict_intent(text):
    X = vectorizer.transform([text])
    probs = model.predict_proba(X)[0]

    confidence = max(probs)
    intent = model.classes_[probs.argmax()]

    return intent, confidence