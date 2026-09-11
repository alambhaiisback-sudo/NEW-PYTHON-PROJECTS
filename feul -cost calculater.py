distance = float(input("Enter distance in km: "))
mileage = float(input("Enter vehicle mileage (km/l): "))
petrol_price = float(input("Enter petrol price per litre: "))

fuel_needed = distance / mileage
total_cost = fuel_needed * petrol_price

print("\n--- FUEL CALCULATOR ---")
print("Distance:", distance, "km")
print("Fuel needed:", round(fuel_needed, 2), "litres")
print("Total cost: ₹", round(total_cost, 2))