"""
    This is a list of things I am trying in Python to see if I understand 'numpy'.
    
    It is basically a test suite for what I understand (or misunderstand) about numpy.
    I have nothing but a test suite, since I am not writing numpy itself!
    
    This is just a selective cut-and-paste-and-explain from an interactive python session.
    Mostly it is selected, simplified examples from the scipy web site,
       http://www.scipy.org/Getting_Started
    
#############################################################################
#   Part 1. Creating Arrays
#############################################################################

# The "zeros" function gives an array full of zeros:
>>> a = zeros(10)
>>> a
array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.])

# The "type" of data in an array (integers or approximated real numbers) must be uniform
#  and cannot be changed once the array is created. We can specify the type explicitly
#  by including a "dtype" parameter to the zeros function:
>>> a = zeros(10, dtype=int)
>>> a
array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

# On many, BUT NOT ALL, systems, the default type is "double",
#  BUT since this is not true everywhere, always provide a dtype
#  to avoid having a program that works on some computers but not others!
>>> a = zeros(10, dtype=double)
>>> a
array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.])

# Note that NumPy allows the use of integers,
#  floating-point approximations of real numbers,
#  and complex numbers (with two floating-point values);
# It also allows explicit specification of how many binary digits
#  are to be used for a given type of value, but this is beyond the
#  scope of these examples.

>>> zeros(4, dtype=complex)
array([ 0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j])


#############################################################################
#   Part 2. Working with Array Elements
#############################################################################

# An array can have elements set or retrieved, like a list:
>>> a[5] = 17.5425

>>> a[5]
17.5425

# We can also ask for the size of an array with "len" (as for a list or string), or "size":
>>> len(a)
10
>>> size(a)
10


#############################################################################
#   Part 3. Printing Arrays
#############################################################################

# When we print the array, numpy tries to format it in a uniform way
>>> a
array([  0.    ,   0.    ,   0.    ,   0.    ,   0.    ,  17.5425,
         0.    ,   0.    ,   0.    ,   0.    ])

# Very small or large numbers use scientific notation in Python; NumPy formats for this.
>>> -17.7 / 1000000000000000000
-1.77e-17
>>> a[2] = -17.7 / 1000000000000000000
>>> a[2]
-1.77e-17
>>> a[5]
17.5425
>>> a
array([  0.00000000e+00,   0.00000000e+00,  -1.77000000e-17,
         0.00000000e+00,   0.00000000e+00,   1.75425000e+01,
         0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
         0.00000000e+00])

# The "set_printoptions" can control a variety of aspects of the printing,
#  including the width of the screen (in characters), which is used to
#  control how the array elements are grouped onto lines:

>>> set_printoptions(linewidth=50)
>>> a
array([  0.00000000e+00,   0.00000000e+00,
        -1.77000000e-17,   0.00000000e+00,
         0.00000000e+00,   1.75425000e+01,
         0.00000000e+00,   0.00000000e+00,
         0.00000000e+00,   0.00000000e+00])
         
>>> set_printoptions(linewidth=120)
>>> a
array([  0.00000000e+00,   0.00000000e+00,  -1.77000000e-17,   0.00000000e+00,   0.00000000e+00,   1.75425000e+01,
         0.00000000e+00,   0.00000000e+00,   0.00000000e+00,   0.00000000e+00])

# The "precision" option controls the number of figures printed after the decimal point
>>> set_printoptions(precision=2)
>>> a
array([  0.00e+00,   0.00e+00,  -1.77e-17,   0.00e+00,   0.00e+00,   1.75e+01,   0.00e+00,   0.00e+00,   0.00e+00,
         0.00e+00])
         
>>> set_printoptions(precision=4)
>>> a
array([  0.0000e+00,   0.0000e+00,  -1.7700e-17,   0.0000e+00,   0.0000e+00,   1.7543e+01,   0.0000e+00,   0.0000e+00,
         0.0000e+00,   0.0000e+00])

#############################################################################
#   Part 4. Working with Slices of Arrays
#############################################################################

# We can assign to a range of elements, like so:
>>> a[7:] = 7.01
>>> a[:4] = 3.995
>>> a
array([  3.995 ,   3.995 ,   3.995 ,   3.995 ,   0.    ,  17.5425,   0.    ,   7.01  ,   7.01  ,   7.01  ])

>>> a[2:5] = 23.45   # set elements 2, 3, and 4
>>> a
array([  3.995 ,   3.995 ,  23.45  ,  23.45  ,  23.45  ,  17.5425,   0.    ,   7.01  ,   7.01  ,   7.01  ])

# The subscript ":" means all elements:
>>> a[:] = 123.4
>>> a
array([ 123.4,  123.4,  123.4,  123.4,  123.4,  123.4,  123.4,  123.4,  123.4,  123.4])


#############################################################################
#   Part 5. More options for Creating Arrays
#############################################################################

# The function "ones" is like zeros, but initializes the array to 1:
>>> a = ones(5, dtype=double)
>>> a
array([ 1.,  1.,  1.,  1.,  1.])

# We can even create an "empty" array and then fill it later.
# NOTE that elements we don't bother to set could have any value.
>>> a = empty(8, dtype=double)
>>> a[0:2]=32.1
>>> a[2:5]=555.3
>>> a[5:8]=-0.001
>>> a
array([  3.2100e+01,   3.2100e+01,   5.5530e+02,   5.5530e+02,   5.5530e+02,  -1.0000e-03,  -1.0000e-03,  -1.0000e-03])

# We can build a NumPy array from a Python list with the "array" function
>>> a = array([2.1718, 3.1415, 6.022e23])
>>> a
array([  2.1718e+00,   3.1415e+00,   6.0220e+23])

>>> b = array([3, 4, 5])
>>> b
array([3, 4, 5])

>>> c = array([2.1718, 3, 3,1415, 4, 6.022e23])
>>> c
array([  2.1718e+00,   3.0000e+00,   3.0000e+00,   1.4150e+03,   4.0000e+00,   6.0220e+23])

# We can create another array of the same size and element type with "zeros_like", etc.
>>> z = zeros_like(c)
>>> z
array([ 0.,  0.,  0.,  0.,  0.,  0.])

>>> y = ones_like(b)
>>> y
array([1, 1, 1])

 
#############################################################################
#   Part 6. Multi-Dimensional Arrays
#############################################################################

# For multi-dimensional structures, provide a PYTHON LIST of sizes rather than a single number:
>>> b = zeros([3,5], dtype=double)
>>> b
array([[ 0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.]])
       
# To work with an element, we provide two indices:
>>> b[2,4]
0.0
>>> b[2,4] = 17.6
>>> b
array([[  0. ,   0. ,   0. ,   0. ,   0. ],
       [  0. ,   0. ,   0. ,   0. ,   0. ],
       [  0. ,   0. ,   0. ,   0. ,  17.6]])
>>> b[0,3] = 300.4
>>> b
array([[   0. ,    0. ,    0. ,  300.4,    0. ],
       [   0. ,    0. ,    0. ,    0. ,    0. ],
       [   0. ,    0. ,    0. ,    0. ,   17.6]])

# The "length" of an array is the number of rows; the length of a row is the number of columns.
# The size of an array is the total number of elements;
# The shape is a tuple of the sizes in each dimension
>>> len(b)       # b has three rows
3
>>> len(b[0])    # row 0 of b has five elements, since it's five columns wide:
5
>>> size(b)      # b is 3 by 5, or 15 elements total
15
>>> shape(b)
(3, 5)


# We can read or write an entire row of an array using ":" for the whole range of the column
>>> b[0,:]
array([   0. ,    0. ,    0. ,  300.4,    0. ])
>>> b[0,:] = ones(5, dtype=double)
>>> b
array([[  1. ,   1. ,   1. ,   1. ,   1. ],
       [  0. ,   0. ,   0. ,   0. ,   0. ],
       [  0. ,   0. ,   0. ,   0. ,  17.6]])

# But note that size must be preserved ... we can't put 20 values in a 5-value row (unlike with Python lists):
>>> b[1,:]=ones(20, dtype=double)
Traceback (most recent call last):
...
ValueError: operands could not be broadcast together with shapes (5) (20) 

# We can, however, fill with "as many as necessary":
>>> b[1,:] = 1
>>> b
array([[  1. ,   1. ,   1. ,   1. ,   1. ],
       [  1. ,   1. ,   1. ,   1. ,   1. ],
       [  0. ,   0. ,   0. ,   0. ,  17.6]])

# We can refer to all element in all dimensions with the ":"
>>> b[:,:] = 123.5
>>> b
array([[ 123.5,  123.5,  123.5,  123.5,  123.5],
       [ 123.5,  123.5,  123.5,  123.5,  123.5],
       [ 123.5,  123.5,  123.5,  123.5,  123.5]])

# We can also refer to all elements of one column
#  (This is cool because it can't be done easily with Python lists,
#   or the arrays of many other languages).
>>> b[:,3] = 57.12
>>> b
array([[ 123.5 ,  123.5 ,  123.5 ,   57.12,  123.5 ],
       [ 123.5 ,  123.5 ,  123.5 ,   57.12,  123.5 ],
       [ 123.5 ,  123.5 ,  123.5 ,   57.12,  123.5 ]])
           

#############################################################################
#   Part 7. Idioms for Updating Arrays
#############################################################################

#
# Sometimes we can update the desired elements of an array
#  with one line of Python, i.e., by using the slice operations;
#
# However, other times we may find it hard to express our result in this way,
#  and fall back on the traditional use of "for" loops to identify each
#  desired index in the array, and then update the desired elements one at a time.
# This approach has been used since at least the 1960's,
#  and works in almost all imperative programming languages;
# The update-many-elements approach works in many, but not all, modern languages.
#
# See the example_array_update procedure below for an example;
#  in this example, it adds 1 to everything in the 1st column, 10 to the 2nd column, etc.,
#  except on at the "corners" of the array where it only adds half as much.

>>> example_array_update(b, array([1, 10, 100, 500, 800]))
>>> b
array([[ 124.  ,  133.5 ,  223.5 ,  557.12,  523.5 ],
       [ 124.5 ,  133.5 ,  223.5 ,  557.12,  923.5 ],
       [ 124.  ,  133.5 ,  223.5 ,  557.12,  523.5 ]])

#############################################################################
#   Part 8. Plotting Data Visually
#############################################################################

# Plotting can be done through the matplotlib library;
#  For a tutuoral, see
#    http://matplotlib.sourceforge.net/users/pyplot_tutorial.html#pyplot-tutorial
#  (which is the source of much of my examples).
#
# NOTE that, as of the time I write this, it is NOT working in the Springfield lab!

# >>> from matplotlib.pyplot import *

# >>> plot(b)

# I'm not sure if we need to call "show" to display the plot;
#  after calling "plot", one may be able to set axes, line styles, etc?
# >>> show()


#############################################################################
#   Part 9. Arrays, Lists, References and Copies
#############################################################################

# Values are COPIED into the array, rather than referred to by the array
# (Lists, on the other hand, refer to external objects that are not copied;
#  we drew this with arrows during lectures and labs).
# This use of copies rather than references shows up if we create a "row"
#  of values and install it into a larger array in two places ---
#  The two copies of the row can be modified _independently_.

>>> row = ones(12, dtype=double)
>>> a = zeros([4,12], dtype=double) # 4 rows of 12 each  
>>> a
array([[ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.]])
>>> a[1,:] = row[:]
>>> a[3,:] = row[:]
>>> a
array([[ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
       [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
       [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
       [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.]])
>>> a[1,5] = 0.88
>>> a[3,5] = 0.77
>>> row[5] = 111
>>> row
array([   1.,    1.,    1.,    1.,    1.,  111.,    1.,    1.,    1.,    1.,    1.,    1.])

>>> a
array([[ 0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ],
       [ 1.  ,  1.  ,  1.  ,  1.  ,  1.  ,  0.88,  1.  ,  1.  ,  1.  ,  1.  ,  1.  ,  1.  ],
       [ 0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ],
       [ 1.  ,  1.  ,  1.  ,  1.  ,  1.  ,  0.77,  1.  ,  1.  ,  1.  ,  1.  ,  1.  ,  1.  ]])
         
# Here's the "shared elements" example, EXACTLY as before, but with Python lists:

>>> row = [1] * 12   # a list of 12 ones
>>> a = [[0]*12] * 4  # a list of 4 rows of 12 zeros each
>>> a   # note different printing format from numpy arrays
[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
>>> a[1] = row
>>> a[3] = row   # now a[1] and a[3] are the SAME list, not two copies of it!
>>> a    # except for formatting, it _looks_ like numpy, but...
[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
>>> a[1][5] = 0.88  # Overwrite element 5 of row 1
>>> a[3][5] = 0.77  # Overwrite the SAME spot in "row"
>>> row[5] = 111    # And overwrite the SAME spot another time!
>>> row  # no surprise to see the 111 here, as we did in numpy
[1, 1, 1, 1, 1, 111, 1, 1, 1, 1, 1, 1]
>>> a    # But look!  Where are my 0.88 and 0.77???
[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 111, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 111, 1, 1, 1, 1, 1, 1]]

"""

from numpy import *
# make Python look in the right place for logic.py
import sys
sys.path.append('/home/courses/python')
from logic import precondition

def example_array_update(array_two_d, row_of_things_to_add):
    precondition(    len(shape(array_two_d)) == 2 # two-dimensional array
                 and len(shape(row_of_things_to_add)) == 1  # one-dimensional
                 and shape(array_two_d)[1] == len(row_of_things_to_add)  # same number of columns
                 )

    n_rows = shape(array_two_d)[0]  # number of rows
    n_cols = shape(array_two_d)[1]
    
    for r in range(n_rows):
        for c in range(n_cols):
            if (r == 0 or r == n_rows-1) and (c==0  or c==n_cols-1):  # at a corner
                what_to_add = row_of_things_to_add[c]/2.0
            else:
                what_to_add = row_of_things_to_add[c]
            array_two_d[r, c] = array_two_d[r, c]+what_to_add

# Standard test stuff  from doctest web site:    
def _test():
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print("Wahoo! Passed all", result[1], __file__.split('/')[-1], "tests!")
    else:
        print("Rats!")

if __name__ == "__main__": _test()
