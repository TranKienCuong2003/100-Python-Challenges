# 100+ Python challenging programming exercises for Python 3

## 1. Level description
### Level 1	Beginner 
Beginner means someone who has just gone through an introductory Python course. He can solve some problems with 1 or 2 Python classes or functions. Normally, the answers could directly be found in the textbooks.

### Level 2	Intermediate 
Intermediate means someone who has just learned Python, but already has a relatively strong programming background from before. He should be able to solve problems which may involve 3 or 3 Python classes or functions. The answers cannot be directly be found in the textbooks.

### Level 3	Advanced. 
He should use Python to solve more complex problem using more rich libraries functions and data structures and algorithms. He is supposed to solve the problem using several Python standard packages and advanced techniques.

----

## 2. Problem template

Question
Hints
Solution

----

## 3. Questions

### Question 1
Level 1

Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints: 
Consider use range(#begin, #end) method

Solution:
```python
def find_numbers():
    print("Finding numbers divisible by 7 but not a multiple of 5 between 2000 and 3200...")
    result = [str(num) for num in range(2000, 3201) if num % 7 == 0 and num % 5 != 0]
    print("Here are the numbers:")
    print(", ".join(result))

find_numbers()
```

### Question 2
Level 1

Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

Solution:
```python
def compute_factorial():
    num = int(input("Enter a number to compute its factorial: "))
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is: {factorial}")

compute_factorial()
```

### Question 3
Level 1

Question:
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
Consider use dict()

Solution:
```python
def generate_square_dict():
    n = int(input("Enter a number: "))
    square_dict = {i: i * i for i in range(1, n + 1)}
    print(square_dict)

generate_square_dict()
```

### Question 4
Level 1

Question:
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
tuple() method can convert list to tuple

Solution:
```python
def generate_list_and_tuple():
    numbers = input("Enter a sequence of comma-separated numbers: ")
    num_list = numbers.split(",")
    num_tuple = tuple(num_list)
    print(num_list)
    print(num_tuple)

generate_list_and_tuple()
```

### Question 5
Level 1

Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters

Solution:
```python
class StringProcessor:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("Enter a string: ")

    def printString(self):
        print(self.string.upper())

def test_StringProcessor():
    processor = StringProcessor()
    processor.getString()
    processor.printString()

test_StringProcessor()
```

### Question 6
Level 2

Question:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24

Hints:
If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the output received is 26.0, it should be printed as 26)
In case of input data being supplied to the question, it should be assumed to be a console input. 

Solution:
```python
import math

def calculate_Q():
    C = 50
    H = 30
    D = input("Enter comma-separated values for D: ").split(",")
    result = []

    for d in D:
        Q = math.sqrt((2 * C * int(d)) / H)
        result.append(str(round(Q)))

    print(",".join(result))

calculate_Q()
```

### Question 7
Level 2

Question:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

Hints:
Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.

Solution:
```python
def generate_2d_array():
    X, Y = map(int, input("Enter two digits X and Y (comma-separated): ").split(","))
    result = []

    for i in range(X):
        row = []
        for j in range(Y):
            row.append(i * j)
        result.append(row)

    print(result)

generate_2d_array()
```

### Question 8
Level 1

Question:
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

Solution:
```python
def sort_words():
    words = input("Enter a comma-separated sequence of words: ").split(",")
    words.sort()
    print(",".join(words))

sort_words()
```

### Question 9
Level 1

Question:
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

Solution:
```python
def capitalize_lines():
    lines = []
    print("Enter lines (enter an empty line to stop):")
    while True:
        line = input()
        if line == "":
            break
        lines.append(line.upper())
    
    for line in lines:
        print(line)

capitalize_lines()
```

### Question 10
Level 1

Question:
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
We use set container to remove duplicated data automatically and then use sorted() to sort the data.

Solution:
```python
def check_divisibility_by_5():
    binary_numbers = input("Enter a sequence of comma-separated 4-digit binary numbers: ").split(",")
    divisible_by_5 = []

    for binary in binary_numbers:
        decimal = int(binary, 2)
        if decimal % 5 == 0:
            divisible_by_5.append(binary)

    print(",".join(divisible_by_5))

check_divisibility_by_5()
```

### Question 11
Level 2

Question:
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

Solution:
```python
value = []
items=[x for x in input().split(',')]
for p in items:
    intp = int(p, 2)
    if not intp%5:
        value.append(p)

print(','.join(value))
```

### Question 12
Level 2

Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

