import requests
import streamlit as st
import plotly.graph_objects as go

st.title("🌤️ Live Weather Dashboard")

city = st.text_input("Enter city name", "saharanpur")

api_key = "15ceb54037ee90c094aab85e582b5e0b"  # <-- Yahan apna OpenWeatherMap API key paste karo
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()
if data["cod"] == 200:
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]
    desc = data["weather"][0]["description"]

    st.subheader(f"Weather in {city}")
    st.write(f"🌡️ Temperature: {temp}°C")
    st.write(f"💧 Humidity: {humidity}%")
    st.write(f"💨 Wind Speed: {wind} m/s")
    st.write(f"☁️ Description: {desc}")

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=temp,
        title={'text': "Temperature (°C)"},
        gauge={'axis': {'range': [-10, 50]}}
    ))

    st.plotly_chart(fig)

else:
    st.error("City not found.")
