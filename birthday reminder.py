name = input("Enter your name: ")
birthday = input("Enter your birthday (DD-MM): ")

print("\n🎂 Birthday Reminder")
print("Name:", name)
print("Birthday:", birthday)

reminder = input("Do you want a birthday reminder? (yes/no): ").lower()

if reminder == "yes":
    print("🔔 Reminder set successfully!")
else:
    print("Reminder not set.")