Solution:
```python
def find_even_digit_numbers():
    even_digit_numbers = []

    for number in range(1000, 3001):
        str_number = str(number)
        if all(int(digit) % 2 == 0 for digit in str_number):
            even_digit_numbers.append(str_number)

    print(",".join(even_digit_numbers))

find_even_digit_numbers()
```

### Question 13
Level 1

Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

Solution:
```python
def count_letters_and_digits():
    sentence = input("Enter a sentence: ")
    letters = 0
    digits = 0

    for char in sentence:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1

    print(f"LETTERS {letters}")
    print(f"DIGITS {digits}")

count_letters_and_digits()
```

### Question 14
Level 1

Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

Solution:
```python
def count_case_letters():
    sentence = input("Enter a sentence: ")
    upper_case = 0
    lower_case = 0

    for char in sentence:
        if char.isupper():
            upper_case += 1
        elif char.islower():
            lower_case += 1

    print(f"UPPER CASE {upper_case}")
    print(f"LOWER CASE {lower_case}")

count_case_letters()
```

### Question 15
Level 1

Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

Solution:

```python
def compute_value():
    a = input("Enter a digit: ")
    result = int(a) + int(a*2) + int(a*3) + int(a*4)
    print(result)

compute_value()
```

### Question 16
Level 1

Question:
Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

Solution:

```python
def square_odd_numbers():
    numbers = input("Enter a sequence of comma-separated numbers: ").split(",")
    odd_numbers = [str(int(num)) for num in numbers if int(num) % 2 != 0]
    print(",".join(odd_numbers))

square_odd_numbers()
```

### Question 17
Level 1

Question:
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

Solution:

```python
def compute_net_amount():
    net_amount = 0
    while True:
        transaction = input("Enter transaction (or press Enter to stop): ")
        if not transaction:
            break
        transaction_type, amount = transaction.split()
        amount = int(amount)

        if transaction_type == 'D':
            net_amount += amount
        elif transaction_type == 'W':
            net_amount -= amount

    print(net_amount)

compute_net_amount()
```

### Question 18
Level 2

Question:
A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

Solutions:

```python
import re

def check_password_validity():
    passwords = input("Enter comma-separated passwords: ").split(",")
    valid_passwords = []

    for password in passwords:
        if (6 <= len(password) <= 12 and
            re.search(r"[a-z]", password) and
            re.search(r"[0-9]", password) and
            re.search(r"[A-Z]", password) and
            re.search(r"[$#@]", password)):
            valid_passwords.append(password)

    print(",".join(valid_passwords))

check_password_validity()
```

### Question 19
Level 2

Question:
You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
We use itemgetter to enable multiple sort keys.

Solutions:
from operator import itemgetter, attrgetter

```python
from operator import itemgetter

def sort_tuples():
    data = input("Enter tuples (name, age, height) separated by commas: ").split(",")
    tuples = [tuple(item.split()) for item in data]
    
    sorted_tuples = sorted(tuples, key=itemgetter(0, 1, 2))
    
    print(sorted_tuples)

sort_tuples()
```

### Question 20
Level 2

Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Hints:
Consider use yield

Solution:

```python
class DivisibleBy7:
    def __init__(self, n):
        self.n = n

    def generate(self):
        for i in range(0, self.n + 1):
            if i % 7 == 0:
                yield i

n = int(input("Enter the value of n: "))
div_by_7 = DivisibleBy7(n)

for number in div_by_7.generate():
    print(number)
```

### Question 21
Level 1

Question
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡­
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

Solution:

```python
import math

def calculate_distance():
    x, y = 0, 0
    
    while True:
        move = input("Enter movement (e.g., UP 5) or type 'end' to stop: ")
        
        if move.lower() == 'end':
            break
        
        direction, steps = move.split()
        steps = int(steps)
        
        if direction == 'UP':
            y += steps
        elif direction == 'DOWN':
            y -= steps
        elif direction == 'LEFT':
            x -= steps
        elif direction == 'RIGHT':
            x += steps
    
    distance = math.sqrt(x**2 + y**2)
    print(round(distance))

calculate_distance()
```

### Question 22
Level 2

Question:
Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1

Hints
In case of input data being supplied to the question, it should be assumed to be a console input.

Solution:

```python
from collections import defaultdict

def word_frequency():
    sentence = input("Enter a sentence: ")
    
    words = sentence.split()
    
    frequency = defaultdict(int)
    
    for word in words:
        frequency[word] += 1
    
    for word in sorted(frequency.keys()):
        print(f"{word}:{frequency[word]}")

word_frequency()
```

