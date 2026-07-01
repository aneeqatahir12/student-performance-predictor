# 🎓 Student Performance Predictor

A Machine Learning web application that predicts student exam performance based on study habits and academic history.

## 🌐 Live Demo

Frontend

https://student-performance-cy8e.bolt.host

Backend API

https://student-performance-predictor-a899.onrender.com

---

# 📌 Project Overview

This project uses a trained Machine Learning model to estimate a student's expected performance using four input features.

The application consists of:

- Machine Learning Model
- Flask REST API
- React Frontend (Bolt.new)
- Render Deployment

---

#  Features

- Predict student performance instantly
- REST API built with Flask
- Machine Learning model using Scikit-learn
- Modern React frontend
- Responsive UI
- Cloud deployment using Render
- API integration between frontend and backend

---

#  Input Features

The model predicts performance using:

-  Hours Studied
-  Previous Scores
-  Sleep Hours
-  Sample Question Papers Practiced

---

#  How It Works

1. User enters student information.
2. React frontend sends a POST request.
3. Flask API receives the data.
4. Machine Learning model predicts the score.
5. Prediction is returned as JSON.
6. Frontend displays the result.

---

# 🛠 Tech Stack

## Machine Learning

- Python
- Scikit-learn
- NumPy
- Joblib

## Backend

- Flask
- Flask-CORS

## Frontend

- React
- TypeScript
- Tailwind CSS
- Bolt.new

## Deployment

- Render
- GitHub

---

# 📂 Project Structure

```
student-performance-predictor
│
├── app.py
├── requirements.txt
├── student_performance_model.pkl
└── README.md
```

---

#  API Endpoint

## POST /predict

Example Request

```json
{
  "Hours Studied": 6,
  "Previous Scores": 75,
  "Sleep Hours": 7,
  "Sample Question Papers Practiced": 8
}
```

Example Response

```json
{
  "success": true,
  "prediction": 64.64
}
```

---

# 💻 Local Installation

Clone the repository

```bash
git clone https://github.com/aneeqatahir12/student-performance-predictor.git
```

Move into the project

```bash
cd student-performance-predictor
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the server

```bash
python app.py
```

Server runs at

```
http://127.0.0.1:5000
```

---

# 🌍 Live Demo

Frontend

https://student-performance-cy8e.bolt.host

Backend

https://student-performance-predictor-a899.onrender.com

---

#  Future Improvements

- Authentication
- Prediction History
- Database Integration
- Charts & Analytics
- Docker Support
- CI/CD Pipeline

---

# 👩‍💻 Author

**Aneeqa Tahir**

AI & Machine Learning Learner

GitHub

https://github.com/aneeqatahir12

LinkedIn

(Add your LinkedIn profile here)

---

⭐ If you found this project useful, consider giving it a star.
