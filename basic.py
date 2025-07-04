# print(5&6)
# print(5|6)
# print(5^6)
# print(5<<6)
# print(5>>6)

# x = 5
# print(x*2+3) 

# x = 5
# x=x+1
# print(x*(3+2))

# x = input("Enter a number: ")
# y = input("Enter another number: ")
# z =( .5*float(x)*float(y))
# print("The area of the triangle is: ", z)

# x = input("Enter a number of x : ")
# y = input("Enter another number of y : ")
# x,y = y,x
# print("x =",x)
# print("y =",y) 


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

# import math as m # To impport math modole with an alias
# x = m.sqrt(16)
# print("The square root of 12 is: ", x)

# from math import * # To import all functions from the math module
# x = gcd(16,12)
# print("The square root of 16 is: ", x)

# x = 2
# y = 3
# print(x,y ,sep="*") # To print x and y with a separator

# x =10
# y = 3.5
# z = "Akanksha"
# print("hello,{2} x = {0}, y = {1}".format(x, y, z))