### Question 23
level 1

Question:
Write a method which can calculate square value of number

Hints:
Using the ** operator

Solution:

```python
def calculate_square(number):
    return number ** 2

number = int(input("Enter a number: "))
print(f"The square of {number} is: {calculate_square(number)}")

```

### Question 24
Level 1

Question:

Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. But Python has a built-in document function for every built-in functions.

Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()

And add document for your own function
Hints:
The built-in document method is __doc__

Solution:
```python
def custom_function():
    """
    This is a custom function that prints a message.
    It does not take any arguments and simply prints a message when called.
    """
    print("This is a custom function!")

print("Documentation for abs():")
print(abs.__doc__)
print("\nDocumentation for int():")
print(int.__doc__)
print("\nDocumentation for raw_input():")
print(input.__doc__)

print("\nDocumentation for custom_function():")
print(custom_function.__doc__)

```
### Question 25
Level 2

Question:
Define a class, which have a class parameter and have a same instance parameter.

Hints:
Define a instance parameter, need add it in __init__ method
You can init a object with construct parameter or set the value later

Solution:
```python
class MyClass:
    class_param = "This is a class parameter"
    
    def __init__(self, instance_param=None):
        if instance_param:
            self.instance_param = instance_param
        else:
            self.instance_param = "Default instance parameter"

    def display(self):
        print(f"Class parameter: {MyClass.class_param}")
        print(f"Instance parameter: {self.instance_param}")

obj1 = MyClass("Custom instance parameter")
obj1.display()
obj2 = MyClass()
obj2.display()

print(f"Accessing class parameter from the class: {MyClass.class_param}")

```

### Question 26:
Level 1
Define a function which can compute the sum of two numbers.

Hints:
Define a function with two numbers as arguments. You can compute the sum in the function and return the value.

Solution

```python
def sum_of_two_numbers(a, b):
    return a + b

result = sum_of_two_numbers(5, 3)
print("The sum is:", result)

```

### Question 27
Level 1

Define a function that can convert a integer into a string and print it in console.

Hints:

Use str() to convert a number to string.

Solution
```python
def int_to_string(number):
    print(str(number))

int_to_string(123)
```

### Question 28
Level 1

Define a function that can convert a integer into a string and print it in console.

Hints:

Use str() to convert a number to string.

Solution
```python
def int_to_string(number):
    print(str(number))

int_to_string(123)
```

### Question 29
Level 1

Define a function that can receive two integral numbers in string form and compute their sum and then print it in console.

Hints:

Use int() to convert a string to integer.

Solution
```python
def sum_of_strings(num1, num2):
    sum_result = int(num1) + int(num2)
    print(sum_result)

sum_of_strings("10", "20")
```

### Question 30
Lvel 1

Define a function that can accept two strings as input and concatenate them and then print it in console.

Hints:

Use + to concatenate the strings

Solution
```python
def concatenate_strings(str1, str2):
    result = str1 + str2
    print(result)

concatenate_strings("Hello", "World")
```

### Question 31
Level 1

Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print al l strings line by line.

Hints:

Use len() function to get the length of a string

Solution
```python
def print_max_length_string(str1, str2):
    if len(str1) > len(str2):
        print(str1)
    elif len(str1) < len(str2):
        print(str2)
    else:
        print(str1)
        print(str2)

print_max_length_string("Hello", "World!")
```
### Question 32
Level 1

Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".

Hints:

Use % operator to check if a number is even or odd.

Solution
```python
def check_even_odd(number):
    if number % 2 == 0:
        print("It is an even number")
    else:
        print("It is an odd number")

check_even_odd(4)
check_even_odd(7)
```

### Question 33
Level 1

Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.

Hints:

Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.

Solution
```python
def create_square_dict():
    square_dict = {}
    for i in range(1, 21):
        square_dict[i] = i ** 2
    print(square_dict)

create_square_dict()
```


### Question 34
Level 1

Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.

Hints:

Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
Use range() for loops.

Solution
```python
def create_square_dict():
    square_dict = {}
    for i in range(1, 21):
        square_dict[i] = i ** 2
    print(square_dict)

create_square_dict()
```

### Question 35
Level 1

Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the values only.

Hints:

Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
Use range() for loops.
Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.

Solution
```python
def print_square_values():
    square_dict = {}
    for i in range(1, 21):
        square_dict[i] = i ** 2
    
    for value in square_dict.values():
        print(value)

print_square_values()
```

