# Python Coding Course Notes 

## General Info
check out python PEPs and look at the code style guide to get an idea of what my code should look like so it matches what other programmers are doing.
'''
    #The program gets executed from top to bottom i.e.
    age = 20
    age = 30
    print(age)  # <--- this would output 30, because we changed the variable in the 2nd line'
'''
Can convert different types of data into other types of data using these functions
int()
float()
bool()
str()

Objects in programming are like objects in the real world, like the remote, the toaster. etc etc they have different capabilites and its the same in programming.  

There are general functions, like print, input, and then there are specific object functions that are called methods. these are function or methods that only affect the object they are attached to. 

When writing a program it will consist of thousands of lines of code. so it better to break it down into chunks called **functions**. 

## Intro to Python
who uses python?
people who already code
beginners, huge global community, wealth of documentation
useful in many areas, like data science, AI and machine learning, web development, and Internet of things with devices like raspberry Pi. 
Large organizations use Python. 
what makes python great
is a general purpose language, has a large standard library,
FOR DATA SCIENCE: these libraries are used, Pandas,NumPy,SciPy, and matplotlib
FOR AI: TensorFlow,PyTorch,Keras, and Scikit-learn
FOR NATURAL LANGUAGE PROCESSING: Natural Language Toolkit (NLTK)
Summary
 Python has clear and readable syntax
Python has a huge global community and wealth of documentation

## Data Types
there are different types of data in python, i.e. Numbers(Integers,Float), Strings, and Boolean
```
x = input("x: ")
y = int(x) + 1
print(f"x:  {x}, y: {y}")  # This will print x: 1, y: 2

# int(x)
# float(x)
# bool(x)
# str(x) types of different type switching

# in the boolean function we have truthy and falsy values
# Falsy - "", 0, none

# bool(0) will be false  bool("") will be false, all other strs will be true
# bool(1) will be true
# bool(-1) will be true
# bool(5) will be true

```

Integers: 11
Real numbers: 21.213
words: "hello Python 101"
can use the type() command in python to check and see the type of data in a line of code
type(11)  = Integer
type(21.213)  =  float
type("Hello, Python 101")  =  str (string)
integers can be negative or postive
floats are numbers inbetween integers. like 1.5 and 1.34 are inbetween 1 and 2
you can covert types of data to other types, called type casting
float(2):2.0 turns the integer 2 into the float 2.0
if you cast int(1.1):1 then you lose part of the data as the integer becomes 1
other types of data in python is BOOLEAN
they have 2 different statuses, True, False, first letters must be capital
type(True): bool
if you cast a boolean true to an integer you get a 1
int(True) --> 1
if you cast a boolean flase to an integer you get a 0
int(False) --> 0
if you cast a 1 to a bool you get a true
bool(1) --> True
if you cast a 0 to a bool you get a false
bool(0) --> False

## Introduction to using Jupyter
select a cell and then use Shift + Enter to execute that code.
putting "#" in front of anything you type will make the compiler ignore it i.e.
print('Hello World') # this is to practice writing notes
when executed the # this is to practice writing notes,  will not show up in the executed code.
If you spell something wrong in the code, it will generate a NameError
If you forget to close the code line it will generate a SyntaxError
Python can tell you when you have a mistake in your code as you write it, you don't have to compile it first for it to let you know that it has an error.

In Jupyter
pushing the stop button in the left hand menu put that notebook offline,

## Input Function
you can use the input function to interact with the terminal window. For instance you can get how old someone is like this.

```
birth_year = input('Enter your birth year ')
age = 2024 - int(birth_year)
print('You are',age,'years old')
```

This string of code will ask the user to input their birth year,  it will then store that in the variable "birth_year" it will then subtract the current year from their birth year, but it also has to covert the year they enter into an integer because python cannot subtract an int from a str. then it will print the results on the last line. Any input you get back from the input function on the terminal window will come back as a string. 

