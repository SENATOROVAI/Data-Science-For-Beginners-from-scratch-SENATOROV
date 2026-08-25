"""Introduction to Data Science and Programming basics."""

# Data science facilitates decision-making, pattern recognition, predictive analytics, and data visualization. It enables us to:
#
# - Uncover critical questions and determine the primary causes of problems.
# - Detect patterns within raw data.
# - Prepare models for predictive analysis.
# - Present findings effectively through graphs, dashboards and etc.
# - Ensure for machines the ability to be capable in sense of intelligence.
# - Assess customer sentiment and refine recommendations.
# - Accelerate business development by enabling faster and more informed decisions.
#
# **Components of Data Science**
# - Data Mining.
# - Data Analytics.
# - Data Engineering.
# - Visualization.
# - Statistical Analysis.
# - Artificial Intelligence targets the creation of machines that imitate human actions. It dates back to Alan Turing's early work in 1936 but so far cannot substitute a human totally.
# - Machine Learning extracts knowledge from data, by the following means: training with a teacher or training without a teacher.
# - Deep Learning uses multi-layer neural networks to cope with complex tasks where traditional Machine Learning is useless.
# - Big Data involves dealing with vast amounts of often unstructured data, requiring tools and systems designed to handle heavy workloads efficiently.
#
# **A data scientist extracts key findings from business data by taking these actions:**
#
# - Ask appropriate questions to understand the problem.
# - Garner data from multiple sources (enterprise, public, etc.).
# - Process raw data and turn it into manageable format.
# - Use Machine Learning algorithms or statistical models for insights.
# - Submit to stakeholders key findings for management needs.
#
#
# **Key skills for success in Data Science:**
#
# - Programming: Proficiency in Python or R is essential, where Python is deemed the preferred choice due to its simplicity and extensive libraries.
# - Statistics: A solid grasp of statistical concepts is crucial for deriving meaningful insights from data.
# - Databases: Expertise in managing and retrieving data from databases is fundamental.
# - Modeling: Mathematical models facilitate predictions and aid in selecting the most effective Machine Learning algorithms.
#
# **What is Programming?**
#
# Programming is the way of the communication with the computer. It is defined by specific, sequential instructions. Simply put, it transforms ideas into step-by-step commands that a computer can process. These structured instructions are known as an algorithm.
#
# **Computer Algorithm**
#
# In computer systems, an algorithm is a logical sequence written in software by developers to process input and generate output on a target computer. An optimal algorithm delivers results more efficiently than a non-optimal one. Like computer hardware, algorithms are regarded as a form of technology.
#
# **What is a programming language?**
#
# To communicate instructions to a computer, we use programming languages. There are hundreds of them, each with its own rules (syntax) and meanings (semantics), much like human languages. Just as words can have different spellings and pronunciations across languages, the same message is expressed differently in various programming languages.
#
# No matter which programming language you choose, the computer does not understand it directly. Instead, it processes Machine Language, which consists of complex numerical sequences. Writing in machine language is challenging, which is why programming languages are considered high-level — they are closer to human languages. An explanation, how high-level languages are translated into machine language, is described below.
#
# **What is Source Code and how to run it?**
#
# Source code is the set of instructions programmers write in various programming languages. It is written in plain text without any formatting like bold, italics, or underlining. This is why word processors such as MS Word, LibreOffice, or Google Docs are not suitable for writing source code. These tools automatically add formatting elements like font styles, indentation, and other embedded data, which prevents the text from being pure code. Source code must consist solely of actual characters.
#
# There are three main ways to convert source code into machine code:
#
# * Compilation;
# * Interpretation;
# * A combination of both.
#
# A compiler is a program that converts the source code to the machine code.
#
# An interpreter is a computer program that directly executes instructions written in a programming language,
# without requiring them previously to have been compiled into a machine language program.
#
# Comparison between Compiler and Interpreter:
#
# - Compiler: Translates the entire code in one go.
# - Interpreter: Executes the code one line at a time.
# - Compiler: Produces a standalone executable machine code file.
# - Interpreter: Runs the code directly without generating a separate file.
# - Compiler: Once compiled, the source code is not needed.
# - Interpreter: The source code must be available every time it runs.
# - Compiler: Executes faster because the code is precompiled.
# - Interpreter: Executes more slowly as it translates the code during runtime.

