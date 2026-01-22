# Filter and Manipulate Data to gind Sustainable cities 

city_data = [
    {"city": "City A", "temperature": 25, "carbon_footprint": 500, "is_sustainable": True},
    {"city": "City B", "temperature": 30, "carbon_footprint": 350, "is_sustainable": False},
    {"city": "City C", "temperature": 22, "carbon_footprint": 600, "is_sustainable": True},
    {"city": "City D", "temperature": 15, "carbon_footprint": 200, "is_sustainable": False},
    {"city": "City E", "temperature": 28, "carbon_footprint": 450, "is_sustainable": True},
]

sustainable_cities = []

for data in city_data:
    if data["is_sustainable"]:
        sustainable_cities.append(data["city"])

print(sustainable_cities)
     