## Numbers
### Mathematical expressions
```
x = 1
x = 1.1
x = 1 + 2j  # These are complex numbers a + bi 'i' is the imaginary number

print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)  # This will return the float 3.3333
print(10 // 3)  # This will return an integer, so 3
print(10 % 3)  # This will return the remainder of the division calculation
print(10 ** 3)  # This will take 10 to the power of 3

x = 10
x = x + 3  #This statement
x += 3  # Is the same as this statement, the both increment x by 3, can use any of the math operators this way as well

```

```
import math  # This imports the math module which has a lot more methods for complex math equations

print(round(2.5))  # This will round the float to nearest whole number, 6 will round up, 5 will round down
print(abs(-2.9))  # this will return the absolute value of a number in this case 2.9

print(math.ceil(2.2))  # This will return the ceiling of a number
# to find all the methods in the math module, google search python 3.12(< or current version)
```
there are a few different operators we can use, + - * /, //(which returns an integer after doing the division), theres the % which will return the remainder after dividing 2 numbers, and there the ** which would be 10 ** 3, 10 to the power of 3
### Augmented Operators
there are augmented assignment operators that we can also use.
```
x = 10
x = x + 3
```
or we can do it with less code this way
```
x = 10
x += 3
```
Can replace the + with any other operator
### Comparison Operators
```
10 < 3
10 > 3
10 >= 3
10 <= 3
10 == 3
10 != 3 #not equal too
# can also compare strings
"bag" > "apple" # bag is greater because when sorted bag comes after apple.
"bag" == "BAG" # this would be false because captial and lowercase are not equal
```

```
x = 3 > 2
print(x)
```
This will return a value of True, because 3 is greater than 2 , if the first number was less than 2 the returned value would be False, can also use >=, <, <=, ==(equal too), !=(not equal too operator)

## And, or, not statements
### 'And' Operator (Both need to be true)
```
price = 8
print(price > 10 and price < 30)
```
in this piece of code the value that it will return will be False, because of the 'and' operator, for this code to be true the price would need to be more than 10 but less than 30, since its 8, the code of False.
### 'Or' Operator (at least one needs to be true)
```
price = 8
print(price > 10 or price < 30)
```
In this code it looks at the price and sees if it is greater than 10, and it is not so it keeps going and looks to see 'or' if it is less than 30. in this case the code would True
### 'Not Operator' (Inverses any value that is returned)
```
price = 8
print(not price > 10)
```
in this code the result would normally be False, because 8 is not greater than 10, but because of the not in there it inverts the result, making the code read True.

Expressions are a type of operation that computers perform.
like mathematical operations.
50+40+30  the numbers are operands and the +'s are the operators
+adds, -subtracts, *multiplies, /divides
in all the above cases these operators produce a FLOAT
we can use a // for integer division
variables can be assigned and then used by just inputting the variable name later i.e.
My_Variable = 1
then we can use My_Variable:1 + 1 = 2
we can store the results of multiple operations in a variable like this
x= 43+60+16+41, then x=160, to call that variable it then become x:160
then we can use x to assign a new value to a new variable like this
y = x/60,   y=2.66
we can also do the same and use x to change the value of x like this
x = x/60,  then x-2.66, the old value of x is no longer important

## String Operations
a string is a series of characters and spaces inside " or '
'Michael Jackson'
you can call each character in a string with a variable. each character has a number attached to it based on the amount of numbers in the string. ie

M I C H A E L       J A   C  K   S  O   N
0 1 2 3  4 5 6  7   8 9  10  11 12 13 14
Name0: M  Name5: E  Name13:O
Can also be used with negative numbers
M    I    C     H   A    E    L            J  A  C  K   S   O  N
-15 -14 -13 -12 -11 -10 -9 -8    -7 -6 -5 -4 -3 -2 -1
Name-1:N    Name-8:space  Name-15:M
### Slicing
M I C H A E L       J A   C  K   S  O   N
0 1 2 3  4 5 6  7   8 9  10  11 12 13 14
Name[0,4] = Mich  Name[8,12]= Jack
### Stride
M I C H A E L       J A   C  K   S  O   N
0 1 2 3  4 5 6  7   8 9  10  11 12 13 14
Name[::2]Mcaljcsn the 2 indicates that every 2nd variable will be selected
### Stride/Slicing
M I C H A E L       J A   C  K   S  O   N
0 1 2 3  4 5 6  7   8 9  10  11 12 13 14
Name[0:5:2]: Mca  will selected every other variable up to variable 4
the Len command will determine the length of string len('Michael Jackson') which would print 15

