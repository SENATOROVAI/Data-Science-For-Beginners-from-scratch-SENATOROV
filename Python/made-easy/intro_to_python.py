"""Introduction to Python."""

# Python is a Free, Open Source, interpreted, high-level programming language designed for general-purpose use.
# It promotes clear and readable code through high-level data structures, indentation-based grouping, and the absence of explicit variable declarations.
#
# **Python's fundamental principles are encapsulated in The Zen of Python (PEP 20).**
#
# Key principles include:
#
# - Beautiful is better than ugly.
# - Explicit is better than implicit.
# - Simple is better than complex.
# - Complex is better than complicated.
# - Readability counts.
#
# Python does not need to be compiled into binary. Instead, it translates source code into bytecode, which is then interpreted and executed in the computer’s native language.
#
# An interpreter is a program that runs code directly without first converting it into machine language. This allows immediate execution of instructions without requiring compilation.
#
# Python includes a built-in interpreter accessible through the terminal. However, it has limitations, such as the absence of syntax highlighting and tab completion.
#
# **The most popular Python interpreters:**
#
# - IPython: An interactive shell with advanced features, often used alongside Jupyter Notebook for enhanced development.
# - CPython: The standard Python implementation, written in C, known for its broad compatibility but constrained by the Global Interpreter Lock (GIL).
# - IronPython: A Python implementation designed for the .NET framework, enabling integration with .NET libraries.
# - Jython: A Python variant that translates code into Java bytecode, allowing execution on the Java Virtual Machine (JVM).
# - PyPy: A high-performance Python implementation featuring Just-In-Time (JIT) compilation, making it much faster than CPython.
# - PythonNet: Enables seamless interoperability between Python and the .NET Common Language Runtime (CLR), allowing them to function together.
#
# **Stackless Python** is an alternative Python interpreter compatible with Python 3.7. In contrast to CPython, it does not depend on the C call stack, instead clearing it between function calls. As a result it enables efficient microthreading, which minimizes upward expenses of traditional OS threads. It also provides support for coroutines, communication channels, tasklets, and round-robin scheduling.
#
# Python supports both procedure-oriented programming (POP) and object-oriented programming (OOP). POP emphasizes reusable functions, whereas OOP arranges programs around objects that encapsulate both data and behavior. Python’s OOP model is more intuitive and straightforward compared to languages like C++ or Java.
#
# Python ensures seamless integration with C, C++, or Java for performance-critical tasks or proprietary algorithms. This improves execution speed and security while maintaining Python’s simplicity. Additionally, Python is both extensible and embeddable.
#
# * Being extensible means that Python is capable of calling C/C++/Java code.
# * Embeddable feature implies that Python can be integrated into other applications.
#
# **Why Use Anaconda?**
# - Allows installation at the user level without requiring administrative privileges.
# - Manages packages independently from system libraries, ensuring isolation.
# - Provides binary package installation via conda, eliminating the need for compilation like pip.
# - Simplifies dependency management, preventing compatibility issues between packages.
# - Comes with essential tools like NumPy, SciPy, PyQt, Spyder IDE, and supports custom installations via Miniconda.
# - Prevents conflicts with system libraries, ensuring a stable Python environment.
#
# **IPython Qt Console**
# A GUI-based interactive shell for Jupyter kernels, enhancing the terminal experience. It supports syntax highlighting, inline figures, session export, and graphical call tips, making coding more efficient and user-friendly.
#
# **Spyder**
# A free Python IDE included with Anaconda, designed for scientific computing. It provides advanced features such as editing, interactive testing, debugging, and introspection, making it a powerful tool for data analysis and development.
#
# Spyder is specifically tailored for scientists, engineers, and data analysts, combining advanced editing, debugging, and profiling tools with interactive execution, data exploration, and visualization. It integrates seamlessly with scientific libraries like NumPy, SciPy, Pandas, IPython, Matplotlib, and SymPy, making it a comprehensive tool for research and data analysis.
#
# **Jupyter Notebook**
# A web-based interactive computing tool that extends traditional console-based programming. It allows users to develop, document, and execute code, integrating explanatory text, mathematics, and rich media, making it ideal for data science, machine learning, and research.
#
# It is comprised of:
#
# * A web application that allows users to create interactive documents containing code, text, and visual outputs.
# * Notebook documents that store inputs, outputs, explanatory text, and rich media, providing a complete computational record.
#
# Notebook documents (files with the .ipynb extension) store both inputs and outputs from an interactive session, interleaving executable code with explanatory text, mathematics, and rich representations of resulting
# objects. These features make notebook files ideal for research, data science, and machine learning workflows.
#
# Internally, Jupyter notebooks are JSON files, which makes them easy to version-control, share, and collaborate on.
#
# ## 2.12 Answers to the exercises
#
# ### 2.12.1
#
# 1. No, Python is open-source, while freeware is just free to use.
# 2. No. Freeware is free but closed-source; open-source allows modifications.
# 3. Variable types are determined at runtime.
# 4. Python, R, SQL, Julia, Java.
# 5. Easier to read, dynamic typing, automatic memory management.
# 6. Runs on different OS without modification.
# 7. Extensible: Uses C/C++/Java code. Embeddable: Integrated into other apps.
# 8. IDE: Full-featured coding tool. Terminal: Command-line interface.
# 9. Open via jupyter notebook; it supports interactive execution, unlike PDFs or text.
# 10. Markdown cells: Text and formatting. Code cells: Execute Python code.
#
#

