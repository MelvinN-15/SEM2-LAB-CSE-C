# ⚡ NumPy Deep Revision Blueprint

A structural, dense reference guide designed for rapid technical review.

---

## 1. Zero Initialization (`np.zeros`)
*   **Feature**: Allocates a contiguous block of memory initialized entirely to `0.0`. Used as placeholders for accumulating values.
*   **Syntax**: `np.zeros(shape, dtype=float)`
*   **Example**:
    ```python
    import numpy as np
    arr = np.zeros((2, 3))
    print(arr)
    ```
*   **Sample Output**:
    ```text
    [[0. 0. 0.]
     [0. 0. 0.]]
    ```

---

## 2. Sequence Generation (`np.arange`)
*   **Feature**: Generates evenly spaced values within a half-open interval `[start, stop)`.
*   **Syntax**: `np.arange([start,] stop, [step,], dtype=None)`
*   **Example**:
    ```python
    import numpy as np
    arr = np.arange(0, 10, 2)
    print(arr)
    ```
*   **Sample Output**:
    ```text
    [0 2 4 6 8]
    ```

---

## 3. Linear Interval Spacing (`np.linspace`)
*   **Feature**: Generates specified number of elements spaced evenly over a closed specified interval `[start, stop]`. Crucial for plotting functions.
*   **Syntax**: `np.linspace(start, stop, num=50, endpoint=True)`
*   **Example**:
    ```python
    import numpy as np
    arr = np.linspace(0, 1, 5)
    print(arr)
    ```
*   **Sample Output**:
    ```text
    [0.   0.25 0.5  0.75 1.  ]
    ```

---

## 4. Dimension & Axis Inspection (`.ndim`)
*   **Feature**: Returns the absolute integer count of dimensions (axes) present within the structural layout.
*   **Syntax**: `array.ndim`
*   **Example**:
    ```python
    import numpy as np
    arr = np.array([[1, 2], [3, 4]])
    print(arr.ndim)
    ```
*   **Sample Output**:
    ```text
    2
    ```

---

## 5. Structural Shape Inspection (`.shape`)
*   **Feature**: Returns a tuple representing the length of the array along each respective axis.
*   **Syntax**: `array.shape`
*   **Example**:
    ```python
    import numpy as np
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    print(arr.shape)
    ```
*   **Sample Output**:
    ```text
    (2, 3)
    ```

---

## 6. Structural Dimension Reshaping (`.reshape`)
*   **Feature**: Reconfigures the dimensional footprint of an array without mutating its internal data content. Element product must match original size.
*   **Syntax**: `array.reshape(new_shape)`
*   **Example**:
    ```python
    import numpy as np
    arr = np.array([1, 2, 3, 4, 5, 6])
    grid = arr.reshape(2, 3)
    print(grid)
    ```
*   **Sample Output**:
    ```text
    [[1 2 3]
     [4 5 6]]
    ```

---

## 7. Multi-Axis Coordinate Slicing (`[r, c]`)
*   **Feature**: Extracts target rows and columns directly via memory views. Changes to sliced views propagate backward and alter the source array.
*   **Syntax**: `array[row_start:row_stop, col_start:col_stop]`
*   **Example**:
    ```python
    import numpy as np
    arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
    slice_view = arr[0:2, 1:3]
    print(slice_view)
    ```
*   **Sample Output**:
    ```text
    [[20 30]
     [50 60]]
    ```

---

## 8. Vectorized Arithmetic (`+`, `-`, `*`, `/`)
*   **Feature**: Evaluates equations instantly across elements using compiled SIMD instructions, avoiding traditional loop performance penalties.
*   **Syntax**: `array <operator> scalar` OR `array1 <operator> array2`
*   **Example**:
    ```python
    import numpy as np
    data = np.array([1, 2, 3])
    print(data * 2)
    ```
*   **Sample Output**:
    ```text
    [2 4 6]
    ```

---

## 9. Global Summation (`np.sum`)
*   **Feature**: Aggregates and returns the calculation total of every element within the structure. Can be scoped to row/col via `axis`.
*   **Syntax**: `np.sum(a, axis=None)`
*   **Example**:
    ```python
    import numpy as np
    arr = np.array([[1, 2], [3, 4]])
    print(np.sum(arr))
    ```
*   **Sample Output**:
    ```text
    10
    ```

---

## 10. Element-wise Square Root (`np.sqrt`)
*   **Feature**: Independently computes the square root of each specific element in place, casting standard integers to floating points.
*   **Syntax**: `np.sqrt(x)`
*   **Example**:
    ```python
    import numpy as np
    arr = np.array([4, 9, 16])
    print(np.sqrt(arr))
    ```
