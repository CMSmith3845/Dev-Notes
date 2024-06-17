# calculate the sum of numbers from 1 to 10 using a for loop

sum_numbers = 0
for num in range(1, 11):
    sum_numbers += num
print(sum_numbers)

# Print the elements of a list using a for loop
list = [1, 2, 3, 4, 5, 2.32, "for"]  # could also use element in place of num
for num in list:
    print(num)  # Want to make sure we print the varible in the for statement so we are acutally using teh for statement

# calculate the elements in a list using the for loop

list_1 = [1, 2, 3, 4, 5]
multi_num = 1
for num in list_1:
    multi_num *= num
print(multi_num)

# print even numbers from 1 to 10 using a for loop

for number in range(0, 11, 2):
    print(number)

# print numbers in reverse from 10 to 1 using a for loop

for numbers in range(10, 0, -1):  # The -1 increments down 1 in reverse order
    print(numbers)
