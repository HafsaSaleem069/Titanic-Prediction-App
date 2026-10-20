# Titanic Passenger Survival Prediction

A small Streamlit app that predicts Titanic passenger survival from passenger class, gender, sibling count, and port of embarkation.

## Run locally

```bash
python -m pip install -r requirements.txt
streamlit run app.py
```

The trained model file, `svc_trained_model.pkl`, must remain in the repository root beside `app.py`.

## Deploy on Streamlit Community Cloud

1. Sign in at [share.streamlit.io](https://share.streamlit.io/) with GitHub.
2. Choose **Create app** and select this repository, the `main` branch, and `app.py` as the entrypoint.
3. Deploy. Community Cloud installs the packages from `requirements.txt`.
