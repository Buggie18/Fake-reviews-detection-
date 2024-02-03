from flask import Flask, render_template, request
import numpy as np
import pickle

# Load the model
model = pickle.load(open("model.pkl", "rb"))

flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return render_template("index.html")

@flask_app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get the input text from the form
        review_text = [str(x) for x in request.form.values()]
        
        # Vectorize the input text using the same TF-IDF vectorizer
        review_tfidf = tfidf_vectorizer.transform(review_text)
        
        # Make the prediction
        prediction = int(model.predict(review_tfidf)[0])
        
        # Display the prediction on the HTML page
        return render_template("index.html", prediction_text="The review is {}".format("Fake" if prediction == 1 else "Real"))
    
    except Exception as e:
        return render_template("index.html", prediction_text="Error: {}".format(e))

if __name__ == "__main__":
    flask_app.run(debug=True)
