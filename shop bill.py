total = 0

while True:

    product = input("Enter product name (done to finish): ")

    if product.lower() == "done":
        break

    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    amount = price * quantity
    total += amount

    print(product, "=", amount)

gst = total * 0.18
final_amount = total + gst

print("\n===== FINAL BILL =====")
print("Total:", total)
print("GST:", gst)
print("Final Amount:", final_amount)