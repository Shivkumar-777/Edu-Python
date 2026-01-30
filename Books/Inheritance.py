# Inheritance

class SolarEnergySystem(EnergySystem):
  def __init__(self, building_name, energy_consumption, emission_factor, solar_production):
    super().__init__(building_name, energy_consumption, emission_factor)
    self.solar_production = solar_production

  def net_energy_consumption(self):
    return self.energy_consumption - self.solar_production

solar_building1 = SolarEnergySystem("Solar Building A", 5000, 0.45, 1500)
net_consumption = solar_building1.net_energy_consumption()

print("Net Energy Consumption:", net_consumption, "kWh")