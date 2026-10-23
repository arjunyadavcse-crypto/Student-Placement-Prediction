<<<<<<< HEAD
# 🎓 Student Placement Prediction Portal (SPP)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Django](https://img.shields.io/badge/Django-6.1-green?logo=django)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?logo=scikit-learn)
![License](https://img.shields.io/badge/License-MIT-purple)

An end-to-end Machine Learning-powered web portal designed for Training & Placement (T&P) cells and students. It evaluates candidate readiness, predicts campus placement outcomes using a trained **Support Vector Classifier (SVC)**, and delivers personalized skill-gap advisory along with printable evaluation reports.

---

## 📌 Project Overview

Campus placements are a critical milestone in higher technical education. This portal bridges the gap between academic self-assessment and industry expectations by analyzing historical campus placement trends across three core criteria:
1. **Academic Performance (CGPA)** (0.00 – 10.00)
2. **Cognitive & Aptitude Assessment (IQ Score)** (60 – 140)
3. **Technical Competency & Profile Score** (0 – 100)

Unlike basic toy projects, this application provides **placement confidence probabilities**, **qualitative status ratings**, and **actionable placement cell recommendations** tailored to individual weak areas.

---

## ✨ Key Features

- **🔐 Student Authentication System:** Secure registration and login flow with session persistence across the evaluation lifecycle.
- **🎯 Intelligent Placement Classifier:** Powered by an SVM model (`SVC`) combined with `StandardScaler` for robust multi-factor classification.
- **📊 Quantitative Probability Gauge:** Converts decision margin metrics into intuitive placement likelihood percentages (e.g., `84.5%`).
- **📋 Training & Placement Cell Advisory:** Dynamic, rule-assisted recommendations addressing low CGPA, aptitude gaps, or profile shortcomings.
- **🖨️ Printable Official Assessment Report:** Dedicated CSS print-mode allowing instant PDF generation or physical report printing.
- **💎 Modern Responsive UI:** Polished dark-mode glassmorphic interface built with vanilla CSS.

---

## 🛠️ Technology Stack

| Component | Technology |
|---|---|
| **Backend Framework** | Django (Python) |
| **Machine Learning** | Scikit-Learn (`SVC`, `StandardScaler`) |
| **Model Serialization** | Joblib |
| **Database** | SQLite3 (Django ORM) |
| **Frontend** | HTML5, Vanilla CSS3 (Glassmorphism & Flex/Grid) |
| **Data Processing** | NumPy, Python Standard Library |

---

## 🧠 Machine Learning Pipeline

- **Dataset:** 300+ engineering student records capturing `cgpa`, `iq`, `profile_score`, and recruitment status (`placed`).
- **Feature Scaling:** `StandardScaler` normalizes inputs to zero mean and unit variance.
- **Model:** Support Vector Classifier (`SVC`) optimized for non-linear decision boundaries.
- **Probability Derivation:** Evaluates the hyperplane distance via `decision_function` mapped through a logistic sigmoid function:
  $$\text{Probability} = \frac{1}{1 + e^{-\text{decision\_value}}}$$

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/student-placement-prediction.git
cd student-placement-prediction
```

### 2. Set Up Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Required Dependencies
```bash
pip install django scikit-learn joblib numpy
```

### 4. Apply Database Migrations
```bash
python manage.py migrate
```

### 5. Run the Development Server
```bash
python manage.py runserver
```

Open your browser and visit: `http://127.0.0.1:8000/`

---

## 📂 Project Directory Structure

```text
spp/
│
├── manage.py                     # Django management script
├── db.sqlite3                    # Local SQLite database
├── students_placement.csv        # Placement training dataset
├── sp_Model.pkl                  # Trained Support Vector Classifier model
├── sp_scaler_Model.pkl           # Trained StandardScaler object
│
├── spp/                          # Django Project Core
│   ├── __init__.py
│   ├── settings.py               # Django configuration & installed apps
│   ├── urls.py                   # Global URL routing
│   ├── wsgi.py
│   └── asgi.py
│
└── students/                     # Students Application
    ├── models.py                 # Student registration & credentials model
    ├── views.py                  # Auth, ML prediction & advisory views
    ├── apps.py
    └── templates/                # Frontend UI Templates
        ├── home.html             # Landing page & quick navigation
        ├── login.html            # Student login card
        ├── signup.html           # Candidate registration card
        ├── input.html            # Placement assessment input form
        └── result.html           # Placement evaluation report card
```

---

## 📈 Standard Assessment Benchmarks

| Metric | Campus Benchmark | Industry Relevance |
|---|---|---|
| **CGPA** | $\ge 7.0$ | Primary eligibility screening for MNCs & Product firms |
| **Aptitude (IQ)** | $\ge 100$ | Written assessment / cognitive round clearance |
| **Technical Profile** | $\ge 60$ | Hands-on project portfolio & technical interview readiness |

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to check the [issues page](https://github.com/your-username/student-placement-prediction/issues).

---

## 📄 License

This project is open-source and licensed under the [MIT License](LICENSE).
=======
# Student-Placement-Prediction
 An end-to-end Machine Learning web application built with Django and Scikit-Learn to predict campus placement likelihood and provide strategic skill-gap advisory based on CGPA, aptitude test scores, and technical profile ratings.
>>>>>>> 3c8607d15a4bb50903a2db77b33c63105e299ce9
