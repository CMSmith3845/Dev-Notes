# def multiply(x, y):
#    return x * y


# multiply(2, 3, 4, 5)  # this will not work because we have only 2 parameters up top


# to fix this we have to write the code this way

# def multiply(*numbers):
#    print(numbers)

# multiply(2, 3, 4, 5)  # This will generate a tuple with these numbers i.e. (2,3,4,5), and tuples are iterable

# def multiply(*numbers):  # This will iterate over the tuple and print each number on a new line
#   for number in numbers:
#        print(number)


# multiply(2, 3, 4, 5)


def multiply(*numbers):  # creates the tuple of (2,3,4,5)
    total = 1  # set the var 'total' to 1
    for number in numbers:  # for each number in numbers we multiply total times it, so 1 * 2 = 2, then 2 * 3 = 6 etc...
        total *= number  # could also be written as total = total * number
    return total  # returns the total but need to make sure its not part of the for loop


print(multiply(2, 3, 4, 5))  # prints the solution to multiplying the numbers in tuple.