can combine strings with the statement function
statement = Name + 'is the best'
statement = 'Michael Jackson is the best'

can mulitply copies of the string with
3 * 'michael jackson'
'michael jackson michael jackson michael jackson'
 
cannot change the value of the original string withe
name0= J   instead you would have to combine the original string with something else and use the strings name like this
name = name + 'is the best' the name becomes 'michael jackson is the best'

\ backslash indicate the start of a new escape sequence 
print('Michael Jackson \n is the best') the \n indicates a new line
Michael Jackson
is the best

\t indicates a tab
print('Michael Jackson \t is the best')
Michael Jackson    Is the best

a double \\ put the backslash in the sting
print('Michael Jackson \\ is the best')
Michael Jackson \ is the best
putting an R before the sequence will input the backslash as well
print(r 'michael jackson \ is the best')
Michael Jackson \ is the best

### Applying Methods to strings
When you apply a method to a string it creates a new string. so if on one line you apply a method and print that and then go back and print the original variable, it will be unchanged and print the orignal one after the first one that was changed. 

A='Thriller is the sixth studio album'
B=A.upper()
B='THRILLER IS THE SIXTH STUDIO ALBUM'

A='Michael Jackson is the best'
B= A.replace('Michael','Janet')
Janet Jackson is the best

Using FInd on a string
name = 'Michael Jackson'
M I C H A E L       J A   C  K   S  O   N
0 1 2 3  4 5 6  7   8 9  10  11 12 13 14
name.find('el'):5 <-- the 5 is the first number of the found sequence
name.find('Jack'):8 <-- the 8 is the first number of the found sequence
Name.find('&*D):-1 <-- if the substring ('&*D) is not in the string the result will be -1

Another way of doing this is to use the 'in" function
```
course = 'Python for Beginners'
print('Python' in course)
```
This will return a boolean answer of True, which in some cases is more desirable than using the index of the searched item.

```
course = "Python Programming"
course_capital = print(course.upper())  # In this case you are calling .upper which will put all characters in the
string in upper case
print(course)  # something to  be aware of is these .methods create a new string so the original string is unaffected
```

course = "Python Programming"
print(course.lower())  # this will put in lowercase
print(course.title())  # this will capitalize the first letter of every word
print(course.strip())  # removes any whitespace before or after the string, useful for input from users who may not
have formatted it properly
print(course.rstrip())  # will remove the whitespace on the right of the string
print(course.lstrip())  # will remove the whitespace on the left of the string
print(course.find("Pro"))  # this will find the index of the argument between the ""'s, if -1 means argue not in the str
print(course.replace("P","j"))  # This will replace all of the first arguement with the 2nd, Ps to js
print("Pro" in course)  # This will look for "Pro" in course, and will return a boolean statement
print("swift" not in course)  # This will return the boolean True, because swift is 'not in' the var course

 if you call a string thru a variable and then put a period after it, you call up specific string methods in this case
 everything in python is an object and all objects have .methods that we can apply to the





## Formatting strings in python
## Escape characters

```

 \"  This will print a double quote in the middle of a string
 \'  this will print a single quote in the middle of a string
 \\  this will print a backslash in the middle of a string
 \n  this will add a new line in the code like this
course1 = ("Python  \nProgramming")
print(course1)

course = "Python \"Programming"  # Used the \ here to espace the " and allow it be used in the middle of the string
print(course)

```


### 'f' formatting strings

