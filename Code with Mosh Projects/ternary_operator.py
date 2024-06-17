age = 22
if age >= 18:
    print("Eligible")
else:
    print("Inelgible")

# Another way to write this code is to assign Eligible or Inelgible to a variable

age = 22
if age >= 18:
    message = "Eligible"
else:
    message = "Ineligble"
print(message)

# Another easier way to write this with the variable is as follows
age = 22
message = "Eligible" if age >= 18 else "Not Eligible"  # This is the ternary operator
print(message)
