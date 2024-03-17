A for loop in Python is a powerful tool for iterating over a sequence of items. It allows you to execute a block of code for each item in the sequence. Here's a breakdown of how for loops work:

Basic Structure:

Python
for item in sequence:
    # Code to be executed for each item
Use code with caution.
for: This keyword marks the beginning of the loop.
item: This is a variable name that will hold the current item from the sequence during each iteration of the loop.
sequence: This can be any iterable object, such as a list, tuple, string, or dictionary (with certain conditions for dictionaries). The loop will iterate over each element in the sequence.
:: This colon introduces the code block that will be executed for each item.
Example: Looping through a List

Python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
Use code with caution.
This code will print each fruit from the fruits list on a new line:

apple
banana
cherry
Iterating over a String

Python
message = "Hello, world!"

for char in message:
    print(char, end=" ")  # Print characters with spaces in between
Use code with caution.
This code will print each character of the message string with a space between them:

H e l l o ,   w o r l d !
Using the range() Function

The range() function generates a sequence of numbers within a specified range. You can use it to create a loop that iterates a certain number of times:

Python
for i in range(5):  # Loop iterates 5 times (0 to 4)
    print(i)
Use code with caution.
This code will print the numbers from 0 to 4 (inclusive of 0, exclusive of 5):

0
1
2
3
4
Modifying Items within the Loop

You can modify items within the loop using indexing or other operations:

Python
numbers = [1, 2, 3]

for i in range(len(numbers)):  # Use index to access and modify
    numbers[i] *= 2

print(numbers)  # Output: [2, 4, 6]
Use code with caution.
break and continue Statements:

break: Exits the loop prematurely when a certain condition is met.
continue: Skips the current iteration and moves to the next one.
Example with break:

Python
for num in range(10):
    if num == 5:
        break  # Exit the loop when num is 5
    print(num)
Use code with caution.
This code will print numbers from 0 to 4:

0
1
2
3
4
else Clause:

You can optionally add an else clause that executes after the loop finishes iterating through all items:

Python
for color in ["red", "green", "blue"]:
    print(color)
else:
    print("Loop completed!")
Use code with caution.
This code will print the colors and then "Loop completed!" after all colors have been processed.

In essence, for loops provide a concise and efficient way to iterate over sequences, making them essential for various tasks in Python programming.

.............................................................................................................

Introduction to Loops
Sometimes a programmer wants to execute a group of statements a certain number of times. This can be done using loops. Based on this loops are further classified into following main types;

for loop
while loop
The for Loop
for loops can iterate over a sequence of iterable objects in python. Iterating over a sequence is nothing but iterating over strings, lists, tuples, sets and dictionaries.

Example: iterating over a string:
name = 'Abhishek'
for i in name:
    print(i, end=", ")

Output:
A, b, h, i, s, h, e, k,

Example: iterating over a list:
colors = ["Red", "Green", "Blue", "Yellow"]
for x in colors:
    print(x)

Output:
Red
Green
Blue
Yellow

Similarly, we can use loops for lists, sets and dictionaries.

range():
What if we do not want to iterate over a sequence? What if we want to use for loop for a specific number of times?

Here, we can use the range() function.

Example:
for k in range(5):
    print(k)

Output:
0
1
2
3
4
Here, we can see that the loop starts from 0 by default and increments at each iteration.

But we can also loop over a specific range.

Example:
for k in range(4,9):
    print(k)

Output:
4
5
6
7
8

Quick Quiz
Explore about third parameter of range (ie range(x, y, z))