```

Name = 'John'
Age = '30'
print(f'my name is {Name} and I am {age} years old')
'my name is John and i am 30 years old'

Name = 'John'
Age = '30'
print('my name is {} and i am {} years old'.format(name,age))
'my name is john and i am 30 years old'

Name = 'John'
Age = '30'
print('my name is %s and i am %d years old' % (name, age))
'my name is john and i am 30 years old'

```

All the above methods work for formatting strings but f string style of formatting is the preferred method.

```
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

```




### Other capabilites of F strings

```
x= 20
y = 30
print(f'the sum of x and y is {x+y}.')
'the sum of x and y is 50'
```

### Regular String 
in a regular string the code interprets the \n as a new line instead of as the \new_folder
regular_string = 'C:\new_folder\file.txt'
print('regular string' regular_string)
regular string:     C:
ew_filefolder.txt

### Raw String 
in a raw string it interprets the \ as a backslash and not an exit operation
raw_string = r"C:\new_folder\file.txt"
print("Raw String:", raw_string)
Raw String: C:\new_folder\file.txt


## RegEx

In Python, RegEx (short for Regular Expression) is a tool for matching and handling strings.

This RegEx module provides several functions for working with regular expressions, including search, split, findall,and sub.

Python provides a built-in module called re, which allows you to work with regular expressions. First, import the remodule



to start RegEx you have to import re 
import  re

import re

s1 = "Michael Jackson is the best"

Define the pattern to search for
pattern = r"Jackson"

Use the search() function to search for the pattern in the string
result = re.search(pattern, s1)

Check if a match was found
if result:
    print("Match found!")
else:
    print("Match not found.")

this will print 'match found'. if there was no Jackson found in the search it would print 'Match not found'.

### special sequences in RegEx

| Special Sequence | Meaning | Example |
| --- | --- | --- |
| \d | Matches any digit character (0-9) | "123" matches "\d\d\d" |
| \D | Matches any non digit character | "hello" matches \D\D\D\D|
| \w | Matches any word character (a -z, A - Z, 0-9, and _) | "hello world matches "\w\w\w\w\w\w\w\w\w\w\w |
| \W | Matches any word non-word character | "@#$%" matches \W\W\W\W |
| \s  | Matches any whitespace character (space, tab, newline, etc.) | "hello world" matches \w\w\w\w\w\s\w\w\w\w\w |
| \S | Matches any non-whitespace character | "hello world" matches \S\S\S\S\S\S\S\S\S |
| \b | Matches the boundary between a word character and a non-word character | "cat" matches \bcat\b in "The cat sat on the mat"|
| \B| Matches any position that is not a word boundary| "cat" matches \Bcat\B in "category" but not in T |

```
pattern = r"\d\d\d\d\d\d\d\d\d\d"  # Matches any ten consecutive digits
text = "My Phone number is 1234567890"
match = re.search(pattern, text)

if match:
    print("Phone number found:", match.group())
else:
    print("No match")
this will print the phone number in the text. if no consecutive 10 digits were found it would print 'No Match'



pattern = r"\W"  # Matches any non-word character
text = "Hello, world!"
matches = re.findall(pattern, text)

print("Matches:", matches)
```

this will find all instances of non word characters, in this case it uses the findall function to check the state Hello, World! for all non word characters. In this case it would list out the , and the !


s2 = "Michael Jackson was a singer and known as the 'King of Pop'"


Use the findall() function to find all occurrences of the "as" in the string
result = re.findall("as", s2)

Print out the list of matched words
print(result)
This will print out a list of the word 'as' so i will give 'as' 'as' you get the 2nd one because the of the as at the end of the word 'was' in the string.



s2= 'Michael Jackson was a singer and known as the 'King of Pop'

Use the split function to split the string by the "\s"
split_array = re.split("\s", s2)

The split_array contains all the substrings, split by whitespace characters
print(split_array)

this will print a list of all the substrings that are seperated by whitespaces i.e. 
'Michael' 'Jackson' 'was' 'a' 'singer' 'and' 'known' 'as' 'the' 'king' 'of' 'pop'

## Tuples and Lists

