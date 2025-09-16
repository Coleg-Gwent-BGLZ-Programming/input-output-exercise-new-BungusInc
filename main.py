# Starter file for the Smoothie Shop Calculator exercise

print("Welcome to the Smoothie Shop!")
approve = None
options = ("yes" , "no")
# TODO: Ask the user for their name using input()
print("Hello, what is your name?")
name = input()
print(f"Hello, {name}.")
# TODO: Ask how many smoothies they want to buy
number = input("How many smoothies of untitled flavour would you like to purchase")

# TODO: Convert the number of smoothies to an integer
number = int(number)

# TODO: Calculate the total cost (each smoothie costs £3.50)
price = number * 3.50

# TODO: Display a message using a formatted string
print(f"You have ordered {number}")
print(f"Your total comes to £{price}") 
# OPTIONAL CHALLENGE:
# Ask if the customer wants a reusable cup for £1.00 extra
while approve  not in options 
  approve = input("Would you like to purchase a reusable cup for £1.00?  :").lower()
if approve == "yes":
  price +=1
  print(f"The total comes to £{price}")
else:
  print("Ok.")

# Add the cost if they say yes

