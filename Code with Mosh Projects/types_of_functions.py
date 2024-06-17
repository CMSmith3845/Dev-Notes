def greet(name):
    print(f"Hi {name}")


#  In this function we are locked to just printing the output to the terminal

def get_greeting(name):
    return f"Hi,{name}"


message = get_greeting("Mosh")
print(message)

# In this function since we are returning the "Mosh" and assigning it to a variable we have a lot more options of the
# things we can do with it.
