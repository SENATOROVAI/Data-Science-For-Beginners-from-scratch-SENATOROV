"""Algorithm complexity."""

# For small programs, performance is often negligible.
# However, when optimization is needed, Python’s `timeit` and `cProfile` modules help measure execution time
# and identify bottlenecks for improvement.
#
#
# The `timeit` module in Python’s standard library measures the execution speed of small code
# snippets by running them thousands or millions of times and calculating the average runtime.
# It temporarily disables garbage collection for more stable results.
#
#
# ```python
# import timeit
#
# timeit.timeit("a, b = 42, 101; a = a ^ b; b = a ^ b; a = a ^ b")  # 0.1307766629999998
# ```
#
# By default, the code passed to `timeit.timeit()` cannot access variables and functions from the rest of the program.
#
# To fix this, pass `globals()` as the globals argument:
#
#
# ```python
# timeit.timeit("print(spam)", number=1, globals=globals())
# # hello
# # 0.000994909999462834
# ```
#
#
# The `cProfile` module is more effective than `timeit` for analyzing entire functions or programs.
# It systematically measures execution time, memory usage, and function call details, providing a comprehensive performance profile.
#
# To use `cProfile`, pass the function or code to `cProfile.run()`:
#
#
# ```python
# import time, cProfile
#
#
# def addUpNumbers():
#     total = 0
#     for i in range(1, 1000001):
#         total += i
#
#
# cProfile.run("addUpNumbers()")
# ```
#
# When using cProfile, the output contains several key metrics:
#
#  - `ncalls` – Number of times the function was called.
#  - `tottime` – Total execution time of the function, excluding sub-functions.
#  - `percall` – Time per call (tottime divided by ncalls).
#  - `cumtime` – Cumulative time spent in the function, including sub-function calls.
#  - `percall` (cumulative) – cumtime divided by ncalls.
#  - `filename:lineno(function)` – The file and line number where the function is defined.
#
#
# **Big-O notation** is a method for analyzing algorithms that describes how execution
# time scales with input size. It helps evaluate efficiency and predict performance as the input grows.
#
#
# **Big-O notation** categorizes algorithm efficiency by growth rate as input size increases. Ordered from best (least slowdown) to worst (most slowdown):
#
# - `O(1)` – Constant time (fastest, e.g., accessing an array element).
# - `O(log n)` – Logarithmic time (e.g., binary search).
# - `O(n)` – Linear time (e.g., iterating through a list).
# - `O(n log n)` – Quasilinear time (e.g., merge sort, quicksort).
# - `O(n²)` – Quadratic time (e.g., nested loops, bubble sort).
# - `O(2ⁿ)` – Exponential time (e.g., recursive Fibonacci).
# - `O(n!)` – Factorial time (slowest, e.g., brute-force permutations).
# Lower complexities are ideal, while higher ones can become impractical for large inputs.
#
#
# **Examples:**
#
# - `O(1) (Constant Time)`: Checking if a bookshelf is empty – the number of books doesn't affect the time.
# - `O(log n) (Logarithmic Time)`: Binary search – finding a book in an alphabetically sorted shelf by repeatedly halving the search space.
# - `O(n) (Linear Time)`: Reading all books on a shelf – if the number of books doubles, the time required also doubles.
# - `O(n log n) (N-Log-N Time)`: Sorting books alphabetically – each book is placed using binary search (O(log n)),
# and this process repeats for n books, resulting in O(n log n).
# Efficient sorting algorithms like merge sort, quicksort, and Timsort follow this complexity.
# - `O(n²) (Quadratic Time)`: Checking for duplicate books on an unordered shelf – each book is compared
# with every other book, resulting in O(n × n). Doubling the books quadruples the number of operations.
# Common in nested loops and inefficient sorting algorithms like bubble sort.
# - `O(2ⁿ) (Exponential Time)`: Photographing all possible book arrangements on a shelf – each
# book can either be included or not, leading to 2ⁿ combinations.
# Common in brute-force algorithms like subset generation or solving the traveling salesman problem.
# - `O(n!) (Factorial Time)`: Photographing books in every possible order – there are n! (factorial) permutations of n books.
# This complexity grows extremely fast and is common in brute-force algorithms like traveling salesman problem (TSP) and generating all permutations.
#
#
# `Big-O Notation` Analyzes Worst-Case Scenario: It estimates the maximum time an algorithm
# will take as input size grows. This helps evaluate performance bottlenecks and scalability,
# ensuring an algorithm handles the most demanding cases efficiently.
#
# `Ω (Big-Omega)` Notation Describes Best-Case Scenario: It represents the minimum time an algorithm takes.
# For example, an algorithm with Ω(n) runs at least in linear time in the best case.
# While Big-O (O) focuses on the worst-case, Big-Omega (Ω) helps analyze the best possible efficiency.
#
# `Θ (Big-Theta)` Notation Describes Tight Bounds: It applies when an algorithm has the same complexity
# in both best-case (Ω) and worst-case (O) scenarios. For example, Θ(n)
# means the algorithm always runs in linear time. While Big-O is more commonly used,
# Big-Theta provides a more precise performance estimate.
