class EnergySystem:

  def __init__(self, building_name, energy_consumption, emission_factor):
    self.building_name = building_name
    self.energy_consumption = energy_consumption
    self.emission_factor = emission_factor

building1 = EnergySystem("Building A", 5000, 0.45)
building2 = EnergySystem("Building B", 8000, 0.60)
building3 = EnergySystem("Building C", 3000, 0.30)

total_energy_consumption = building1.energy_consumption + building2.energy_consumption + building3.energy_consumption
total_emission = building1.energy_consumption * building1.emission_factor + building2.energy_consumption * building2.emission_factor + building3.energy_consumption * building3.emission_factor

print("Total Energy Consumption:", total_energy_consumption, "kWh")
print("Total Emission:", total_emission, "kg CO2e")

def calculate_carbon_footprint(self):
  return self.energy_consumption * self.emission_factor

def calculate_energy_savings(self):
  return self.energy_consumption * 0.10

print("Carbon Footprint:", calculate_carbon_footprint(building1), "kg CO2e")
print("Energy Savings:", calculate_energy_savings(building1), "kWh") 