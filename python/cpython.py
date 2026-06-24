"""Answers to CPython and PyPy interpreter questions for issue #4."""

# ### CPython and PyPy — Issue #4
#
# Answers based on the video *Интерпретатор Cpython и PYPY* and the practical tasks.

# ### Introduction

# ### 1. What is CPython and how does it differ from Python?
#
# Python is a language specification; CPython is its reference implementation, written in C. Python refers to the language/spec, while CPython is the interpreter.

# ### 3. How many Python implementations exist, and which is the most popular?
#
# Six popular are listed here: CPython, PyPy, Jython, IronPython, MicroPython, StacklessPython. CPython is the most popular.

# ### 4. What language is CPython written in?
#
# C (with parts of the standard library written in Python).

# ### 5. (optional).  Who created CPython?
#
# Guido van Rossum

# ### 6. Why Python is considered fast?
#
# Many performance-critical libraries (e.g. NumPy) are implemented in C, which compiles to machine code and allows direct memory control - so the heavy work runs at C speed rather than in the Python interpreter.

# ### 7. Write the path to the CPython interpreter on your computer.
#
# C:\Python\Python313\python.exe

# ### 8. What is contained in the 'include' folder in CPython?
#
# The 'include' folder contains header files that allow programmers to connect C or C++ programs with Python and build Python extensions.

# ### 9. Where can you find CPython source code? (GitHub link)
#
# https://github.com/python/cpython

# ### 10. (optional) How does the CPython interpreter work when executing code?
#
# CPython converts Python code into bytecode and then executes that bytecode using the Python Virtual Machine (PVM).

# ### 11. What command runs a file with CPython?
#
# `python <path>`

# ### 12. Can you run text files through the Python interpreter? Why?
#
# CPython looks at the code inside the file, not just the file extension. As long as the file contains valid Python code, the interpreter can run it. The .py extension is the standard convention, but what really matters is that the contents of the file are written in Python.

# ### 13. How do you specify the path to the interpreter and the file to execute the code?
#
# To run a Python program, you can specify the full path to the CPython interpreter followed by the path to the Python file. For example:
#
# d:\>"C:\Python\Python313\python.exe" D:\test.py

# ### Introduction to PyPy

# ### 14. How does PyPy differ from CPython?
#
# PyPy uses a JIT compiler, while CPython executes Python bytecode through an interpreter.

# ### 15. Why can PyPy not be used for all Python projects?
#
# PyPy can run most Python code, but it's not a drop-in replacement for everything. The big issue is C extensions - PyPy emulates CPython's C API, and a lot of those extensions either break or run slower under it, which kills the point. On top of that, PyPy uses more memory, starts slowly, and its JIT needs time to warm up, so short scripts often see no benefit (or run worse). It also trails CPython on supporting the latest Python versions. So for projects leaning on CPython-specific C extensions or quick one-off scripts, it's just not worth it.

# ### 16. Where can you download PyPy?
#
# https://www.pypy.org/

# ### Installing and running PyPy

# ### 17. How do you install PyPy after downloading?
#
# Extract the downloaded zip file, un-zip, and copy to a desired folder; optionally add it to PATH so `pypy` is callable.

# ### 18. How do you run a file with PyPy?
#
# `pypy <path>`

# ### 19. Why does PyPy execute code faster than CPython?
#
# Its JIT compiler translates frequently executed "hot" code paths to machine code at runtime, avoiding repeated interpretation.

# ### Practical tasks

# ### Task 1: Find and install CPython
#
# C:\>python --version
# Python 3.13.7

# ### Task 2: Explore CPython structure
#
# C:\>where python
# C:\Python\Python313\python.exe
# 265 files, 5 folders

# ### Task 3: Run a file with CPython
#
# Create `example.txt`, run it with `python example.txt`, then rename to `.py` and re-run.
#
# C:\>C:\Python\Python313\python.exe D:\example.txt
# Hello from CPython!
#
# C:\>C:\Python\Python313\python.exe D:\example.py
# Hello from CPython!

# ### Task 4: Install and use PyPy
#
# C:\>C:\Python\pypy3.11\python.exe D:\example_pypy.py
# Hello from pypy!

# ### Task 5: Performance comparison (CPython vs PyPy)

# +
import time

start_time = time.time()
total = 0
for i in range(1, 10000000):
    total += i
end_time = time.time()

print("Result:", total)
print("Execution time:", end_time - start_time, "seconds")
# -

# #### Local execution
#
# CPython
# Result: 49999995000000
# Execution time: 0.36514806747436523 seconds
#
# PyPy
# Result: 49999995000000
# Execution time: 0.01087641716003418 seconds
#
#
# I ran the same performance_test.py file using both CPython and PyPy. CPython executed the program as a regular bytecode interpreter, while PyPy used its JIT compiler. In this type of loop-based calculation, PyPy may run faster because it can optimize repeated operations while the program is running.
#
# Based on the execution times, the interpreter with the smaller time value performed better. In my test, PyPy was faster than CPython.
