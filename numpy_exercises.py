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
