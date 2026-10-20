import pandas as pd
import streamlit as st
import pickle
from pathlib import Path

MODEL_PATH = Path(__file__).with_name("svc_trained_model.pkl")
with MODEL_PATH.open("rb") as f:
    model = pickle.load(f)

st.title("Titanic Passenger Survival Prediction")

pclass = st.selectbox("Passenger Class", ["First", "Second", "Third"])
gender = st.selectbox("Gender", ["Female", "Male"])
sibling = st.selectbox("Siblings aboard", ["Zero", "One", "Two", "Three"])
embarked = st.selectbox("Port of Embarkation", ["Cherbourg", "Queenstown", "Southampton"])

# Match the LabelEncoder category order used when the saved model was trained.
pclass_val = {"First": 0, "Second": 1, "Third": 2}[pclass]
gender_val = {"Female": 0, "Male": 1}[gender]
sibling_val = {"One": 0, "Three": 1, "Two": 2, "Zero": 3}[sibling]
embarked_val = {"Cherbourg": 0, "Queenstown": 1, "Southampton": 2}[embarked]

if st.button("Predict"):
    X = pd.DataFrame(
        [[pclass_val, gender_val, sibling_val, embarked_val]],
        columns=["PClass", "Gender", "Sibling", "Embarked"],
    )
    pred = model.predict(X)[0]
    if pred == 1:
        st.success("Survived")
    else:
        st.error("Did not survive")
