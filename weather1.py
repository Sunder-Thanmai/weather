import requests
city_name=input("enter city name =")
API_KEY="7c65fd4ac346d7ab4a58e78bb8b80bb6"
url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
 
response=requests.get(url)
def get_precautions(desc,temp):
    desc=desc.lower()
    t=float(temp)
    if "rain" in desc:
        return [
            "carry an umbrella"
            "wear waterproof shoes"
            "avoid riding a bike without raincoat"
        ]
    elif "haze" in desc or "mist" in desc or "fog" in desc:
        return [
            "use sunscreen"
            "wear light cotton clothes"
            "stay hydrated" 
        ]
    elif "cloud" in desc:
        return [
            "weather is normal"
            "carry a light jacket just in case"
        ]
    elif t>=32:
        return [
            "very hot! Drink plenty of water"
            "Avoid going out in the afternoon"
            "wear cotton clothes"
        ]
    elif t<=16:
        return ["Weather is normal"]
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
    elif t >= 32:
        return "Very light cotton clothing, cap, sunglasses"
    elif t <= 16:
        return "Sweater, jacket, gloves"
    else:
        return "Normal casual clothing"
if response.status_code == 200:
    data = response.json()

    desc = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    feels = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]

    print("\nWeather Report")
    print("---------------------------")
    print("Weather:", desc)
    print("Temperature:", temp, "°C")
    print("Feels Like:", feels, "°C")
    print("Humidity:", humidity, "%")

    print("\nPrecautions:")
    for p in get_precautions(desc, temp):
        print("•", p)

    print("\nRecommended Dress Code:")
    print(get_dress_code(desc, temp))

else:
    print("Invalid city or API error")