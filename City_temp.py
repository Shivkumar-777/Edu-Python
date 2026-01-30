city_data = {
    "Name" : "Delhi",
    "Temperature": 25,
    "Carbon_Footprint" : 500.75,
    "Is_Sustanable" : False
}

print(f"City data : {city_data}")

city_data['AQI'] = 100
print(f"Update 1 : City data : {city_data}")

del city_data['Temperature']
print(f"Update 2 : City data : {city_data}")

city_data['Temperature'] = 26
print(f"Update 3 : City data : {city_data}")

