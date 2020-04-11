# Welcome to arrays
# Arrays in Python are called Lists and during the script I will called them arrays
# Writing a array
A = ['yellow', 'red', 'blue', 'green', 'black']
# We will be using the A array throughout the script
# The is how the output looks like of a simple array
print(A)
# >>>Output: ['yellow', 'red', 'blue', 'green', 'black']

# Displaying values from the string using their index
print('The value on the index of 2 is: '+ A[2])
# >>>Output: The value on the index of 2 is blue

# Slicing the array
print('A[1:4] returns= '+ str(A[1:4]))
# = returns ['red', 'blue', 'green']
print('A[2:] returns= '+ str(A[2:]))
#= returns ['blue', 'green', 'black']
print('A[:2] returns= '+ str(A[:2]))
#= returns ['yellow', 'red']
print('A[-1] returns= '+ str(A[-1]))
#= returns 'black'
print('A[1:-1] returns= '+ str(A[1:-1]))
#= returns ['red', 'blue', 'green']

# Using the len() function will display the number of items inside of a array
print('There are '+ str(len(A)) +' items in the A array')

# Sorting; sorted() is the only sort function in Python but it allows you to a lot of things,
# for higher detail visit link:https://docs.python.org/3/howto/sorting.html
# Simple Sort is just sorting the array values from lower to upper
print('This ('+str(A)+') will be sorted like this: '+ str(sorted(A)))