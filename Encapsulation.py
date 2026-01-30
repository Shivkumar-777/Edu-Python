# Encapsulation

class EnergySystem:
  def __init__(self, building_name, energy_consumption, emission_factor):
    self._building_name = building_name
    self._energy_consumption = energy_consumption
    self._emission_factor = emission_factor

  def get_energy_consumption(self):
    return self._energy_consumption

  def calculate_carbon_footprint(self):
    return self._energy_consumption * self._emission_factor

  building = EnergySystem("Building A", 5000, 0.45)
  print("Building Name:", building._building_name)
  print("Energy Consumption:", building.get_energy_consumption(), "kWh")