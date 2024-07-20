# in this example, if the inputed number is divisible by 3 we will print the message 'Fizz', if the inputed number is divisible by 5 we will print the message 'Buzz',
# if the number is divisible by both 3 and 5 we will print "FizzBuzz" otherwise we return the entered number.

def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return 'FizzBuzz'
    if input % 3 == 0:
        return 'Fizz'
    if input % 5 == 0:
        return 'Buzz'
    return input

print(fizz_buzz(4))