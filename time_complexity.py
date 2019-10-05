# What is time complexity ?

"""Time complexity: is basically how efficient an algorithm is or how long
does it take for a function to run given it's input"""

"""Time complexity: can also be defined as the quantification of the amount
 of time taken by a set of code or algorithm to process or run as the function
 of the given input"""

# Time complexity is address mathematically using th Big(o) notation

# Some of the main Big(O) classification

# O(c) => Constant Time
"""Constant time definition: the algorithm in question
execute the same number of operations regardless of the size of the input
so for any input size n, a constant time algorithm performs the same
number of operations every time
example:
    looping through hashtable
    index based array
"""


# O(logn) => Logarithmic Time

"""
Logarithmic Time definition: the algorithm inquestion increases the number
of operation it performs as a logarithmic function of the input size n.
The function log n grows very slowly, so as n get larger, the number of
operation the algorithm needs to perform does not increase by very much
example:
    looping through a dictionary
    binary search
"""

# O(n) => Linear Time
"""
Linear Time definition: the algorithm in question increases the number
of operations it performs as a linear function of the input size n
The number of additional operations the algorithm needs to perform
grows in direct proportion to the increase in input size n

"""


# O(nlogn) => Long Linear Time
"""
Long linear time definition: the algorithm in question
increases the number of operations it performs as a log-linear
function of the input size

intuitively you can think of this runtime classification as
looping over every single element and doing some additional
work on each of them
Note: this is more common on sorting algorithm
example:
    quicksort
    mergesort
    heapsort
    timsort
"""

# O(n power c) => Quadratic time
"""
Quadratic time definition: the algorithm in question increases
the number of operations it performs as a quadratic function
of the input size n
    example:
        n = 10 => n square = 100
        n = 100 => n square = 1000000
"""


# O(c power n) => Exponential time