### Question 36
Level 1

Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.

Hints:

Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
Use range() for loops.
Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.

Solution
```python
def print_square_keys():
    square_dict = {}
    for i in range(1, 21):
        square_dict[i] = i ** 2
    
    for key in square_dict.keys():
        print(key)

print_square_keys()

```

### Question 37
Level 1

Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).

Hints:

Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.

Solution
```python
def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print(li)

printList()
```
### Question 38
Level 1

Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.

Hints:

Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
Use [n1:n2] to slice a list

Solution
```python
def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print(li[:5])

printList()
```

### Question 39
Level 2

Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list.

Hints:

Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
Use [n1:n2] to slice a list

Solution
```python
def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print(li[-5:])

printList()
```
### Question 40
Level 1

Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print all values except the first 5 elements in the list.

Hints:

Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
Use [n1:n2] to slice a list

Solution
```python
def printList():
    li = list()
    for i in range(1, 21):
        li.append(i ** 2)
    print(li[5:])

printList()
```

### Question 41
Level 1

Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included). 

Hints:

Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
Use tuple() to get a tuple from a list.

Solution
```python
def printTuple():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print(tuple(li))
		
printTuple()
```
### Question 42
Level 2

With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line. 

Hints:

Use [n1:n2] notation to get a slice from a tuple.

Solution
```python
tp=(1,2,3,4,5,6,7,8,9,10)
tp1=tp[:5]
tp2=tp[5:]
print(tp1)
print(tp2)
```

### Question 43
Level 2

Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10). 

Hints:

Use "for" to iterate the tuple
Use tuple() to generate a tuple from a list.

Solution
```python
def generate_even_tuple():
    original_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    even_numbers = [num for num in original_tuple if num % 2 == 0]
    even_tuple = tuple(even_numbers)
    print(even_tuple)

generate_even_tuple()
```
### Question 44
Level 1

Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No". 

Hints:

Use if statement to judge condition.

Solution
```python
s= raw_input()
if s=="yes" or s=="YES" or s=="Yes":
    print "Yes"
else:
    print "No"
```
### Question 45
Level 2

Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].

Hints:

Use filter() to filter some elements in a list.
Use lambda to define anonymous functions.

Solution
```python
li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = filter(lambda x: x%2==0, li)
print(evenNumbers)
```

### Question 46
Level 2

Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

Hints
Use map() to generate a list.
Use lambda to define anonymous functions.

Solution
```python
li = [1,2,3,4,5,6,7,8,9,10]
squaredNumbers = map(lambda x: x**2, li)
print(squaredNumbers)
```

### Question 47
Level 2

Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

Hints
Use map() to generate a list.
Use filter() to filter elements of a list.
Use lambda to define anonymous functions.

Solution
```python
li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = map(lambda x: x**2, filter(lambda x: x%2==0, li))
print(evenNumbers)
```
### Question 48
Level 2

Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).

Hints:

Use filter() to filter elements of a list.
Use lambda to define anonymous functions.

Solution
```python
evenNumbers = filter(lambda x: x%2==0, range(1,21))
print(evenNumbers)
```

### Question 49
Level 2

Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).

Hints
Use map() to generate a list.
Use lambda to define anonymous functions.

Solution
```python
squaredNumbers = map(lambda x: x**2, range(1,21))
print(squaredNumbers)
```

### Question 50
Level 3

Define a class named American which has a static method called printNationality.

Hints:
Use @staticmethod decorator to define class static method.

Solution
```python
class American(object):
    @staticmethod
    def printNationality():
        print("America")

anAmerican = American()
anAmerican.printNationality()
American.printNationality()
```

### Question 51
Level 3

Define a class named American and its subclass NewYorker. 

Hints:

Use class Subclass(ParentClass) to define a subclass.

Solution:
```python
class American(object):
    pass

class NewYorker(American):
    pass

anAmerican = American()
aNewYorker = NewYorker()
print(anAmerican)
print(aNewYorker)
```

### Question 52
Level 2

Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area. 

Hints:

Use def methodName(self) to define a method.

Solution:
```python
class Circle(object):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2 * 3.14

aCircle = Circle(2)
print(aCircle.area())
```

### Question 53
Level 2

Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area. 

Hints:

Use def methodName(self) to define a method.

Solution:
```python
class Rectangle(object):
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        return self.length * self.width

aRectangle = Rectangle(2, 10)
print(aRectangle.area())
```

### Question 54
Level 3

Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

