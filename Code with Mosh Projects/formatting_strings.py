first = "Chris"
last = "Smith"
full = f"{first} {last}"  # Formatted String -  This will replace what's inside the curly braces at run time.
print(full)

first = "Chris"
last = "Smith"
full = f"{len(first)} {last}"  # You can call any built-in functions inside the curly braces and it will run
print(full)

first = "Chris"
last = "Smith"
full = f"{len(first)} {2 + 2}"  # Can also add expressions inside the curly braces like this
print(full)