#

"""Introduction to Python."""

# Python is a Free, Open Source, interpreted, high-level programming language designed for general-purpose use.
# It promotes clear and readable code through high-level data structures, indentation-based grouping, and the absence of explicit variable declarations.
#
# **Python's fundamental principles are encapsulated in The Zen of Python (PEP 20).**
#
# Key principles include:
#
# - Beautiful is better than ugly.
# - Explicit is better than implicit.
# - Simple is better than complex.
# - Complex is better than complicated.
# - Readability counts.
#
# Python does not need to be compiled into binary. Instead, it translates source code into bytecode, which is then interpreted and executed in the computer’s native language.
#
# An interpreter is a program that runs code directly without first converting it into machine language. This allows immediate execution of instructions without requiring compilation.
#
# Python includes a built-in interpreter accessible through the terminal. However, it has limitations, such as the absence of syntax highlighting and tab completion.
#
# **The most popular Python interpreters:**
#
# - IPython: An interactive shell with advanced features, often used alongside Jupyter Notebook for enhanced development.
# - CPython: The standard Python implementation, written in C, known for its broad compatibility but constrained by the Global Interpreter Lock (GIL).
# - IronPython: A Python implementation designed for the .NET framework, enabling integration with .NET libraries.
# - Jython: A Python variant that translates code into Java bytecode, allowing execution on the Java Virtual Machine (JVM).
# - PyPy: A high-performance Python implementation featuring Just-In-Time (JIT) compilation, making it much faster than CPython.
# - PythonNet: Enables seamless interoperability between Python and the .NET Common Language Runtime (CLR), allowing them to function together.
#
# **Stackless Python** is an alternative Python interpreter compatible with Python 3.7. In contrast to CPython, it does not depend on the C call stack, instead clearing it between function calls. As a result it enables efficient microthreading, which minimizes upward expenses of traditional OS threads. It also provides support for coroutines, communication channels, tasklets, and round-robin scheduling.
#
# Python supports both procedure-oriented programming (POP) and object-oriented programming (OOP). POP emphasizes reusable functions, whereas OOP arranges programs around objects that encapsulate both data and behavior. Python’s OOP model is more intuitive and straightforward compared to languages like C++ or Java.
#
# Python ensures seamless integration with C, C++, or Java for performance-critical tasks or proprietary algorithms. This improves execution speed and security while maintaining Python’s simplicity. Additionally, Python is both extensible and embeddable.
#
# * Being extensible means that Python is capable of calling C/C++/Java code.
# * Embeddable feature implies that Python can be integrated into other applications.
#
# **Why Use Anaconda?**
# - Allows installation at the user level without requiring administrative privileges.
# - Manages packages independently from system libraries, ensuring isolation.
# - Provides binary package installation via conda, eliminating the need for compilation like pip.
# - Simplifies dependency management, preventing compatibility issues between packages.
# - Comes with essential tools like NumPy, SciPy, PyQt, Spyder IDE, and supports custom installations via Miniconda.
# - Prevents conflicts with system libraries, ensuring a stable Python environment.
#
# **IPython Qt Console**
# A GUI-based interactive shell for Jupyter kernels, enhancing the terminal experience. It supports syntax highlighting, inline figures, session export, and graphical call tips, making coding more efficient and user-friendly.
#
# **Spyder**
# A free Python IDE included with Anaconda, designed for scientific computing. It provides advanced features such as editing, interactive testing, debugging, and introspection, making it a powerful tool for data analysis and development.
#
# Spyder is specifically tailored for scientists, engineers, and data analysts, combining advanced editing, debugging, and profiling tools with interactive execution, data exploration, and visualization. It integrates seamlessly with scientific libraries like NumPy, SciPy, Pandas, IPython, Matplotlib, and SymPy, making it a comprehensive tool for research and data analysis.
#
# **Jupyter Notebook**
# A web-based interactive computing tool that extends traditional console-based programming. It allows users to develop, document, and execute code, integrating explanatory text, mathematics, and rich media, making it ideal for data science, machine learning, and research.
#
# It is comprised of:
#
# * A web application that allows users to create interactive documents containing code, text, and visual outputs.
# * Notebook documents that store inputs, outputs, explanatory text, and rich media, providing a complete computational record.
#
# Notebook documents (files with the .ipynb extension) store both inputs and outputs from an interactive session, interleaving executable code with explanatory text, mathematics, and rich representations of resulting
# objects. These features make notebook files ideal for research, data science, and machine learning workflows.
#
# Internally, Jupyter notebooks are JSON files, which makes them easy to version-control, share, and collaborate on.
#
# ## 2.12 Answers to the exercises
#
# ### 2.12.1
#
# 1. No, Python is open-source, while freeware is just free to use.
# 2. No. Freeware is free but closed-source; open-source allows modifications.
# 3. Variable types are determined at runtime.
# 4. Python, R, SQL, Julia, Java.
# 5. Easier to read, dynamic typing, automatic memory management.
# 6. Runs on different OS without modification.
# 7. Extensible: Uses C/C++/Java code. Embeddable: Integrated into other apps.
# 8. IDE: Full-featured coding tool. Terminal: Command-line interface.
# 9. Open via jupyter notebook; it supports interactive execution, unlike PDFs or text.
# 10. Markdown cells: Text and formatting. Code cells: Execute Python code.
#
#

#
