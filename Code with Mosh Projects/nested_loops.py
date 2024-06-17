for x in range(
        5):  # This is the outer loop or the loop that excuted first, and is why the pairs of coordinates start with 0
    for y in range(3):  # This is the inner loop and executes after the outer loops whichs gives us the 2nd "0" in (0,0)
        print(
            f"({x},{y})")  # This then prints every combination of the above 2 number ranges, (0,0) (0,1) (0,2) (1,0) (1,1) etc etc...
