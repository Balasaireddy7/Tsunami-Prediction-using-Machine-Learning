import streamlit as st
import pandas as pd
import pickle

# Load trained model
with open('best_rf_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.set_page_config(page_title=" Tsunami Prediction App", layout="centered")
st.title('Tsunami Prediction App')
st.write('This app predicts the likelihood of a tsunami based on earthquake parameters.')

# User Inputs
st.subheader("Enter Earthquake Parameters")

magnitude = st.number_input('Magnitude', min_value=0.0, max_value=10.0, value=7.0, step=0.1)
cdi = st.number_input('CDI', min_value=0.0, max_value=10.0, value=5.0, step=0.1)
mmi = st.number_input('MMI', min_value=0.0, max_value=10.0, value=5.0, step=0.1)
sig = st.number_input('Significance (Sig)', min_value=0, max_value=3000, value=800, step=10)
nst = st.number_input('NST', min_value=0, max_value=1000, value=200, step=10)
dmin = st.number_input('Dmin', min_value=0.0, max_value=20.0, value=1.0, step=0.1)
gap = st.number_input('Gap', min_value=0.0, max_value=300.0, value=25.0, step=1.0)
depth = st.number_input('Depth', min_value=0.0, max_value=700.0, value=70.0, step=1.0)
latitude = st.number_input('Latitude', min_value=-90.0, max_value=90.0, value=0.0, step=0.1)
longitude = st.number_input('Longitude', min_value=-180.0, max_value=180.0, value=0.0, step=0.1)
month = st.number_input('Month', min_value=1, max_value=12, value=6, step=1)

# Create input DataFrame
input_data = pd.DataFrame({
    'magnitude': [magnitude],
    'cdi': [cdi],
    'mmi': [mmi],
    'sig': [sig],
    'nst': [nst],
    'dmin': [dmin],
    'gap': [gap],
    'depth': [depth],
    'latitude': [latitude],
    'longitude': [longitude],
    'Month': [month]
})

# Align columns with model (in case of order differences)
input_data = input_data.reindex(columns=model.feature_names_in_, fill_value=0)

# Predict button
if st.button('Predict Tsunami'):
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success(' **Prediction: Tsunami likely!** ⚠️')
    else:
        st.info('**Prediction: No tsunami likely.**')
