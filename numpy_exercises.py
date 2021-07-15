import numpy as np

#Use the following code for the questions below:
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

#How many negative numbers are there?
neg_nums = a[a < 0]
print('\n1)')
print(f'There are {len(neg_nums)} negative numbers.')

#How many positive numbers are there?
pos_nums = a[a > 0]
print('\n2)')
print(f'There are {len(pos_nums)} positive numbers.')

#How many even positive numbers are there?
even_nums = a[ (a % 2 == 0) ]
even_pos_nums = even_nums[even_nums > 0]
print('\n3)')
print(f'There are {len(even_pos_nums)} even positive numbers.')

#If you were to add 3 to each data point, how many positive numbers would there be?
a_plus_three = a + 3
a_plus_three_pos_nums = a_plus_three[a_plus_three > 0]
print('\n4)')
print(f'After adding 3 to each data point, there are {len(a_plus_three_pos_nums)} positive numbers.')

#If you squared each number, what would the new mean and standard deviation be?
a_squared = a ** 2
squared_mean = a_squared.mean()
squared_stddev = a_squared.std()
print('\n5)')
print(f'After squaring each number the new mean is {squared_mean} and the new std is {squared_stddev:.2f}.')

#A common statistical operation on a dataset is centering. 
#This means to adjust the data such that the mean of the data is 0. This is done by subtracting the mean from each data point. 
#Center the data set. See this link for more on centering.
#I will assume this should be done to the original dataset, not the squared dataset
mean = a.mean()
centered_set = a - mean
print('\n6)')
print(f'The centered data set is:')
print(centered_set)

#Calculate the z-score for each data point.
z_scores = (a - mean) / a.std()
print('\n7)')
print(f'The z-scores for each data point are:')
print(z_scores)

#Copy the setup and exercise directions from More Numpy Practice into your numpy_exercises.py and add your solutions.

print('\nMore Numpy Practice')
## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Set up 1: using list "a"')

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a = sum(a)
print('\n1)')
print(f'The sum of all the numbers in the list is {sum_of_a}.')

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a = min(a)
print('\n2)')
print(f'The min of all the numbers in the list is {min_of_a}.')

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = max(a)
print('\n3)')
print(f'The max of all the numbers in the list is {max_of_a}.')

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a = sum_of_a / len(a)
print('\n4)')
print(f'The mean of a is {mean_of_a}.')

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
product_of_a = 1
for num in a:
    product_of_a *= num
print('\n5)')
print(f'The product of all the numbers in a is {product_of_a}.')

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_of_a = [num * num for num in a]
print('\n6)')
print('The list containing the squares of a is:')
print(squares_of_a)

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a = [num for num in a if num % 2 == 1]
print('\n7)')
print('The list containing all the odd numbers of a is:')
print(odds_in_a)

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a = [num for num in a if num % 2 == 0]
print('\n8)')
print('The list containing all the even numbers of a is:')
print(evens_in_a)

## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = np.array([
    [3, 4, 5],
    [6, 7, 8]
])

print('Setup 2: using list "b":')

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = b.sum()
print('\n1)')
print(f'The sum of b is {sum_of_b}.')

# Exercise 2 - refactor the following to use numpy. 
min_of_b = b.min()
print('\n2)')
print(f'The min of b is {min_of_b}.')

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = b.max()
print('\n3)')
print(f'The max of b is {max_of_b}.')

# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = b.mean()
print('\n4)')
print(f'The mean of b is {mean_of_b}.')

# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = b.prod()
print('\n5)')
print(f'The product of all the numbers in b is {product_of_b}.')

# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = b ** 2
print('\n6)')
print('The list of squares of b is:')
print(squares_of_b)

# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = b[b%2 == 1]
print('\n7)')
print('The list of odds in b is:')
print(odds_in_b)

# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = b[b%2 == 0]
print('\n8)')
print('The list of evens in b is:')
print(evens_in_b)

