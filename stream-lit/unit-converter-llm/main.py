import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
secret_key = os.getenv("MY_SECRET_KEY")
# Gemini API setup
genai.configure(api_key=secret_key)

# Offline conversion dictionary (basic units)
conversion_rates = {
    "Meter": {"Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000, "Mile": 0.000621371, "Yard": 1.09361, "Foot": 3.28084, "Inch": 39.3701},
    "Kilogram": {"Gram": 1000, "Pound": 2.20462, "Ounce": 35.274},
    "Celsius": {"Fahrenheit": lambda c: (c * 9/5) + 32, "Kelvin": lambda c: c + 273.15}
}

# Function to convert using Gemini AI
def convert_using_gemini(query):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(query)
    return response.text

# Function to convert offline
def convert_offline(value, from_unit, to_units):
    if from_unit in conversion_rates:
        results = {}
        for to_unit in to_units:
            conversion = conversion_rates[from_unit].get(to_unit)
            if conversion:
                results[to_unit] = conversion(value) if callable(conversion) else value * conversion
        return results
    return None

# Streamlit UI
st.title("🚀 Advanced Unit Converter with Chat(AI)")

# Select category
category = st.selectbox("Select Category", list(conversion_rates.keys()))

# Input and dropdowns
value = st.number_input("Enter Value:", min_value=0.0, step=0.01)
from_unit = st.selectbox("From", list(conversion_rates.keys()))
to_units = st.multiselect("Convert To (Select multiple)", conversion_rates[from_unit].keys())

# Convert Button
if st.button("Convert"):
    if to_units:
        offline_result = convert_offline(value, from_unit, to_units)
        if offline_result:
            st.success(f"Offline Conversion: {offline_result}")
        else:
            ai_query = f"Convert {value} {from_unit} to {', '.join(to_units)}."
            ai_result = convert_using_gemini(ai_query)
            st.success(f"AI Conversion: {ai_result}")
    else:
        st.warning("⚠️ Please select at least one unit to convert to!")

# Basic Chat Feature
st.subheader("💬 Chat with AI")
user_message = st.chat_input("Ask me anything...")
if user_message:
    chat_response = convert_using_gemini(user_message)
    st.write("🤖 AI:", chat_response)