```
numbers = (1, 2, 3)
numbers[0] = 10
```
tuples are immutable so the above lines of code will output an error, because we cannot change the 0 index of the tuple to 10.

tuples are an ordered sequence
tuples are written as comma-seperated elements within parenteses

Ratings = (10,9,6,5,10,8,9,6,2)

3 different types of tuples in python

string, Integer, and Float

tuple1=('disco',10,1.2)
	type(tuple1)=tuple
	
each element in the tuple is part of an index. can be postiive or negative indexes

tuple1=('disco',10,1.2)
-3 0='disco'    tuple1[0]:'disco  tuple1[-3]:'disco'
-2  1=10            tuple1[1]: 10      tuple1[-2]: 10
-1  2=1.2            tuple1[2]:1.2      tuple1[-1]:1.2

tuples can be combined or concatenated

tuple2=tuple1 + ('hard rock',10)
('disco',10,1.2,'hard rock',10)
   0         1   2         3         4   <-- indexed like this

tuples can be sliced

('disco',10,1.2,'hard rock',10)
    0        1   2          3        4
tuple2[0:3]: ('disco',10,1.2)
                ^ - use the 3 to get the 1.2, if it was  2 it would only slice up to the 10.
if you wanted the last part of the tuple you would use this line of code
tuple2[3:5]: ('hard rock',10)
                ^ - notice we have to use the 5 which is technically longer that the tuple but we need to in 
			order to get the last item in the tuple.
			
Can use the len command to obtain the length of a tuple

len(('disco',10,1.2,'hard rock',10)) the result would be 5 as there are 5 elements

tuples are immutable and cannot be changed, instead you have to create a new tuple

for instance if we wanted to sort the tuple in the previous examples we would need a new tuple

RatingsSorted= sorted(Ratings)

(2,5,6,6,8,9,9,10,10)

tuples can contain other tuples and complex information

NT = (1,2,('pop,'rock'),(3,4),('disco,(1,2)))
           0 1                  2               3        4
NT[2]: ('pop','rock') [1] = ('rock')  <-- if you call the tuple then the index changes so it is only counting 
                0       1                                 touple you called.
then if you called 
NT[2][0]: ('pop')  <-- you get pop, this can then go even deeper by adding more brackets

NT[2][0][0]: ('p')  <-- you would just get the p because it is the 0 index in the new tuple

## Lists
list is also an ordered sequence, a list is denoted with square brackets instead of parentheses, the difference between lists and tuples are lists are mutable
```
names = ['john', 'bob', 'mosh', 'sam', 'mary']
names[0] = "Jon" #This will change John to Jon
print(names)
```
Can use a negative index to get names at the end of the list names[-1] would be mary and so forth.
```
names = ['john', 'bob', 'mosh', 'sam', 'mary']
names[0] = "Jon"  #This will change John to Jon
print(names[0:3])
print(names)  #List doesn't get changed from accessing the index

```
In this code above it will output the names, Jon, Bob, and Mosh. This however does not change the list it simply takes a part of it to use, if you print list again down further in the code, like what is at the bottom in the example above, it will print the original list unmodified. 
```
numbers = [1, 2, 3, 4, 5]
numbers.insert(0, -1)  # This will add a -1 at the beginning of the list
print(numbers)
```
In PyCharm, you can hit Ctrl + P and it will bring up a mini bar about the object method that you are applying and that will give you an idea of what it is looking for.
```
numbers = [1, 2, 3, 4, 5]
print(1 in numbers)
```
this is asking for a boolean function, it will return 'true' because its looking to see if 1 is in the numbers list.
```
numbers = [1, 2, 3, 4, 5]
print(len(numbers))
```
This will print the length(len) of the list, in this case 5

L= ['Michael Jackson', 10.1, 1982]

Lists can contain, strings, floats, integers, other lists and tuples

['Michael Jackson', 10.1, 1982,[1,2],('A',1)]

Each element of the list can be accessed with an index, can be positive or negative