Hints:

To override a method in super class, we can define a method with the same name in the super class.

Solution:
```python
class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.length = l

    def area(self):
        return self.length * self.length

aSquare = Square(3)
print(aSquare.area())
```

### Question 55
Level 1

Please raise a RuntimeError exception.

Hints:

Use raise() to raise an exception.

Solution:

```python
def raise_runtime_error():
    raise RuntimeError("This is a RuntimeError exception")

try:
    raise_runtime_error()
except RuntimeError as e:
    print(f"Caught an exception: {e}")
```

### Question 56
Level 2

Write a function to compute 5/0 and use try/except to catch the exceptions.

Hints:

Use try/except to catch exceptions.

Solution:
```python
def throws():
    return 5 / 0

try:
    throws()
except ZeroDivisionError:
    print("division by zero!")
except Exception as err:
    print(f'Caught an exception: {err}')
finally:
    print('In finally block for cleanup')
```

### Question 57
Level 3

Define a custom exception class which takes a string message as attribute.

Hints:

To define a custom exception, we need to define a class inherited from Exception.

Solution:
```python
class MyError(Exception):
    """My own exception class

    Attributes:
        msg -- explanation of the error
    """
    
    def __init__(self, msg):
        self.msg = msg

try:
    raise MyError("something wrong")
except MyError as e:
    print(f"Caught MyError: {e.msg}")
```

### Question 58
Level 1

Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.

Example:
If the following email address is given as input to the program:

trankiencuong30072003@gmail.comcom

Then, the output of the program should be:

trankiencuong30072003

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:

Use \w to match letters.

Solution:
```python
import re

email_address = input("Enter an email address: ")
pattern = r"(\w+)@((\w+\.)+(com))"
match = re.match(pattern, email_address)

if match:
    print("Username:", match.group(1))
else:
    print("Invalid email address")
```

### Question 59
Level 2

Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only.

Example:
If the following email address is given as input to the program:

trankiencuong30072003@gmail.com@google.com

Then, the output of the program should be:

gmail

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:

Use \w to match letters.

Solution:
```python
import re

email_address = input("Enter an email address: ")

pattern = r"(\w+)@(\w+)\.(com)"

match = re.match(pattern, email_address)

if match:
    print("Domain:", match.group(2))
else:
    print("Invalid email address")

```

### Question 60
Level 2

Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.

Example:
If the following words is given as input to the program:

2 cats and 3 dogs.

Then, the output of the program should be:

['2', '3']

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:

Use re.findall() to find all substring using regex.

Solution:
```python
import re

s = input("Enter a string: ")

numbers = re.findall(r"\d+", s)

print(numbers)
```

### Question 61
Level 1

Print a unicode string "hello world".

Hints:

Use u'strings' format to define unicode string.

Solution:
```python
unicodeString = "Hello, world! This is a Unicode string."
print("The Unicode string is:")
print(unicodeString)
```

### Question 62
Level 2

Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.

Hints:

Use unicode() function to convert.

Solution:
```python
s = input("Please enter a string: ")
print(f"You entered (as Unicode): {s}")
```

### Question 63
Level 1

Write a special comment to indicate a Python source code file is in Unicode.

Hints:
This comment is typically added at the beginning of the file to specify the character encoding of the source code, ensuring compatibility with Unicode characters.

Solution:
```python
# -*- coding: utf-8 -*-

#----------------------------------------#
# This file is written in UTF-8 encoding, 
# allowing it to handle Unicode characters correctly.
#----------------------------------------#
```

### Question 64
Level 1

Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).

Example:
If the following n is given as input to the program:

5

Then, the output of the program should be:

3.55

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:
Use float() to convert an integer to a float

Solution:
```python
def compute_sum(n):
    total = 0.0
    for i in range(1, n + 1):
        total += i / (i + 1)
    return total

n = int(input("Enter a positive integer (n > 0): "))

if n > 0:
    result = compute_sum(n)
    print(f"The result of the series is: {result:.2f}")
else:
    print("Please enter a value greater than 0.")

```

### Question 65
Level 2

Write a program to compute:

f(n)=f(n-1)+100 when n>0
and f(0)=1

with a given n input by console (n>0).

Example:
If the following n is given as input to the program:

5

Then, the output of the program should be:

500

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:
We can define recursive function in Python.

