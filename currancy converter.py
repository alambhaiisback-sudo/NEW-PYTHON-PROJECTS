amount = float(input("Enter amount in INR: "))

print("1. INR to USD")
print("2. INR to EUR")
print("3. INR to GBP")

choice = int(input("Choose option: "))

if choice == 1:
    usd = amount / 83
    print("USD:", usd)

elif choice == 2:
    eur = amount / 90
    print("EUR:", eur)

elif choice == 3:
    gbp = amount / 105
    print("GBP:", gbp)

else:
    print("Invalid choice")