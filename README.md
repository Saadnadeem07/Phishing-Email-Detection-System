# 🛡️ Phishing Email Detection System

An intelligent, machine-learning powered system that analyzes email content and classifies it as **Phishing** or **Safe** in real time — helping users spot malicious emails before they cause harm.

<p align="left">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white">
  <img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white">
  <img alt="scikit-learn" src="https://img.shields.io/badge/scikit--learn-F7931E?logo=scikitlearn&logoColor=white">
  <img alt="License" src="https://img.shields.io/badge/License-MIT-green">
</p>

---

## 📖 Overview

Phishing remains one of the most common attack vectors in cyber security. This project tackles it with a lightweight ML model trained on a large corpus of labelled emails. The model is served through a **FastAPI** backend and consumed by a clean, responsive **web interface** that returns an instant verdict along with a confidence score.

| | |
|---|---|
| **Model** | TF-IDF features + Gradient Boosting Classifier |
| **Backend** | FastAPI + Uvicorn |
| **Frontend** | HTML, Tailwind CSS, vanilla JavaScript |
| **Dataset** | ~175k labelled emails (`Safe` / `Phishing`) |

---

## ✨ Features

- 🔍 **Accurate detection** — classifies emails using a trained Gradient Boosting model.
- ⚡ **Real-time feedback** — instant prediction with a confidence percentage.
- 🎨 **Clean UI** — responsive, animated interface that reacts to the result.
- 🔌 **Simple REST API** — a single `POST /predict` endpoint, easy to integrate.

---

## 📁 Project Structure

```
phishing-email-detection/
├── backend/                # FastAPI service that serves predictions
│   ├── app.py              # API app + /predict endpoint
│   ├── model.pkl           # Trained classifier
│   └── vectorizer.pkl      # Fitted TF-IDF vectorizer
├── frontend/
│   └── index.html          # Web interface
├── model/
│   └── train_model.py      # Training pipeline (regenerates the .pkl files)
├── data/
│   └── emails.csv          # Labelled training dataset
├── docs/
│   └── IS-ProjectProposal.pdf
├── requirements.txt
├── LICENSE
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone & install dependencies

```bash
git clone https://github.com/Saadnadeem07/Phishing-Email-Detection-System.git
cd Phishing-Email-Detection-System

python -m venv .venv
source .venv/bin/activate        # On Windows: .venv\Scripts\activate

pip install -r requirements.txt
```

### 2. Run the backend

```bash
cd backend
uvicorn app:app --reload
```

The API is now available at **http://127.0.0.1:8000**.
Interactive docs (Swagger UI) are at **http://127.0.0.1:8000/docs**.

### 3. Open the frontend

Open `frontend/index.html` in your browser, paste an email, and click **Check Email**.

> The frontend talks to the backend at `http://127.0.0.1:8000`, so make sure the API is running first.

---

## 🧠 Retraining the Model (optional)

The repository already ships with a trained model. To retrain it on the dataset:

```bash
python model/train_model.py
```

This regenerates `backend/model.pkl` and `backend/vectorizer.pkl` and prints the accuracy and classification report.

---

## 🔌 API Reference

### `POST /predict`

**Request body**

```json
{ "email": "Your account has been suspended. Click here to verify..." }
```

**Response**

```json
{ "prediction": "Phishing Email", "confidence": 0.97 }
```

### `GET /`

Health check — returns the API status.

---

## 🖼️ Output

![Application screenshot](https://github.com/user-attachments/assets/e7c605f8-3b64-46bf-93c9-44ce6d1233bd)

---

## 🎯 Scope

- Focuses on the **textual content** of emails (body and subject line).
- Does **not** analyze attachments, images, or embedded links.

---

## 👥 Authors

- **Saad Nadeem**
- **Saad Habib**
- **Abdul Basit**
- **Talha Rauf**
- **Sultan-Ul-Arfeen**

**Supervisor:** Dr. M. Umer Aftab

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
