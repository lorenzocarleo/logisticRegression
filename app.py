from flask import Flask, request, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load the model
model = joblib.load('logistic_regression_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from form
    try:
        year = int(request.form['year'])
        price = float(request.form['price'])
        beds = int(request.form['beds'])
        baths = int(request.form['baths'])
        sqft = int(request.form['sqft'])
    except ValueError:
        return "Please enter valid inputs."

    # Create a DataFrame for the model
    input_data = pd.DataFrame([[year, price, beds, baths, sqft]],
                              columns=['Year', 'Price', 'Beds', 'Baths', 'Sqft'])

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Add a descriptive message
    if prediction == 1:
        prediction_text = 'The model predicts that the price is likely to increase.'
    else:
        prediction_text = 'The model predicts that the price is not likely to increase.'

    return render_template('result.html', prediction_text=prediction_text)

    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True, port=5001)