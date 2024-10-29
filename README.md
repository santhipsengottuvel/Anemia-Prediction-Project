Anemia Prediction Project

This project aims to predict anemia based on various blood parameters such as Hemoglobin, MCH (Mean Corpuscular Hemoglobin), MCHC (Mean Corpuscular Hemoglobin Concentration), MCV (Mean Corpuscular Volume), and gender using a machine learning model. The project has been containerized using Docker and deployed on Render.


Project Overview
Anemia is a condition where the blood lacks enough healthy red blood cells or hemoglobin. This project helps in predicting the likelihood of anemia using important blood test parameters. The user provides inputs through a web interface, and the machine learning model predicts whether the person is anemic.


Features

Web Interface: A user-friendly web interface built using Flask, where users can input their blood test parameters.

Machine Learning Model: The project uses a trained machine learning model to predict anemia based on input parameters.

Deployment: The entire application has been containerized using Docker and deployed on Render for public use.


Key Components

Hemoglobin (Hb): The protein in red blood cells responsible for carrying oxygen.

MCH (Mean Corpuscular Hemoglobin): Average mass of hemoglobin per red blood cell in a sample of blood.

MCHC (Mean Corpuscular Hemoglobin Concentration): Average concentration of hemoglobin in red blood cells.

MCV (Mean Corpuscular Volume): A measure of the average volume of a red blood cell.


Tech Stack
Python 3.11
Flask for web development
scikit-learn for machine learning
Docker for containerization
Render for deployment
pandas, numpy for data manipulation and processing


Project Structure
bash
Copy code
├── app.py                      # Flask app for handling web requests
├── src/
│   ├── Pipelines/
│   │   ├── Predict_pipeline.py  # Pipeline for preprocessing and prediction
│   ├── exception.py             # Custom exception handling
│   ├── utils.py                 # Utility functions for saving/loading models
├── templates/
│   ├── index.html               # Main homepage for input
│   ├── home.html                # Result page after prediction
├── Dockerfile                   # Docker configuration
├── requirements.txt             # Python dependencies
├── artifacts/
│   ├── model.pkl                # Trained model
│   ├── preprocessor.pkl         # Preprocessing object (scaler)
├── README.md                    # Project documentation


Installation and Usage

1. Clone the repository
bash
Copy code
git clone https://github.com/santhipsengottuvel/Anemia-Prediction-Project.git
cd Anemia-Prediction-Project

2. Create and activate a virtual environment (optional but recommended)
bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies
bash
Copy code
pip install -r requirements.txt

4. Run the Flask application
bash
Copy code
python app.py
Navigate to http://127.0.0.1:5000/ in your browser to use the application.

5. Docker Setup
To run the project in a Docker container:

bash
Copy code
docker build -t anemia_proj .
docker run -p 5000:5000 anemia_proj

6. Deployment on Render
The project is deployed on Render. You can access it live using the following link:

Anemia Prediction Web App
anemia-proj-latest.onrender.com