successful = False  # This is if the call attempt got thru, then the var successful is true
for number in range(3):
    print("Attempt", (number + 1), (number + 1) * "*")

    if successful:  # This will cause the above loop to break if the attempt was successful
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")  # This will print the message if the for loop ends up being False, if the for
    # loop ends up being True, it will not print
