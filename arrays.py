# Welcome to arrays
# Arrays in Python are called Lists and during the script I will called them arrays
# Writing a array
A = ['yellow', 'red', 'blue', 'green', 'black']
B = ['yellow', 'red', 'blue', 'green', 'black']
C = ['']
# We will be using the A array throughout the script
# The is how the output looks like of a simple array
print(A)
# >>>Output: ['yellow', 'red', 'blue', 'green', 'black']

# Displaying values from the string using their index
print('\nThe value on the index of 2 is: ' + A[2])
# >>>Output: The value on the index of 2 is blue

# Slicing the array
print('\nA[1:4] returns= ' + str(A[1:4]))
# = returns ['red', 'blue', 'green']
print('A[2:] returns= ' + str(A[2:]))
# = returns ['blue', 'green', 'black']
print('A[:2] returns= ' + str(A[:2]))
# = returns ['yellow', 'red']
print('A[-1] returns= ' + str(A[-1]))
# = returns 'black'
print('A[1:-1] returns= ' + str(A[1:-1]))
# = returns ['red', 'blue', 'green']

# Using the len() function will display the number of items inside of a array
print('\nThere are ' + str(len(A)) +' items in the A array')

# Sorting; sorted() is the only sort function in Python but it allows you to a lot of things,
# for higher detail visit link:https://docs.python.org/3/howto/sorting.html
# Simple Sort is just sorting the array values from lower to upper
print('\nThis ('+str(A)+') will be sorted like this: ' + str(sorted(A)))

# Reversing the array
B.reverse()
print('\n' + str(A) + ' reverses into ' + str(B))
B.reverse()

# Adding/Appending onto the end of the array
B.append('purple')
print('\nAfter appending the new array looks like this: ' + str(B))

# Inserting values into a list
B.insert(5,'pink')
print('\nOn the 5th index we\'ve added the wanted value, so the array looks like this: ' + str(B))

# Adding an array to a array
B.extend(A)
print('\nWe have added the A array onto the B array at its end: ' + str(B))

# Removing the first found value from a array
print('\n' + str(B))
B.remove('red')
print('The first "red" value was removed from the array:')
print(B)

# Deleting a value by index
del B[7]
print('\nWe will remove the value of the 7th index:\n' + str(B))

# Removing the last value for an array
B.pop()
print('\nUsing pop it will remove the last value from the array:\n' + str(B))

# Counting the occurrences of a value in an array
print('\nWe can check how many times there is "yellow" in the array: ' + str(B.count('yellow')))

# Some use of IF statements
if 'purple' in B:
    print('\nThere is purple in array B\n')

# Some use of FOR loops
for x in B:
    print(x)
