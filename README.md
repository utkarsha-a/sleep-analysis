#  Sleep Analysis ML for Fitness App

This project implements an end-to-end machine learning pipeline for analyzing sleep data collected from smartwatches and integrating the insights into a fitness mobile application.

## 🔍 Features
- Nightly sleep quality classification using Random Forest & XGBoost
- Explainable AI with feature importance
- Weekly sleep pattern detection
- API-ready backend using FastAPI
- Designed for React Native app integration

## 🧠 ML Pipeline
Smartwatch Data → Feature Engineering → ML Model → Explainability → Weekly Analysis → Mobile App

## 🛠 Tech Stack
- Python
- Scikit-learn
- XGBoost
- FastAPI
- Pandas, NumPy

## 🚀 How to Run
```bash
python train_sleep_model.py
uvicorn main:app --reload