*   **Sample Output**:
    ```text
    [2. 3. 4.]
    ```

---

## 11. Transposition (`.T`)
*   **Feature**: Flips the structural axis matrix layout across its major diagonal, converting rows into columns instantly.
*   **Syntax**: `array.T`
*   **Example**:
    ```python
    import numpy as np
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    print(arr.T)
    ```
*   **Sample Output**:
    ```text
    [[1 4]
     [2 5]
     [3 6]]
    ```

---

## 12. Matrix Dot Product Multiplication (`np.dot`)
*   **Feature**: Computes true mathematical matrix multiplication (inner product of rows and columns). Columns of A must equal rows of B.
*   **Syntax**: `np.dot(a, b)`
*   **Example**:
    ```python
    import numpy as np
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[2, 0], [1, 2]])
    print(np.dot(A, B))
    ```
*   **Sample Output**:
    ```text
    [[ 4  4]
     [10  8]]
    ```

---

## 13. Index Localization (`np.argmax` / `np.argmin`)
*   **Feature**: Parses an entire input matrix array and outputs the literal index position integer containing the highest/lowest values.
*   **Syntax**: `np.argmax(a, axis=None)`
*   **Example**:
    ```python
    import numpy as np
    scores = np.array([10, 85, 42, 99, 12])
    print(np.argmax(scores))
    ```
*   **Sample Output**:
    ```text
    3
    ```

---

## 14. Vectorized Conditional Filtering (`np.where`)
*   **Feature**: Applies structured element-wise logic evaluation over a dataset, swapping elements when matches register True or False.
*   **Syntax**: `np.where(condition, x_if_true, y_if_false)`
*   **Example**:
    ```python
    import numpy as np
    salaries = np.array([3000, 5000, 2500])
    updated = np.where(salaries > 4000, salaries * 0.8, salaries)
    print(updated)
    ```
*   **Sample Output**:
    ```text
    [3000. 4000. 2500.]
    ```

---

## 15. Vertical Matrix Assembly (`np.vstack`)
*   **Feature**: Connects distinct input sequence sequences vertically by safely treating items as stackable incoming rows. Shapes along the second axis must match.
*   **Syntax**: `np.vstack(tup)`
*   **Example**:
    ```python
    import numpy as np
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    print(np.vstack((a, b)))
    ```
*   **Sample Output**:
    ```text
    [[1 2 3]
     [4 5 6]]
    ```

---

## 16. Horizontal Matrix Assembly (`np.hstack`)
*   **Feature**: Glues incoming source input data side-by-side horizontally, extending the total width column profile of the output sequence.
*   **Syntax**: `np.hstack(tup)`
*   **Example**:
    ```python
    import numpy as np
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    print(np.hstack((a, b)))
    ```
*   **Sample Output**:
    ```text
    [1 2 3 4 5 6]
    ```

---

## 17. Deduplication & Sorting (`np.unique`)
*   **Feature**: Sweeps arrays to drop duplicates, return sorted values, and optionally isolate occurrences.
*   **Syntax**: `np.unique(ar, return_counts=False)`
*   **Example**:
    ```python
    import numpy as np
    responses = np.array(['Yes', 'No', 'Yes'])
    vals, counts = np.unique(responses, return_counts=True)
    print(vals, counts)
    ```
*   **Sample Output**:
    ```text
    ['No' 'Yes'] [1 2]
    ```

---

## 18. Continuous Uniform Distribution (`np.random.default_rng().random`)
*   **Feature**: Instantiates modern Generator engines to populate arrays with floats over uniform continuous spreads `[0.0, 1.0)`.
*   **Syntax**: `generator.random(size=None)`
*   **Example**:
    ```python
    import numpy as np
    rng = np.random.default_rng(seed=42) # Set seed for consistency
    print(rng.random(3))
    ```
*   **Sample Output**:
    ```text
    [0.77395605 0.43887844 0.85859792]
    ```

---

## 19. In-Place Random Sequence Shuffling (`generator.shuffle`)
*   **Feature**: Mutates structural records directly across its axis parameters to scramble value layouts. Protects original array shapes.
*   **Syntax**: `generator.shuffle(x)`
*   **Example**:
    ```python
    import numpy as np
    rng = np.random.default_rng(seed=42)
    deck = np.array([1, 2, 3, 4, 5])
    rng.shuffle(deck)
    print(deck)
    ```
*   **Sample Output**:
    ```text
    [4 2 5 1 3]
    ```
