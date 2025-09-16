# Starter file for the Smoothie Shop Calculator exercise

print("Welcome to the Smoothie Shop!")

# TODO: Ask the user for their name using input()
print("Hello, what is your name?")
name = input()
# TODO: Ask how many smoothies they want to buy
number = int(input("How many smoothies of untitled flavour would you like to purchase"))

# TODO: Convert the number of smoothies to an integer

#I already did that lmfao 

# TODO: Calculate the total cost (each smoothie costs £3.50)
price = number * 3.50

# TODO: Display a message using a formatted string
print(f"You have ordered {number}")
print(f"Your total comes to £{price}") 
# OPTIONAL CHALLENGE:
# Ask if the customer wants a reusable cup for £1.00 extra
approve = input("Would you like to purchase a reusable cup for £1.00?")

# Add the cost if they say yes
if approve =="yes":
  cup = price + 1
  print(f"Your total comes to £{cup}")
