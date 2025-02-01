"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
# Charge for this sign.
charge = 35.00
# Number of characters.
numChars = int(input("How many letters do you want? "))
# Color of characters.
color = input("What color do you want? ")
# Type of wood.
woodType = input("What kind of wood do you want? ")

# Write assignment and if statements here as appropriate.
if numChars > 5:
  charge += (numChars - 5) * 4
if woodType == "oak":
  charge += 20
if color == "gold":
  charge += 15

# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))
