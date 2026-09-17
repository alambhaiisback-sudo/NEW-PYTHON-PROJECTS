print("===== PARKING FEE CALCULATOR =====")

name = input("Enter your name: ")
hours = int(input("Enter parking hours: "))

if hours == 1:
    fee = 20

elif hours == 2:
    fee = 30

elif hours == 3:
    fee = 40

elif hours >= 4:
    fee = hours * 50

else:
    fee = 0

print("\n----- PARKING BILL -----")
print("Name:", name)
print("Parking Hours:", hours)
print("Total Fee: ₹", fee)