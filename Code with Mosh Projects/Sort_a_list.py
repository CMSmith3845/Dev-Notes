numbers = []
numbers = float(input('Enter your list of numbers '))
sorted_numbers = input('How would you like these sorted? ')


if sorted_numbers == 'asc':
    arr.sort()
    print(numbers)

if sorted_numbers == 'desc':
    split_numbers.sort(reverse=True)
    print(split_numbers)

if sorted_numbers == 'none':
    print(split_numbers)
