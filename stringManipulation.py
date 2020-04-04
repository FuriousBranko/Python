# The usage of ' ' and " "

var = "String Manipulations is a 'serious' Crime"
print(var)

# The usage of [ ] to access characters in a string

letterT = var[1]

print(letterT)

# Findoing out the lenght of string

lenghtVar = len(var)

# Finding a possision of a letter within a string
print("Finding the possision of s within var:")
print(var.find("s"))

# Counting the acurences of a letter within a string
print("How many times does 'a' show up in var:")

print(var.find("a"))

# Find on which index does a word start within a string
# I don't find this important but:
# print(var.index("is"))

# Slicing a string

print(var[0])           #get one char of the word
print(var[0:1])         #get one char of the word (same as above)
print(var[0:3])         #get the first three char
print(var[:3])          #get the first three char
print(var[-3:])         #get the last three char
print(var[3:])          #get all but the three first char
print(var[:-3])         #get all but the three last character

# Spliting a string

theSplit = var.split(" ")
# >>>Output: ['String','Manipulations'.'is'.'a','"serious"','Crime']

# Boolean statements

var.startswith("S")
# >>>Output: True

var.endswith("e")
# >>>Output: True

var.endswith("g")
# >>>Output: False

var.isalnum()         #check if all char are alphanumeric
var.isalpha()         #check if all char in the string are alphabetic
var.isdigit()         #test if string contains digits
var.istitle()         #test if string contains title words
var.isupper()         #test if string contains upper case
var.islower()         #test if string contains lower case
var.isspace()         #test if string contains spaces

# Repeating a string

print("Tjasi Tjasi tanana "*3)
# >>>Output: Tjasi Tjasi tanana Tjasi Tjasi tanana Tjasi Tjasi tanana

# Replacing words within a string

print(var.replace("Crime","Bad"))


# Formating a string
smallString = "Tjasi Tjasi"
# All to UPPERCASE
print(smallString.upper())
# All to lower
print(smallString.lower())
# Capitalize each word
print(smallString.title())
# Capitalize on the first word
print(smallString.capitalize())
# Switch the Capitalized letters to lower and vise-versa
print(smallString.swapcase())


# Reversing a string
print(' '.join(reversed(smallString)))

# Stripping ( ͡° ͜ʖ ͡°) a string
theStrip = "  tananna     "
print(theStrip)

print(theStrip.strip())

# To strip only the right side of the string
print(theStrip.rstrip())
# To strip only the left side of the string
print(theStrip.lstrip())

# Adding onto a string

print(smallString + theStrip)

# The join function ( adds a definded value after every character)

print(";".join(smallString))
# >>>Output: T;j;a;s;i; ;T;j;a;s;i