expenses = []

while True:
    print("\n1. Add Expense")
    print("2. Show Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Expense name: ")
        amount = float(input("Amount: "))

        expenses.append([name, amount])
        print("Expense added!")

    elif choice == "2":
        for expense in expenses:
            print(expense[0], "=", expense[1])

    elif choice == "3":
        total = 0

        for expense in expenses:
            total += expense[1]

        print("Total Expense =", total)

    elif choice == "4":
        break

    else:
        print("Invalid choice.")