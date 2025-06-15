import streamlit as st
import requests

st.set_page_config(page_title="Cirrhosis Stage Predictor", layout="centered")
st.title("🩺 Cirrhosis Stage Prediction")
st.markdown("Provide the following clinical values:")

# Collect user inputs
fields = {
    "Age": st.number_input("Age", min_value=0.0),
    "Sex": st.selectbox("Sex", ["Male", "Female"]),
    "Ascites": st.selectbox("Ascites", ["No", "Yes"]),
    "Hepatomegaly": st.selectbox("Hepatomegaly", ["No", "Yes"]),
    "Spiders": st.selectbox("Spiders", ["No", "Yes"]),
    "Edema": st.selectbox("Edema", ["No", "Yes"]),
    "Bilirubin": st.number_input("Bilirubin", min_value=0.0),
    "Cholesterol": st.number_input("Cholesterol", min_value=0.0),
    "Albumin": st.number_input("Albumin", min_value=0.0),
    "Copper": st.number_input("Copper", min_value=0.0),
    "Alk_Phos": st.number_input("Alkaline Phosphatase", min_value=0.0),
    "SGOT": st.number_input("SGOT", min_value=0.0),
    "Tryglicerides": st.number_input("Tryglicerides", min_value=0.0),
    "Platelets": st.number_input("Platelets", min_value=0.0),
    "Prothrombin": st.number_input("Prothrombin", min_value=0.0)
}

# Encode categorical
sex_map = {"Male": 1, "Female": 0}
yesno_map = {"Yes": 1, "No": 0}

payload = {
    "Age": fields["Age"],
    "Sex": sex_map[fields["Sex"]],
    "Ascites": yesno_map[fields["Ascites"]],
    "Hepatomegaly": yesno_map[fields["Hepatomegaly"]],
    "Spiders": yesno_map[fields["Spiders"]],
    "Edema": yesno_map[fields["Edema"]],
    "Bilirubin": fields["Bilirubin"],
    "Cholesterol": fields["Cholesterol"],
    "Albumin": fields["Albumin"],
    "Copper": fields["Copper"],
    "Alk_Phos": fields["Alk_Phos"],
    "SGOT": fields["SGOT"],
    "Tryglicerides": fields["Tryglicerides"],
    "Platelets": fields["Platelets"],
    "Prothrombin": fields["Prothrombin"]
}

# Predict
if st.button("🔍 Predict Stage"):
    try:
        res = requests.post("http://localhost:8000/predict", json=payload)
        if res.status_code == 200:
            result = res.json()
            st.success(f"Predicted Cirrhosis Stage: **{result['predicted_stage']}**")
        else:
            st.error(f"Error: {res.json().get('error')}")
    except Exception as e:
        st.error(f"Request failed: {e}")
