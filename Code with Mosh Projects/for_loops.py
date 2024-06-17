for number in range(3):
    print("Attempt")  # This will attempt 3 times because of range(3)

for number in range(3):
    print("Attempt", number)  # This will number the attempts 0,1,2

for number in range(3):
    print("Attempt", number + 1)  # This will number the attempts 1,2,3, a little more meaningful to users

for number in range(3):
    print("Attempt", number + 1, (
            number + 1) * ".")  # This will put .,..,... on the end of attempt, need the number +1 so it doesn't start with 0 "."'s

for number in range(1, 4):
    print("Attempt", number,
          number * ".")  # This will do the same as above code except its cleaner, the 1,4 range in the first line will decide the number of attempts

for number in range(1, 10, 2):
    print("Attempt", number,
          number * ".")  # This will count 1 to 10 but do it in increments of 2 starting at 1, so 1,3,5,7,9
