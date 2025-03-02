# AI-Based Network Intrusion Detection System (NIDS)

## Overview
This project is an AI-powered **Network Intrusion Detection System (NIDS)** that leverages **six different machine learning models** to analyze and classify network traffic using the **NSL-KDD dataset**. Users can upload network traffic data (CSV format) to the web application and choose a model to test and classify the data. 

The application is built with **Node.js (Express.js)** for the backend, **MongoDB** for data storage, and **Google Authentication** for user login. The machine learning models are implemented in **Python** and executed in the background via **PythonShell** in Node.js.

## Features
- **User Authentication**: Supports local and Google authentication.
- **Multiple ML Models**: Users can test their data with KNN, SVM, Random Forest, Logistic Regression, Naive Bayes, and XGBoost.
- **CSV Upload & Processing**: Users upload network traffic data, and predictions are returned as a downloadable CSV.
- **Scalable Backend**: Built with Express.js and MongoDB.
- **Prediction Execution in Python**: The backend interacts with a Python script to process uploaded CSV files and return predictions.
- **SMOTE for Data Balancing**: The models were trained using **Synthetic Minority Over-sampling Technique (SMOTE)** to ensure the model isn't biased toward majority attack types.

## Tech Stack
- **Backend**: Node.js 
- **Frontend**: EJS (Embedded JavaScript Templates)
- **Database**: MongoDB
- **Machine Learning**: Scikit-learn, XGBoost (Python)
- **Authentication**: Passport.js (Local & Google OAuth)

## Setup Instructions

### Prerequisites
Ensure you have the following installed:
- **Node.js** (v16+ recommended)
- **Python 3.x** (with `joblib`, `pandas`, `scikit-learn`, `xgboost` installed)
- **MongoDB**

### Installation Steps

#### 1. Clone the repository
```bash
git clone https://github.com/genomecrafter/sandbox25.git
cd sandbox25
```

#### 2. Install dependencies
```bash
npm install
```

#### 3. Configure Environment Variables
Edit the `.env` file in the root directory and fill in the required values:
```
DB_LINK=your_mongodb_connection_string
SESSION_SECRET=your_secret_key
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
GOOGLE_CALLBACK_URL=http://localhost:5000/auth/google/callback
```

#### 4. Start MongoDB
Ensure MongoDB is running before starting the server:

#### 5. Run the Application
```bash
node app.js
```

The application should now be running on `http://localhost:port number`.

## Usage
### 1. Register & Login
- Visit the sign-up page to create an account.
- Login using local credentials or Google Authentication.

### 2. Upload CSV File
- Navigate to the **Predict** section.
- Upload a CSV file containing network traffic data.
- Select one of the six available models for prediction.

### 3. Get Prediction Results
- The application will process the file and provide a **downloadable CSV** with predicted attack classifications.

## Machine Learning Models
The backend supports the following models:
- **K-Nearest Neighbors (KNN)**
- **Support Vector Machine (SVM)**
- **Random Forest (RF)**
- **Logistic Regression (LR)**
- **Naive Bayes (NB)**
- **XGBoost (XGB)**

The models were trained using **SMOTE (Synthetic Minority Over-sampling Technique)** to ensure balanced learning and avoid bias toward the majority attack types.

The Python script (`nids_updated_csv.py`) loads the respective model, preprocesses the data, and generates predictions based on the uploaded CSV file.

## API Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Homepage |
| `/login` | GET/POST | User login |
| `/register` | GET/POST | User registration |
| `/uploadjavatpoint` | POST | Upload CSV & process with ML model |
| `/download-file` | GET | Download predicted CSV |
| `/logout` | GET | Logout user |

## Working
Login Page
![login](https://github.com/user-attachments/assets/b6e2c825-0d8e-4444-9968-cd82056644ef)

The home page
![ui1](https://github.com/user-attachments/assets/2c01cdd9-51b7-4770-9477-9be0b55942be)

Predict page
![ui2](https://github.com/user-attachments/assets/41f8a407-a667-488c-a43d-d8cb14d7fcfe)

Test data before uploading
![before](https://github.com/user-attachments/assets/5aed367c-a5e5-4c39-abfd-48139bba9951)

Data file downloaded from website
![after](https://github.com/user-attachments/assets/2c5e8e47-5ad5-4119-9e96-8232f8131bee)


## Future Enhancements
- Add **real-time traffic monitoring**.
- Improve **model accuracy with deep learning**.
- Implement **automatic feature selection** for better predictions.
- Deploy as a **cloud-based service** for scalability.

### Developed for SandBox25 🚀

