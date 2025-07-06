print(" Welcome to KBC (Kaun Banega Crorepati) ")
print("You will be asked 1st question. Choose the correct option to win ₹1,00,000!\n")

# Question
print("Question: how many years of b.tech degree ?")
print("A. 2 years")
print("B. 1 years ")
print("C. 4 years ")
print("D. 5 years ")

# Taking input from user
answer = input("Enter your answer (A/B/C/D): ")

# Converting answer to uppercase (in case user enters lowercase)
answer = answer.upper()

# Checking answer using if-else
if answer == "C":
    print(" Congratulations! You have won ₹1,00,000! ")
elif answer in ["A", "B", "D"]:
    print(" Sorry, that's the wrong answer. The correct answer is C. 4 years .")
else:
    print(" Invalid option. Please choose A, B, C, or D.")
    
print("You will be asked 2nd question. Choose the correct option to win ₹10,00,000!\n")

# Question
print("Question: HOw many day's in a week ?")
print("A. 5 ")
print("B. 7")
print("C. 10")
print("D. 4")

# Taking input from user
answer = input("Enter your answer (A/B/C/D): ")

# Converting answer to uppercase (in case user enters lowercase)
answer = answer.upper()

# Checking answer using if-else
if answer == "B":
    print(" Congratulations! You have won ₹10,00,000! ")
elif answer in ["A", "c", "D"]:
    print(" Sorry, that's the wrong answer. The correct answer is B. 7 Day's .")
else:
    print(" Invalid option. Please choose A, B, C, or D.")
    print("you lost 1 Lakh also ")