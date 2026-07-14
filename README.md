# 🩺 Breast Cancer Prediction using Logistic Regression

A Machine Learning web application that predicts whether a breast tumor is **Benign** or **Malignant** using the **Logistic Regression** algorithm. The model is trained on the **Wisconsin Breast Cancer Diagnostic Dataset** and deployed with **Streamlit** for an interactive user interface.

---

## 📂 Project Structure

```
Breast-cancer_prediction/
│
├── data/
│   └── breast_cancer.csv
│
├── model/
│   └── model.pkl
│
├── app.py
├── breast_cancer.ipynb
├── requirements.txt
└── README.md
```

---

# 🚀 Getting Started

## 1. Clone the Repository

```bash
git clone <repository-url>
cd Breast-cancer_prediction
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate the virtual environment:

```bash
.venv\Scripts\activate
```

---

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run the Project

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

# 🧠 About the Project

This project predicts whether a breast tumor is **Benign (Non-Cancerous)** or **Malignant (Cancerous)** using a Logistic Regression machine learning model.

The model is trained on the **Wisconsin Breast Cancer Diagnostic Dataset**, which contains diagnostic measurements extracted from digitized images of breast tissue samples.

Users can enter the required medical features through the Streamlit interface, and the trained model instantly predicts the diagnosis.

---

# 📊 Dataset

**Dataset Name**

Wisconsin Breast Cancer Diagnostic Dataset

### Features

The dataset contains **30 numerical features**, including:

- Radius
- Texture
- Perimeter
- Area
- Smoothness
- Compactness
- Concavity
- Concave Points
- Symmetry
- Fractal Dimension

and their corresponding mean, standard error, and worst values.

### Target Classes

- **Benign (B)** → Non-Cancerous
- **Malignant (M)** → Cancerous

---

# 🤖 Machine Learning Model

Algorithm Used:

- Logistic Regression

Why Logistic Regression?

- Fast and efficient
- Performs well for binary classification
- Easy to interpret
- High accuracy on the Wisconsin dataset

---

# ⚙️ Project Workflow

```text
                Wisconsin Breast Cancer Dataset
                            │
                            ▼
                    Data Preprocessing
          (Cleaning, Feature Selection, Scaling)
                            │
                            ▼
                     Train-Test Split
                            │
                            ▼
               Logistic Regression Model
                            │
                            ▼
                    Model Training
                            │
                            ▼
                    Model Evaluation
                            │
                            ▼
                    Save Model (.pkl)
                            │
                            ▼
                  Streamlit Web Application
                            │
                            ▼
                User Enters Medical Features
                            │
                            ▼
                   Breast Cancer Prediction
                            │
                            ▼
        Benign ✅          or          Malignant ⚠️
```

---

# 🛠️ Technologies Used

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Joblib
- Logistic Regression

---

# 📈 Model Pipeline

1. Load Wisconsin Breast Cancer Dataset.
2. Perform data preprocessing.
3. Split data into training and testing sets.
4. Train a Logistic Regression classifier.
5. Evaluate model performance.
6. Save the trained model using Joblib/Pickle.
7. Load the model in Streamlit.
8. Accept user input.
9. Predict whether the tumor is Benign or Malignant.
10. Display the prediction on the web interface.

---

# 💻 How the Application Works

```
User Input
     │
     ▼
Streamlit Form
     │
     ▼
Input Validation
     │
     ▼
Trained Logistic Regression Model
     │
     ▼
Prediction
     │
     ▼
Display Result
```

---

# 📌 Future Improvements

- Add multiple ML algorithms for comparison.
- Improve UI/UX with interactive charts.
- Deploy on Streamlit Cloud or Render.
- Display prediction probability.
- Add feature importance visualization.

---

# 📄 License

This project is intended for educational and learning purposes.

---