Solution:
```python
def compute_f(n):
    if n == 0:
        return 1
    else:
        return compute_f(n - 1) + 100

n = int(input("Enter a positive integer (n > 0): "))

if n >= 0:
    result = compute_f(n)
    print(f"The result of f({n}) is: {result}")
else:
    print("Please enter a non-negative value for n.")
```

### Question 66
Level 2

The Fibonacci Sequence is computed based on the following formula:

f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1

Please write a program to compute the value of f(n) with a given n input by console.

Example:
If the following n is given as input to the program:

7

Then, the output of the program should be:

13

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:
We can define recursive function in Python.

Solution:
```python
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter a positive integer (n >= 0): "))

if n >= 0:
    result = fibonacci(n)
    print(f"The Fibonacci number at position {n} is: {result}")
else:
    print("Please enter a non-negative integer.")
```

### Question 67
Level 2

The Fibonacci Sequence is computed based on the following formula:

f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1

Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.

Example:
If the following n is given as input to the program:

7

Then, the output of the program should be:

0,1,1,2,3,5,8,13


Hints:
We can define recursive function in Python.
Use list comprehension to generate a list from an existing list.
Use string.join() to join a list of strings.

In case of input data being supplied to the question, it should be assumed to be a console input.

Solution:
```python
def fibonacci(n):
    # List comprehension to generate Fibonacci sequence up to n
    fib_sequence = [0, 1] + [0]*(n-1)
    [fib_sequence.__setitem__(i, fib_sequence[i-1] + fib_sequence[i-2]) for i in range(2, n+1)]
    return fib_sequence

n = int(input("Enter a positive integer (n >= 0): "))

if n >= 0:
    result = fibonacci(n)
    print(','.join(map(str, result)))
else:
    print("Please enter a non-negative integer.")
```

### Question 68
Level 2

Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.

Example:
If the following n is given as input to the program:

10

Then, the output of the program should be:

0,2,4,6,8,10

Hints:
Use yield to produce the next value in generator.

In case of input data being supplied to the question, it should be assumed to be a console input.

Solution:
```python
def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input("Enter a positive integer (n >= 0): "))

if n >= 0:
    result = even_numbers(n)
    print(','.join(map(str, result)))
else:
    print("Please enter a non-negative integer.")

```

### Question 69
Level 2

Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.

Example:
If the following n is given as input to the program:

100

Then, the output of the program should be:

0,35,70

Hints:
Use yield to produce the next value in generator.

In case of input data being supplied to the question, it should be assumed to be a console input.

Solution:
```python
def divisible_by_5_and_7(n):
    for i in range(0, n + 1):
        if i % 5 == 0 and i % 7 == 0:
            yield i

n = int(input("Enter a positive integer (n >= 0): "))

if n >= 0:
    result = divisible_by_5_and_7(n)
    print(','.join(map(str, result)))
else:
    print("Please enter a non-negative integer.")

```

### Question 70
Level 1

Please write assert statements to verify that every number in the list [2,4,6,8] is even.

Hints:
Use "assert expression" to make assertion.

Solution:
```python
numbers = [2, 4, 6, 8]

for number in numbers:
    assert number % 2 == 0, f"{number} is not an even number"

print("All numbers in the list are even.")
```

### Question 71
Level 1

Please write a program which accepts basic mathematic expression from console and print the evaluation result.

Example:
If the following string is given as input to the program:

30+7

Then, the output of the program should be:

37

Hints:
Use eval() to evaluate an expression.

Solution:
```python
expression = input("Enter a basic mathematical expression: ")

result = eval(expression)
print(result)

```

### Question 72
Level 2

Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.

Hints:
Use if/elif to deal with conditions.

Solution:
```python
def binary_search(sorted_list, target):
    left = 0
    right = len(sorted_list) - 1

    while left <= right:
        mid = (left + right)

        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1

sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7

index = binary_search(sorted_list, target)
if index != -1:
    print(f"Element found at index: {index}")
else:
    print("Element not found")
```

### Question 73
Level 2

Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.

Hints:
Use if/elif to deal with conditions.

Solution:
```python
def binary_search(sorted_list, target):
    left = 0
    right = len(sorted_list) - 1

    while left <= right:
        mid = (left + right)

        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1

sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7

index = binary_search(sorted_list, target)
if index != -1:
    print(f"Element found at index: {index}")
else:
    print("Element not found")
```

### Question 74
Level 1

Please generate a random float where the value is between 10 and 100 using Python math module.

Hints:
Use random.random() to generate a random float in [0,1].

Solution:
```python
import random

random_float = 10 + (random.random() * 90)

print(f"Random float between 10 and 100: {random_float}")
```

