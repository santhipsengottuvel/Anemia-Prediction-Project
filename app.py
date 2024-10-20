from flask import Flask, render_template, request
import sys
import numpy as np
import pandas as pd
from src.exception import CustomException
from sklearn.preprocessing import StandardScaler
from src.Pipelines.Predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'POST':
        # Debug: Print the form data
        print(request.form)  # This will print the form data to the console

        gender = request.form.get("gender")  # Changed to lowercase 'gender'
        print("Gender:", gender)  # Debug: Print Gender to check what the server is receiving

        # Capture the other form fields
        hemoglobin = request.form.get("hemoglobin")  # Changed to lowercase 'hemoglobin'
        print("Hemoglobin:", hemoglobin)

        # Similarly for MCH, MCHC, and MCV
        mch = request.form.get("MCH")
        mchc = request.form.get("MCHC")
        mcv = request.form.get("MCV")
        
        print("MCH:", mch)
        print("MCHC:", mchc)
        print("MCV:", mcv)

        # Validation and error handling
        if gender is None or gender == "":
            return "Gender is missing"

        try:
            data = CustomData(
                Gender=int(gender),
                Hemoglobin=float(hemoglobin),
                MCH=float(mch),
                MCHC=float(mchc),
                MCV=float(mcv)
            )
        except ValueError as ve:
            return f"Invalid input: {ve}"

        # Convert the data into DataFrame format
        pred_df = data.get_data_as_data_frame()
        print(pred_df)

        # Initialize the PredictPipeline and make a prediction
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)

        # Interpret the result
        prediction = "Anemic" if results[0] == 1 else "Not Anemic"
        
        return render_template('home.html', results=prediction)

    return render_template("home.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    