import numpy as np

# Numpy Basics

## Refer to Quick revision doc for summary

# -----------------------------------------------------------------------

# 1. Creating Arrays

zeros_array = np.zeros((2, 3))     # 2x3 matrix of 0.0
sequence    = np.arange(0, 10, 2)  # [0 2 4 6 8]
linear_space = np.linspace(0, 1, 5) # [0.  0.25 0.5  0.75 1. ]

print(zeros_array)
print(sequence)
print(linear_space)

# -----------------------------------------------------------------------
print("\n")
# -----------------------------------------------------------------------

# 2. Inspecting Your Array

example = np.array([[1, 2, 3], [4, 5, 6]])

print(example.ndim)   # Output: 2       (Number of dimensions/axes)
print(example.shape)  # Output: (2, 3)  (Rows, Columns)
print(example.size)   # Output: 6       (Total number of elements)
print(example.dtype)  # Output: int64   (Data type of elements)

# -----------------------------------------------------------------------
print("\n")
# -----------------------------------------------------------------------

# 3. Indexing and Slicing

arr = np.array([[10, 20, 30], 
                [40, 50, 60], 
                [70, 80, 90]])

# Accessing a single element: array[row, column]
print(arr[1, 2])  # Output: 60 (Row 1, Column 2)

# Slicing: array[row_range, column_range]
print(arr[0:2, 1:3])
# Output:
# [[20 30]
#  [50 60]]

# Extract an entire column (Column index 0)
print(arr[:, 0])  # Output: [10 40 70]

# -----------------------------------------------------------------------
print("\n")
# -----------------------------------------------------------------------

# Slicing a NumPy array creates a view, not a copy.
# If you alter a slice, you will accidentally alter your original data array.
# Use .copy() if you want an isolated duplicate

# -----------------------------------------------------------------------

# 4. Vectorization & Broadcasting

data = np.array([1, 2, 3, 4])

# Fast scalar arithmetic
print(data * 2)  # Output: [2 4 6 8]
print(data + 10) # Output: [11 12 13 14]

# Element-wise math between two arrays
weights = np.array([1, 0, 1, 0])
print(data * weights) # Output: [1 0 3 0]

# -----------------------------------------------------------------------
print("\n")
# -----------------------------------------------------------------------

# 5. Reshaping Arrays

flat_array = np.array([1, 2, 3, 4, 5, 6])

# Reshape into a 2x3 matrix
matrix = flat_array.reshape(2, 3)
print(matrix)
# Output:
# [[1 2 3]
#  [4 5 6]]

# -----------------------------------------------------------------------
print("\n")
# -----------------------------------------------------------------------

# 6. Other basic functions

arr = np.array([1,2,3,4,5,6])

print(np.mean(arr))  # Output: 3.5  (Average)
print(np.median(arr)) # Output: 3.5  (Middle value)
print(np.std(arr))    # Output: 1.70 (Standard deviation / spread)
print(np.max(arr))    # Output: 6    (Highest number)
print(np.min(arr))    # Output: 1    (Lowest number)

# -----------------------------------------------------------------------
print("\n")
# -----------------------------------------------------------------------

# 7. Matrix Operations

# -------------------------------------------------------------
# Setup: Create two sample matrices to work with
# -------------------------------------------------------------
# matrix_A is a 2x3 matrix (2 rows, 3 columns)
matrix_A = np.array([[1, 2, 3], 
                     [4, 5, 6]])

# matrix_B is a 3x2 matrix (3 rows, 2 columns)
matrix_B = np.array([[7, 8], 
                     [9, 10], 
                     [11, 12]])

print("--- Original Matrix A ---")
print(matrix_A)

# -------------------------------------------------------------
# 1. np.sum() - Adds up all numbers
# -------------------------------------------------------------
print("\n--- 1. np.sum() ---")
total_sum = np.sum(matrix_A)
print(f"Sum of all elements in Matrix A: {total_sum}") 
# Explanation: 1 + 2 + 3 + 4 + 5 + 6 = 21

# -------------------------------------------------------------
# 2. np.sqrt() - Calculates square root element-wise
# -------------------------------------------------------------
print("\n--- 2. np.sqrt() ---")
sqrt_matrix = np.sqrt(matrix_A)
print("Square roots of each number in Matrix A:")
print(sqrt_matrix)
# Note: Notice the dots! The outputs are automatically floats.

# -------------------------------------------------------------
# 3. np.transpose() or .T - Flips rows and columns
# -------------------------------------------------------------
print("\n--- 3. Transpose (.T) ---")
# This turns our 2x3 matrix into a 3x2 matrix
transposed_A = matrix_A.T
print("Matrix A flipped (Rows become Columns):")
print(transposed_A)

# -------------------------------------------------------------
# 4. np.dot() - Performs matrix multiplication
# -------------------------------------------------------------
print("\n--- 4. np.dot() ---")
# To multiply matrices, columns of the first must match rows of the second.
# matrix_A (2x3) multiplied by matrix_B (3x2) results in a 2x2 matrix.
dot_product = np.dot(matrix_A, matrix_B)
print("Result of Matrix A multiplied by Matrix B:")
print(dot_product)


# -----------------------------------------------------------------------
print("\n")
# -----------------------------------------------------------------------


# 8. Advanced functions

# -- argmax, argmin
scores = np.array([10, 85, 42, 99, 12])

print(np.argmax(scores)) # Output: 3 (99 is at index 3)
print(np.argmin(scores)) # Output: 0 (10 is at index 0)


# -- np.where
salaries = np.array([3000, 4500, 6000, 2500])

# Syntax: np.where(condition, value_if_true, value_if_false)
taxed_salaries = np.where(salaries > 4000, salaries * 0.8, salaries)
print(taxed_salaries) # Output: [3000. 3600. 4800. 2500.]


# -- vstack, hstack
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Vertical Stack (Rows)
print(np.vstack((a, b)))
# Output:
# [[1 2 3]
#  [4 5 6]]

# Horizontal Stack (Columns)
print(np.hstack((a, b)))
# Output: [1 2 3 4 5 6]


# -- np.unique

responses = np.array(['Yes', 'No', 'Yes', 'Maybe', 'No', 'Yes'])

values, counts = np.unique(responses, return_counts=True)
print(values) # Output: ['Maybe' 'No' 'Yes']
print(counts) # Output: [1 2 3]


# -- np.random

# Generate 5 random floats between 0 and 1
print(np.random.rand(5))

# Generate a 2x3 matrix of random integers between 1 and 100
print(np.random.randint(1, 100, size=(2, 3)))

# Shuffle an array in place
deck = np.array([1, 2, 3, 4, 5])
np.random.shuffle(deck)

## Numpy Basics Completed ##