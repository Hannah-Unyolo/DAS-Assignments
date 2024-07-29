# HEAP DATA STRUCTURE

A heap is a tree-like data structure where each parent node is either greater than or equal to or less than or equal to its child node.

## ADVANTAGES

1. Helps in finding the maximum and minimum elements
2. No limit on memory size
3. Allows access to variables globally

# DISADVANTAGES

1. Lack of flexibility
2. Not ideal for searching
3. Memory management
4. Complexity
  
## PROPERTIES

1. Shape Property
2. Complete binary tree

## APPLICATION OF HEAPS

1. Priority Queues: Heaps are often utilized as a means of implementing priority queues. This allows for elements with higher priority to be extracted first, ensuring that the most important tasks are handled promptly.

2. Heapsort algorithm: It is used to handle large datasets without slowing down

3. Graph Algorithms: Heaps allow algorithms to efficiently track and prioritize nodes or vertices based on their distance or weight from the starting point, hence increasing the speed at finding paths or trees




# WHAT IS A TUPLE?
A tuple is an immutable, ordered collection of elements in programming.
It is commonly used in languages like Python, Java, and others.


# CHARACTERISTICS OF TUPLES
1. Immutability: Once created, the elements of a tuple cannot be changed, added, or removed.
2. Ordered: The elements have a defined order, which means that the position of each element is fixed.
3. Heterogeneous: Tuples can contain elements of different data types (e.g., integers, strings, lists).
4. Hashable: Since they are immutable, tuples can be used as keys in dictionaries.

# CREATING TUPLES
Syntax: In Python, tuples are created by placing elements within parentheses, separated by commas.
# Example
my_tuple = (1, 'hello', 3.14)

Single Element Tuple: To create a tuple with a single element, a trailing comma is required.
# Example
single_element_tuple = (42,)

# Accessing Tuple Elements
Elements can be accessed using indexing, similar to lists.
# Example
first_element = my_tuple[0]  # Output: 1

# Common Operations
Concatenation: Tuples can be concatenated using the + operator.
# Example
new_tuple = my_tuple + (4, 5)

Repetition: Use the * operator to repeat tuples.
# Example
repeated_tuple = my_tuple * 2

Slicing: You can slice tuples to obtain a subset.
# Example
sliced_tuple = my_tuple[1:3]  # Output: ('hello', 3.14)

# USE CASES
1. Data Integrity: Use tuples to ensure that the data remains unchanged.

2. Function Returns: Tuples are often used to return multiple values from functions.

3. Data Structures: Useful in creating complex data structures like records or points in space.

# ADVANTAGES OF TUPLES
1. Performance: Tuples can be more memory-efficient than lists due to their immutability.
2. Safety: Protects data from accidental modification.

# LIMITATIONS OF TUPLES
1. Immutability: Cannot modify elements after creation, which can be a drawback in some scenarios.
2. Less Flexible: Limited functionality compared to lists (e.g., no methods like append() or remove()).

