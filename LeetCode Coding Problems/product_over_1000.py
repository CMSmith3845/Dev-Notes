numbers = input('Enter two numbers seperated by a space')


#This works but i want to add a qualifier function to make sure the input is a number, need to learn more before i can do that though

def splitting_numbers():
    split_numbers = numbers.split()
    split_1 = int(split_numbers[0])
    split_2 = int(split_numbers[1])
    product = split_1 * split_2
    if product >= 1000:
        print(product)
    if product < 1000:
        addition = split_1 + split_2
        print(addition)

splitting_numbers()