print("===== MOVIE BOOKING =====")

print("1. Avengers - ₹200")
print("2. Superman - ₹180")
print("3. Batman - ₹150")

choice = int(input("Choose movie: "))
tickets = int(input("Enter number of tickets: "))

if choice == 1:
    movie = "Avengers"
    price = 200

elif choice == 2:
    movie = "Superman"
    price = 180

elif choice == 3:
    movie = "Batman"
    price = 150

else:
    print("Invalid movie")
    exit()

total = price * tickets

if tickets >= 5:
    discount = total * 0.10
else:
    discount = 0

final_amount = total - discount

print("\n===== BILL =====")
print("Movie:", movie)
print("Tickets:", tickets)
print("Total:", total)
print("Discount:", discount)
print("Final Amount:", final_amount)