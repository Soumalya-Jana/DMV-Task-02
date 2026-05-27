# Weather Advisory System
def weather_advisor(weather_type, temperature_celsius):
    weather = weather_type.lower()
    
    if weather == "rainy":
        return "Take an umbrella and wear waterproof shoes."
        
    elif weather == "snowy" and temperature_celsius < 0:
        return "Wear a heavy winter coat, gloves, and boots."
        
    elif weather == "sunny":
        if temperature_celsius > 30:
            return "Wear light clothing, sunglasses, and apply sunscreen."
        else:
            return "Wear sunglasses and a light jacket."
            
    else:
        return "Check the local forecast for more specific advice."

print(weather_advisor("Rainy", 15)) 
print(weather_advisor("Sunny", 35)) 
print(weather_advisor("Sunny", 20))  