# Exercise 9 - print out the shape of the array b.
print('\n9)')
print('The shape of array b is:')
print(b.shape)

# Exercise 10 - transpose the array b.
print('\n10)')
print('The transposed version of array b is:')
print(b.transpose())

# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
b = b.reshape(1,6)
print('\n11)')
print('The reshaped version of array b is:')
print(b)

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
b = b.reshape(6, 1)
print('\n12)')
print('The reshaped version of array b is:')
print(b)

## Setup 3
c = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print('\nSetup 3: using array c')

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.
c_min = c.min()
c_max = c.max()
c_sum = c.sum()
c_prod = c.prod()
print('\n1)')
print(f'Min of c: {c_min}.')
print(f'Max of c: {c_max}.')
print(f'Sum of c: {c_sum}.')
print(f'Product of c: {c_prod}.')

# Exercise 2 - Determine the standard deviation of c.
c_stddev = c.std()
print('\n2)')
print(f'The stddev of c is: {c_stddev:.2f}.')

# Exercise 3 - Determine the variance of c.
c_variance = c.var()
print('\n3)')
print(f'The variance of c is: {c_variance:.2f}.')

# Exercise 4 - Print out the shape of the array c
print('\n4)')
print('The shape of array c is:')
print(c.shape)

# Exercise 5 - Transpose c and print out transposed result.
c_transposed = c.transpose()
print('\n5)')
print('The transposed version of c is:')
print(c_transposed)

# Exercise 6 - Get the dot product of the array c with c. 
c_dot = c.dot(c)
print('\n6)')
print('The dot product of c is:')
print(c_dot)

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
c_times_c_transposed = c * c_transposed
sum_of_c_times_c_transposed = c_times_c_transposed.sum()
print('\n7)')
print(f'The sum of array c times array c transposed is: {sum_of_c_times_c_transposed}.')

# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
prod_of_c_times_c_transposed = c_times_c_transposed.prod()
print('\n8)')
print(f'The product of array c times array c transposed is: {prod_of_c_times_c_transposed}.')

## Setup 4
d = np.array([
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
])

print('\nSetup 4: using array d')

# Exercise 1 - Find the sine of all the numbers in d
d_sin = np.sin(d)
print('\n1)')
print('The sin of all the numbers in array d is:')
print(d_sin)

# Exercise 2 - Find the cosine of all the numbers in d
d_cos = np.cos(d)
print('\n2)')
print('The cosine of all the numbers in array d is:')
print(d_cos)

# Exercise 3 - Find the tangent of all the numbers in d
d_tan = np.tan(d)
print('\n3)')
print('The tangent of all the numbers in array d is:')
print(d_tan)

# Exercise 4 - Find all the negative numbers in d
d_neg = d[d<0]
print('\n4)')
print('All the negative numbers in d are:')
print(d_neg)

# Exercise 5 - Find all the positive numbers in d
d_pos = d[d>0]
print('\n5)')
print('All the positive numbers in d are:')
print(d_pos)

# Exercise 6 - Return an array of only the unique numbers in d.
d_unique = np.unique(d)
print('\n6)')
print('The unique values of d are:')
print(d_unique)

# Exercise 7 - Determine how many unique numbers there are in d.
d_num_unique = len(d_unique)
print('\n7)')
print(f'The number of unique values in d is: {d_num_unique}.')

# Exercise 8 - Print out the shape of d.
print('\n8)')
print('The shape of array d is:')
print(d.shape)

# Exercise 9 - Transpose and then print out the shape of d.
d_transposed = d.transpose()
print('\n9)')
print('The shape of array d transposed is:')
print(d_transposed.shape)

# Exercise 10 - Reshape d into an array of 9 x 2
d_reshaped = d.reshape(9, 2)
print('\n10)')
print('Array d after being reshaped into a 9 x 2 is:')
print(d_reshaped)

