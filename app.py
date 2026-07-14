import streamlit as st
import pickle
import numpy as np
with open("model/model.pkl", "rb") as file:
    model = pickle.load(file)

st.set_page_config(
    page_title="Breast Cancer Prediction",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 Breast Cancer Prediction")
st.write("Enter the patient's tumor measurements below.")
feature_names = [
    "mean_radius",
    "mean_texture",
    "mean_perimeter",
    "mean_area",
    "mean_smoothness",
    "mean_compactness",
    "mean_concavity",
    "mean_concave_points",
    "mean_symmetry",
    "mean_fractal_dimension",
    "radius_error",
    "texture_error",
    "perimeter_error",
    "area_error",
    "smoothness_error",
    "compactness_error",
    "concavity_error",
    "concave_points_error",
    "symmetry_error",
    "fractal_dimension_error",
    "worst_radius",
    "worst_texture",
    "worst_perimeter",
    "worst_area",
    "worst_smoothness",
    "worst_compactness",
    "worst_concavity",
    "worst_concave_points",
    "worst_symmetry",
    "worst_fractal_dimension",
]

inputs = []

col1, col2 = st.columns(2)

for i, feature in enumerate(feature_names):

    if i % 2 == 0:
        with col1:
            value = st.number_input(
                feature.replace("_", " ").title(),
                value=0.0,
                format="%.6f"
            )
    else:
        with col2:
            value = st.number_input(
                feature.replace("_", " ").title(),
                value=0.0,
                format="%.6f"
            )

    inputs.append(value)

if st.button("Predict"):

    data = np.array([inputs])

    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)

    confidence = np.max(probability) * 100

    st.divider()

    if prediction == 1:
        st.error("Prediction: Malignant(⚠️Cancerous)")
    else:
        st.success("Prediction: Benign(✅non Cancerous)")

    st.write(f"**Confidence:** {confidence:.2f}%")

    st.subheader("Prediction Probabilities")

    st.write(f"Benign : {probability[0][0]*100:.2f}%")
    st.write(f"Malignant : {probability[0][1]*100:.2f}%")