import streamlit as st
import pandas as pd
import joblib

#  Load model directly from GitHub repo
model = joblib.load("energy_model.pkl")

st.title(" Energy Consumption Predictor")

# Input fields
hour = st.slider("Hour", 0, 23)
day = st.slider("Day", 1, 31)
month = st.slider("Month", 1, 12)
weekday = st.slider("Weekday", 0, 6)
z1_plug = st.number_input("Zone 1 Plug (kW)")
z2_ac1 = st.number_input("Zone 2 AC1 (kW)")
z2_ac2 = st.number_input("Zone 2 AC2 (kW)")
z2_ac3 = st.number_input("Zone 2 AC3 (kW)")
z2_ac4 = st.number_input("Zone 2 AC4 (kW)")
z2_light = st.number_input("Zone 2 Light (kW)")
z2_plug = st.number_input("Zone 2 Plug (kW)")
z3_light = st.number_input("Zone 3 Light (kW)")
z3_plug = st.number_input("Zone 3 Plug (kW)")

input_data = pd.DataFrame([[hour, day, month, weekday, z1_plug, z2_ac1, z2_ac2, z2_ac3, z2_ac4, z2_light, z2_plug, z3_light, z3_plug]],
                          columns=['hour', 'day', 'month', 'weekday', 'z1_Plug(kW)', 'z2_AC1(kW)', 'z2_AC2(kW)', 'z2_AC3(kW)', 'z2_AC4(kW)',
                                   'z2_Light(kW)', 'z2_Plug(kW)', 'z3_Light(kW)', 'z3_Plug(kW)'])

prediction = model.predict(input_data)
st.success(f" Predicted Zone 1 Light Consumption: {prediction[0]:.2f} kW")
