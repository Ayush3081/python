mango_price = 40
banana_price = 50
pineapple_price = 30

print("Welcome to the Juice Shop!")
print("1. Mango Juice — ", mango_price)
print("2. Banana Juice — ", banana_price)
print("3. Pineapple Juice — ", pineapple_price)


mango_qty = int(input("Enter quantity of Mango Juice: "))
banana_qty = int(input("Enter quantity of Banana Juice: "))
pineapple_qty = int(input("Enter quantity of Pineapple Juice: "))

bill = (mango_price * mango_qty) + (banana_price * banana_qty) + (pineapple_price * pineapple_qty)
print("Your total bill is: ", bill)

x = True
discount = 0.1 * bill * True
print("Your discount is: ", discount)

total_bill = bill - discount
print("Your total bill after discount is: ", total_bill)
















