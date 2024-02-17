print("\"I am a good boy\"")
# this is a comment lines 


# Escape Sequence in python :-
#1 Escape single quotes in Python
# Let us check an example of escape single quotes in Python, we can see how to use \’ single quote in strings in Python.
string = 'That\'s my bag.'
print(string) 

#2 Python escape sequence n. 
# I have used a “\n” newline character. A newline character is used to write the words in a new separate line.
string = "python\n guides"
print(string)

#3 Let us check an example of a Python escape sequence backslash. 
# The backslash is an escape sequence, \\ is used to print a single backslash.
string = "python\\ guides"
print(string)

#4 Escape sequence for space in Python
# In this example, I have used “\t” character to get space between the words.
string = "python\tguides"
print(string)

#5 Escape sequence backspace in Python
# In this example, I have used “\b” to remove the space between the words in Python.
string = "python \bguides"
print(string)

#6 Escape sequence for Hexa value in Python
# Let us check an example of a Python escape sequence for Hexa value, I have used \xhh to convert hexa value into a string.
string = "\x50\x59\x54\x48\x4f\x4E \x47\x55\x49\x44\x45\x53"
print(string)

#7 Escape sequence for Octal value in Python
# Let us check an example of a Python escape sequence for Octal value, I have used \ooo to convert the Octal value into a normal string.
string = "\120\131\124\110\117\116 \107\125\111\104\105\123"
print(string)

#8 escape sequence for space in Python.
# In this example, I have used \t between the words to get space.
string = "python\tguides"
print(string)

# Raw Strings and Escape Sequences in Python
# In Python, you can create raw strings by prefixing the string with the letter r or R. 
# In raw strings, backslashes are treated as literal characters and not as escape characters in Python.
raw_string = r"This is a raw string\nThis will not be on a new line"
print(raw_string)


# Separator in print statement
print("hi","jit",sep="," ,end="@")
print("how are you")