L= ['Michael Jackson', 10.1, 1982]
                     0(-3)       1(-2)   2(-1)
L[0] or L[-3]: 'Michael Jackson'
L[1]  or L[-2]: 10.1
L[2]  or L[-1]: 1982

can also perform slicing on lists
L= ['Michael Jackson', 10.1, 1982,'MJ',1]

L[3:5]:['MJ',1] <-- again the second number (5) needs to be one higher than the end of the list you                                     want

Lists can be combined or concantenated
L= ['Michael Jackson', 10.1, 1982]
L1 = L+['pop',10]
L1 = ['Michael Jackson', 10.1, 1982, 'pop, 10]

lists are mutable so they can be changed with certain functions

L= ['Michael Jackson', 10.1, 1982]
	L.extend(['pop', 10])
	
L = ['Michael Jackson', 10.1, 1982, 'pop', 10]
                    0                    1       2       3      4
so instead of creating a new list, the list is changed and the 2 new elements are added to it

if using append function it combines all the the elements your adding into one i.e.

L= ['Michael Jackson', 10.1, 1982]
	L.append(['pop, 10])
	
L= ['Michael Jackson', 10.1, 1982, ['pop', 10]]
		       0                 1       2              3
		
Can change elements in the list with these functions

A = ['disco', 10, 1.2]
A[0] = 'hard rock'
A = ['hard rock', 10, 1.2]

can delete items with the del command

A = ['disco', 10, 1.2]
del(A[0]): [10, 1.2]

can convert using split

'hard rock'.split()
['hard', 'rock']

can split list using a delimiter

'A, B, C, D'.split(',')<-- delimiter
['A', 'B', 'C', 'D']

Can be Aliased

A = ['hard rock', 10, 1.2]
B = A
then B becomes the same list as A but it is an alias
we know the first element in B[0]  = 'hard rock'. if we change the element in A[0] = 'Banana', then B[0] will also change to 'Banana'

Lists can be cloned with this function

A = ['hard rock', 10, 1.2]
B = A[:]
then B is a clone of A but it is now its own sperate list, so if you change A, B will remain the same

Can get help with any object in python with the help command

A = ['disco', 10, 1.2]

help(A)

# Statements and Loops
## 'If Statement'
```
temperature = 35

if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
```
in this block of code it will output a print to read, "Its a hot day", and "Drink plenty of water". One thing to notice is the 'If' code "Block", this is indicated by the indentation underneath the 'if temperature >30:' line. this means the indented code will only run within the if statement. to get out of that block of code you can hit enter, and then when on the next line you can hit shift+tab, and it will un-indent that line making that code run outside of the if statement. 

## 'Else and Elseif Statements'
```
temperature = 35

if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20: # (20, 30 degrees temp then it will ready "it's a nice day")
    print("Its a nice day")
elif temperature > 10:
    print("It's a bit cold")
else:
    print("It's cold")
print('Done')

```
in this code it the temp is about 30 degrees it will return "It's a hot day", and "Drink plenty of water". Else if(elif) the temp is between 20 and 30 degrees it will return. "It's a nice day"
Else if (elif) the temp is between 10 and 20 degrees it will retrun. "It's a bit cold"
Else if the temp is anything less than 10 it will return. "It's cold". but we don't need to specify <10 because all the other temp ranges are covered. 

## Else, If, and, not logical operators
```
high_income = True
good_credit = True

if high_income and good_credit:  # No need to have high_income == True because that variable is a bool and is already true
    print("Eligible")  # If one of the var's is false then it will output "Not Eligible"
else:
    print("Not Eligible")  # This will output "elgible"

high_income = True
good_credit = False

if high_income or good_credit:  # In this one if either high income or good credit are true then it will output "elgible"
    print("Eligible")
else:
    print("Not Eligible")

high_income = True
good_credit = False
student = True

if not student:  # This will only print "Elgible" is the student var is False
    print("Eligible")
else:
    print("Not Eligible")

high_income = True
good_credit = False
student = False

if (
        high_income or good_credit) and not student:  # need the () around first 2 vars to separate them from the and not student
    print("Eligible")
else:
    print("Not Eligible")
```

## Nested Loops
```
for x in range(5):  # This is the outer loop or the loop that executed first, and is why the pairs of coordinates start with 0
    for y in range(3):  # This is the inner loop and executes after the outer loops which gives us the 2nd "0" in (0,0)
        print(f"({x},{y})")  # This then prints every combination of the above 2 number ranges, (0,0) (0,1) (0,2) (1,0) (1,1) etc etc...
```
## For Else statement
```
successful = False  # This is if the call attempt got thru, then the var successful is true
for number in range(3):
    print("Attempt", (number + 1), (number + 1) * "*")

    if successful:  # This will cause the above loop to break if the attempt was successful
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")  # This will print the message if the for loop ends up being False, if the for
    # loop ends up being True, it will not print
```

##Definition and examples of Iterables
```
print(type(5))  # This will return that "5" is an integer
print(type(range(5)))  # This will return that the range(5) is a range, which is a complex type of data

# This complex data type is iterable, which means it can be iterated over or used in a for loop.
# definition of iterable is something that be looped or used over and over again
for x in range(5):  # This means that x is iterated 5 times and each time it will return a different value.
    print(x)  # note this iteration stops at 4 not 5

for x in "Python":  # Strings are also iterable, this will print x as each character on a new line
    print(x)

for x in [1, 2, 3, 4, "Python"]:  # Lists are also iterable, this will print each number and the word python on new line
    print(x)

for item in shopping_cart:  # shopping_cart is custom object we make, you can make it iterable, so it will print each
    print(item)  # each item that is contained within the custom object shopping_cart
```

## While Loops
```
i = 1
while i <= 1_000: #the underscore here is just to make the number 1000 more readable.
    print(i)
    i = i + 1
```
This code will output the number 1 to 1000.
```
i = 1
while i <= 10:
    print(i * '*')
    i = i + 1
```
This will output a string of *'s up to 10 long because you can multiply a string by a variable in python and it will repeat until the conditions on the variable are met. 
```
number = 100  # This code will keep dividing the number 2 starting at 100, until it reaches 0
while number > 0:
    print(number)
    number //= 2  # same as number = number // 2

command = ""  # this will create an input in the terminal window that will echo back whatever the user types
while command != "quit":  # The loop will stop once the user types quit into the terminal
    command = input(">")
    print("ECHO", command)

command = ""  # The problem with this code is if the user doesn't type quit in lowercase it won't stop iterating
while command != "quit" and command != "QUIT": # This still wouldn't stop if user used a combination of upper and lower case letters
    command = input(">")
    print("ECHO", command)

  # since command is a string we can modify it with .lower and it will covert whatever the user types to lowercase and then will evaluate it against "quit" so it will always stop the loop
command = ""
while command.lower() != "quit":  
    command = input(">")
    print("ECHO", command)
```

## Infinite loop
```
# Infitinte loops will run forever so you need a way to break the loop. Also in infinite loops you don't need to declare
# and define a variable before the loops starts. This will run exactly the same as the loop in while loop example

# command = "", not needed for the loop below to run


while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break
```

## For Loops
```
numbers = [1, 2, 3, 4, 5]
for item in numbers:  # This will print each number on its own line.
    print(item)
```
can also use a while loop to get each number printed on its own line, like this
```
i = 0
while i < len(numbers):  # While i is less than the length of the list numbers then 
    print(numbers[i])  # It will print the list numbers of i
    i = i + 1

```

```
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
```
## Range Function
```
numbers = range(5)
for number in numbers:
    print(number)
```
This will print the numbers 1 to 4 each on a seperate line, because the range is set to 5  and the for loop makes it so each number in the list numbers gets printed as number.
```
numbers = range(5, 10)
for number in numbers:
    print(number)
```
This will output a range of numbers from 5 to 10, but it will exclude the number 10 because its the last number in the range, so it will output the number 5 to 9 each on separate lines.
```
numbers = range(5, 10, 2)
for number in numbers:
    print(number)
```
The 3rd number in the range parenthesis (2), is the step by which the range will count. So this will output the numbers 5,7,9
```
for number in range(5):
    print(number)
```
the range does not have to be stored in a variable so we can also get this to output the number 1 to 4 each on a separate line by writing the code this way.

##Dictionaries
 dictionaries are like an indexed list except you number each element in a dictionary with a key

key 1= 'value', and you assign the value to the key so you can call it later. 

Create the dictionary

Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}
Dict

## Conditional Statements
```
temperature = 15
if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature > 20:
    print("It's nice")
elif temperature < 20:
    print("It's Cold")
print("Done")

```
in this program if the temp is below 20 it will output "It's Cold" if its greater than 20 but not greater than 30 it will read "It's nice", and if its greater than 30 it will read "It's Hot", and "Drink Water". 

# Functions
All functions return 'None' by default, unless you specifically return a value.

## How to name and define a function.
```
def greet():  # naming functions should be done the same way as naming variables.
    print("Hit There")
    print("Welcome Aboard")


# After each function there should be 2 line breaks to separate the function
greet()
```
## Function arguments and how they work
```
def greet(first_name, last_name):  # These are parameters
    print(f"Hi {first_name} {last_name} ")  # The formatted string here calls the parameters from the above line
    print("Welcome Aboard")


greet("Mosh", "Hamedani")  # These are arguments for the above given parameters.
greet("John", "Smith")  # for each new greet() it will run the whole block from above.
```

## Types of functions
```
def greet(name):
    print(f"Hi {name}")  # The greet() and print() functions are type 1 they perform the task of printing something on the terminal


round(1.9)  # this is an example of type 2 it calculates a value and returns it.

# there are 2 types of functions in python
# 1- functions that perform a task
# 2- functions that return a value

```
comparing the 2 different types of functions. 
```
def greet(name):
    print(f"Hi {name}")


#  In this function we are locked to just printing the output to the terminal

def get_greeting(name):
    return f"Hi,{name}"


message = get_greeting("Mosh")
print(message)

# In this function since we are returning the "Mosh" and assigning it to a variable we have a lot more options of the things we can do with it.
```
## Keyword arguments in functions
```
def increment(number, by):
    return number + by


print(increment(2, by=1))  # A more simple way to write the code below, also we are using a keyword argument to make it more clear for anyone reading our code that the 1 is the parameter 'by'

result = increment(2, 1)
print(result)
```
## Default/optional arguments
```
def increment(number, by=1):
    return number + by


print(increment(2))  # This would output 3 because the value of the 2nd argument is defined in the parameters

print(increment(2, 5))  # This will output 7 because the value of by was defined in this statement.

# Generally the arguments of a function are required but this is a way to make them optional and define them later.
# All optional parameters should come after the required ones, otherwise the code won't work i.e.
# def increment(number, by=1, another) this code will not work it must have the by=1 as the last parameter
```

## xargs (or multiple arguments in a function)
```
def multiply(x, y):
    return x * y


 multiply(2, 3, 4, 5)  # this will not work because we have only 2 parameters up top


# to fix this we have to write the code this way

def multiply(*numbers):
    print(numbers)

multiply(2, 3, 4, 5)  # This will generate a tuple with these numbers i.e. (2,3,4,5), and tuples are iterable

def multiply(*numbers):  # This will iterate over the tuple and print each number on a new line
   for number in numbers:
        print(number)


multiply(2, 3, 4, 5)


def multiply(*numbers):  # creates the tuple of (2,3,4,5)
    total = 1  # set the var 'total' to 1
    for number in numbers:  # for each number in numbers we multiply total times it, so 1 * 2 = 2, then 2 * 3 = 6 etc...
        total *= number  # could also be written as total = total * number
    return total  # returns the total but need to make sure its not part of the for loop, so check the indentation.


print(multiply(2, 3, 4, 5))  # prints the solution to multiplying the numbers in tuple. which is 120
```