### Question 75
Level 1

Please generate a random float where the value is between 5 and 95 using Python math module.

Hints:
Use random.random() to generate a random float in [0,1].

Solution:
```python
import random

random_float = 5 + (random.random() * 90)

print(f"Random float between 5 and 95: {random_float}")

```

### Question 76
Level 1

Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.

Hints:
Use random.choice() to a random element from a list.

Solution:
```python
import random

even_numbers = [0, 2, 4, 6, 8, 10]

random_even = random.choice(even_numbers)

print(f"Random even number between 0 and 10: {random_even}")
```

### Question 77
Level 1

Please write a program to output a random number, which is divisible by 5 and 7, between 0 and 10 inclusive using random module and list comprehension.

Hints:
Use random.choice() to a random element from a list.

Solution:
```python
import random

divisible_by_5_and_7 = [0]

random_number = random.choice(divisible_by_5_and_7)

print(f"Random number divisible by 5 and 7 between 0 and 10: {random_number}")

```

### Question 78
Level 1

Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.

Hints:
Use random.sample() to generate a list of random values.

Solution:
```python
import random

random_numbers = random.sample(range(100, 201), 5)

print(f"Random numbers between 100 and 200: {random_numbers}")

```

### Question 79
Level 2

Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.

Hints:
Use random.sample() to generate a list of random values.

Solution:
```python
import random

even_numbers = random.sample(range(100, 201, 2), 5)

print(f"Random even numbers between 100 and 200: {even_numbers}")

```

### Question 80
Level 3

Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.

Hints:
Use random.sample() to generate a list of random values.

Solution:
```python
import random

divisible_by_35 = range(35, 1001, 35)

random_numbers = random.sample(divisible_by_35, 5)

print(f"Random numbers divisible by 5 and 7 between 1 and 1000: {random_numbers}")

```

### Question 81
Level 1

Please write a program to randomly print a integer number between 7 and 15 inclusive.

Hints:
Use random.randrange() to a random integer in a given range.

Solution:
```python
import random

random_integer = random.randrange(7, 16)

print(f"Random integer between 7 and 15: {random_integer}")
```

### Question 82
Level 2

Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".

Hints:
Use zlib.compress() and zlib.decompress() to compress and decompress a string.

Solution:
```python
import zlib

original_string = "hello world!hello world!hello world!hello world!"

compressed_string = zlib.compress(original_string.encode('utf-8'))
print(f"Compressed String: {compressed_string}")

decompressed_string = zlib.decompress(compressed_string).decode('utf-8')
print(f"Decompressed String: {decompressed_string}")
```

### Question 83
Level 1

Please write a program to print the running time of execution of "1+1" for 100 times.

Hints:
Use timeit() function to measure the running time.

Solution:
```python
import timeit

code_to_measure = "1 + 1"

execution_time = timeit.timeit(code_to_measure, number=100)

print(f"Running time of '1 + 1' for 100 times: {execution_time} seconds")
```

### Question 84
Level 1

Please write a program to shuffle and print the list [3,6,7,8].

Hints:
Use shuffle() function to shuffle a list.

Solution:
```python
import random

my_list = [3, 6, 7, 8]

random.shuffle(my_list)

print(my_list)
```

### Question 85
Level 1
Please write a program to shuffle and print the list [3,6,7,8].

Hints:
Use shuffle() function to shuffle a list.

Solution:
```python
import random

my_list = [3, 6, 7, 8]

random.shuffle(my_list)

print(my_list)
```

### Question 86
Level 2

Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

Hints:
Use list[index] notation to get a element from a list.

Solution:
```python
subjects = ["I", "You"]
verbs = ["Play", "Love"]
objects = ["Hockey", "Football"]

for subject in subjects:
    for verb in verbs:
        for obj in objects:
            print(f"{subject} {verb} {obj}")
```

### Question 87
Level 1

Please write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].

Hints:
Use list comprehension to delete a bunch of element from a list.

Solution:
```python
numbers = [5, 6, 77, 45, 22, 12, 24]

odd_numbers = [num for num in numbers if num % 2 != 0]

print(odd_numbers)
```

### Question 88
Level 2

By using list comprehension, please write a program to print the list after removing delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

Hints:
Use list comprehension to delete a bunch of element from a list.

Solution:
```python
numbers = [12, 24, 35, 70, 88, 120, 155]

filtered_numbers = [num for num in numbers if num % 5 != 0 or num % 7 != 0]

print(filtered_numbers)
```

