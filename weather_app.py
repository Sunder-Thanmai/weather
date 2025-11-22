import streamlit as st
import requests

st.set_page_config(page_title="Weather Report + Tips", page_icon="🌤️")

API_KEY = "7c65fd4ac346d7ab4a58e78bb8b80bb6"   # <-- put your key

# --------------------- FUNCTIONS -------------------------

def get_precautions(desc, temp):
    desc = desc.lower()
    t = float(temp)

    if "rain" in desc:
        return [
            "Carry an umbrella 🌂",
            "Wear waterproof shoes",
            "Avoid riding a bike without a raincoat"
        ]
    elif "haze" in desc or "mist" in desc or "fog" in desc:
        return [
            "Use sunscreen",
            "Wear light cotton clothes",
            "Stay hydrated"
        ]
    elif "cloud" in desc:
        return [
            "Weather is normal",
            "Carry a light jacket just in case"
        ]
    elif t > 32:
        return [
            "Very hot! Drink plenty of water",
            "Avoid going out in the afternoon",
            "Wear cotton clothes"
        ]
    elif t < 16:
        return [
            "Very cold! Wear sweater, jacket & gloves"
        ]
    else:
        return ["Normal weather"]


def get_dress_code(desc, temp):
    desc = desc.lower()
    t = float(temp)

    if "rain" in desc:
        return "Raincoat, waterproof shoes, dark clothes"
    elif "haze" in desc or "mist" in desc or "fog" in desc:
        return "Mask, warm hoodie, full sleeves"
    elif "clear" in desc:
        return "Cotton T-shirt, cap, sunglasses"
    elif "cloud" in desc:
        return "Casual wear, light jacket"
    elif t > 32:
        return "Very light cotton clothing, cap, sunglasses"
    elif t < 16:
        return "Sweater, jacket, gloves"
    else:
        return "Normal casual clothing"

# --------------------- UI ------------------------------

st.title("Weather Report + Tips 🌤️🌧️")

city = st.text_input("City name", "Hyderabad")

if st.button("Get Weather"):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    res = requests.get(url)

    if res.status_code == 200:
        data = res.json()

        # Storing in variables like you asked
        desc = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        feels = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]

        # Call functions -> store output in variables
        precautions = get_precautions(desc, temp)
        dress_code = get_dress_code(desc, temp)

        # Displaying on Streamlit
        st.subheader("🌦 Weather Report")
        st.write(f"*Weather:* {desc}")
        st.write(f"*Temperature:* {temp}°C")
        st.write(f"*Feels Like:* {feels}°C")
        st.write(f"*Humidity:* {humidity}%")

        st.subheader("🛡 Precautions")
        for p in precautions:
            st.write("• " + p)

        st.subheader("👗 Dress Code Recommendation")
        st.write(dress_code)

    else:
        st.error("City not found. Try again!")