# ## 1.5 Answers to the exercises
#
# ### 1.5.1
#
# 1.
# - Data Scientist: works with large datasets and applies machine learning and statistical methods to derive insights.
# - Data Engineer: designs and maintains data infrastructure and optimizes data pipelines.
# - Data Analyst: analyzes data patterns and creates reports and visualizations to support decision-making.
# - Statistician: utilizes statistical methods and models to analyze and interpret data.
# - Data Architect: plans and structures databases and data storage systems.
# - Data Admin: ensures data security, accessibility, and proper maintenance of databases.
# - Business Analyst: connects data insights with business strategies.
# - Data/Analytics Manager: leads data teams and manages projects and strategies related to data within an organization.
# These roles are interrelated, all focused on data processing, analysis, and decision-making, but with different focuses — some prioritize infrastructure (Data Engineer, Data Architect), while others concentrate on analysis and insights (Data Scientist, Data Analyst, Statistician).
# 2.
# * Algorithm: A systematic process to solve a problem step by step.
# * Flowchart: A graphical representation of an algorithm using standardized symbols.
# 3.
# - Start the program.
# - Prompt the user to input the Principal Amount (principal).
# - Prompt the user to input the Rate of Interest (rate).
# - Prompt the user to input the Time period in years (years).
# - Calculate the Simple Interest (simple_interest) using the formula:
#     - simple_interest = (principal × rate × years) / 100.
# - Display the computed Simple Interest.
# - End the program.
# 4. Key Factors in Programming: Correctness, Readability, Efficiency, Maintainability, Scalability.
# 5. Machine Language: Consists of binary code (0s and 1s).
# 6. Programming languages are structured, exact, and driven by syntax, whereas spoken languages are often ambiguous and context-dependent.
#
# ## 1.5.2
#
# 1. True;
# 2. False;
# 3. False;
# 4. True;
# 5. False;
# 6. False;
# 7. True;
# 8. False;
# 9. True;
# 10. False.
#
# ## 1.5.3
#
# 1. Algorithm to Calculate Simple Interest on a Principal Amount
# - Start the program.
# - Prompt the user to input the Principal Amount (principal).
# - Prompt the user to input the Rate of Interest (rate).
# - Prompt the user to input the Time period in years (years).
# - Calculate the Simple Interest (simple_interest) using the formula:
#     - simple_interest = (principal × rate × years) / 100.
# - Show the Simple Interest to the user.
# - End the program.
#
# 2. Algorithm to Calculate the Area of a Rectangle
# - Start the program.
# - Prompt the user to input the Length (length) of the rectangle.
# - Prompt the user to input the Width (width) of the rectangle.
# - Calculate the Area (area) using the formula:
#     - area = length × width.
# - Show the Area of the rectangle to the user.
# - End the program.
#
# 3. Algorithm to Calculate the Perimeter of a Circle
# - Start the program.
# - Prompt the user to input the Radius (radius) of the circle.
# - Calculate the Perimeter (perimeter) using the formula:
#     - perimeter = 2 × π × radius.
# - Show the Perimeter of the circle to the user.
# - End the program.
#
# 4. Algorithm to Find All Prime Numbers Less Than 100
# - Start the program.
# - Loop through numbers from 2 to 100.
# - For each number:
#     - Assume the number is prime.
#     - Check if the number is divisible by any number from 2 to the square root of the number.
#     - If divisible, mark it as not prime.
# - In case the number is prime, display it.
# - Repeat for all numbers up to 100.
# - End the program.
#
# 5. Algorithm to Convert an Uppercase Sentence to Sentence Case
# - Start the program.
# - Prompt the user to input a sentence in uppercase.
# - Convert the first letter of the sentence to uppercase.
# - Turn the remaining letters of the sentence to lowercase.
# - Couple the formatted text into a Sentence Case version.
# - Show the converted sentence.
# - End the program.
#
# 6. ![s_1-1.png](attachment:s_1-1.png)
#
# 7. ![scr_2-2.png](attachment:scr_2-2.png)
#
# 8. ![scr_4-4.png](attachment:scr_4-4.png)
#
# 9. ![scr_6-6.png](attachment:scr_6-6.png)
#
# 10. ![scr_7-7.png](attachment:scr_7-7.png)
#
# ## 1.5.4
#
# 1. Artificial Intelligence & Machine Learning (AI/ML), Data Engineering & Cloud Computing, Edge Computing & IoT Analytics, Quantum Computing & Data Science
# 2. PyCharm, VS Code, Spyder, Eclipse + PyDev, Wing IDE, Jupyter Notebook.
# 3.
# * Compiled Languages: C, C++, Java - known for high speed and efficiency, making them ideal for system software and game development.
# * Interpreted Languages: Python, JavaScript, Ruby – offer easier debugging and flexibility, commonly used for scripting, automation, and web development.
# 4. For example, arranging optimal daily time schedule.
# 5. Repetitive Tasks to Automate:
# - File organization (sorting, renaming, and categorizing files).
# - Email filtering and automatic responses.
# - Web scraping for data extraction.
# - Report generation and formatting.
# - Automated backups and file synchronization.
# - System monitoring and log analysis.
# - Invoice generation and expense tracking.
# - Form filling and document generation.
# - Automating software testing and deployment.
# - Scheduling meetings and calendar management.
# - Data cleaning and preprocessing for analytics.