### Question 89
Level 2

By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].

Hints:
Use list comprehension to delete a bunch of element from a list.
Use enumerate() to get (index, value) tuple.

Solution:
```python
numbers = [12, 24, 35, 70, 88, 120, 155]

filtered_numbers = [num for index, num in enumerate(numbers) if index % 2 != 0]

print(filtered_numbers)
```

### Question 90
Level 2

By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.

Hints:
Use list comprehension to make an array.

Solution:
```python
array_3d = [[[0 for _ in range(8)] for _ in range(5)] for _ in range(3)]

print(array_3d)

```

### Question 91
Level 2

By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].

Hints:
Use list comprehension to delete a bunch of element from a list.
Use enumerate() to get (index, value) tuple.

Solution:
```python
numbers = [12, 24, 35, 70, 88, 120, 155]

result = [num for index, num in enumerate(numbers) if index not in [0, 4, 5]]

print(result)
```

### Question 92
Level 1

By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].

Hints:
Use list's remove method to delete a value.

Solution:
```python
numbers = [12, 24, 35, 24, 88, 120, 155]

result = [num for num in numbers if num != 24]

print(result)
```

### Question 93
Level 2

With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists.

Hints:
Use set() and "&=" to do set intersection operation.

Solution:
```python
list1 = [1, 3, 6, 78, 35, 55]
list2 = [12, 24, 35, 24, 88, 120, 155]

intersection = list(set(list1) & set(list2))

print(intersection)
```

### Question 94
Level 1

With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.

Hints:
Use set() to store a number of values without duplicate.

Solution:
```python
input_list = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]

seen = set()

result = [x for x in input_list if not (x in seen or seen.add(x))]

print(result)
```

### Question 95
Level 2

Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

Hints:
Use Subclass(Parentclass) to define a child class.

Solution:
```python
class Person:
    def getGender(self):
        pass

class Male(Person):
    def getGender(self):
        print("Male")

class Female(Person):
    def getGender(self):
        print("Female")

male = Male()
male.getGender()

female = Female()
female.getGender()
```

### Question 96
Level 1

Please write a program which count and print the numbers of each character in a string input by console.

Example:
If the following string is given as input to the program:

abcdefgabc

Then, the output of the program should be:

a,2
c,2
b,2
e,1
d,1
g,1
f,1

Hints:
Use dict to store key/value pairs.
Use dict.get() method to lookup a key with default value.

Solution:
```python
def count_characters(input_string):
    char_count = {}

    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1

    for char, count in char_count.items():
        print(f"{char},{count}")

input_string = input("Enter a string: ")

count_characters(input_string)
```

### Question 97
Level 1

Please write a program which accepts a string from console and print it in reverse order.

Example:
If the following string is given as input to the program:

rise to vote sir

Then, the output of the program should be:

ris etov ot esir

Hints:
Use list[::-1] to iterate a list in a reverse order.

Solution:
```python
def reverse_string(input_string):
    reversed_string = input_string[::-1]

    print(reversed_string)

input_string = input("Enter a string: ")

reverse_string(input_string)
```

### Question 98
Level 1

Please write a program which accepts a string from console and print the characters that have even indexes.

Example:
If the following string is given as input to the program:

H1e2l3l4o5w6o7r8l9d

Then, the output of the program should be:

Helloworld

Hints:
Use list[::2] to iterate a list by step 2.

Solution:
```python
def print_even_index_characters(input_string):

    even_index_chars = input_string[::2]
    
    print(even_index_chars)

input_string = input("Enter a string: ")

print_even_index_characters(input_string)
```

### Question 99
Level 1

Please write a program which prints all permutations of [1,2,3]

Hints:
Use itertools.permutations() to get permutations of list.

Solution:
```python
import itertools

def print_permutations(input_list):
    permutations = itertools.permutations(input_list)
    
    for perm in permutations:
        print(perm)

input_list = [1, 2, 3]

print_permutations(input_list)
```

### Question 100
Level 2

Write a program to solve a classic ancient Chinese puzzle: 
We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?

Hint:
Use for loop to iterate all possible solutions.

Solution:
```python
def solve_puzzle():
    for chickens in range(36):
        rabbits = 35 - chickens
        if 2 * chickens + 4 * rabbits == 94:
            return chickens, rabbits

chickens, rabbits = solve_puzzle()
print(f"There are {chickens} chickens and {rabbits} rabbits.")
```
## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
