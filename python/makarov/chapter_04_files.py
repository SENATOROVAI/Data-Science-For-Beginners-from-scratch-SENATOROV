"""Intro to Google Colab."""

# +
import os

import pandas as pd

# from google.colab import files

# +
# create a object of that class and call method.upload()
# uploaded: dict[str, bytes] = files.upload()
# -

# display paths to folders (dirpath)
# and file names (filenames) and then
for dirpath, _, filenames in os.walk("/content/"):

    # in the nested loop, we go through the file names
    for filename in filenames:

        # and join the path to the folders and
        # the files contained in these folders
        # using the path.join() method
        print(os.path.join(dirpath, filename))

# Let's look the contents of the content folder.
# !ls

# Let's take a look inside sample_data
# !ls /content/sample_data/

# +
# lets look type of  uploaded
# type(uploaded["test.csv"])

# +
# Let's turn to the dictionary key uploaded and apply the .decode() method.
# uploaded_str: str = uploaded["test.csv"].decode()

# the output is a regular string
# print(type(uploaded_str))

# +
# print the first 35 characters of the string
# print(uploaded_str[:35])

# +
# if we split the string using the .split() method by the characters \r
# (return to the beginning of the string) and \n (new line)
# uploaded_list: list[str] = uploaded_str.split("\r\n")

# the output will be a list
# type(uploaded_list)

# +
# pass the file address to the open() function
# the 'r' parameter means that we want to read the file
# f1: TextIO = open("/content/train.csv")

# The .read() method places the entire file in a single line.
# Let's display the first 142 characters (if no parameter is specified,
# the entire content will be displayed).
# print(f1.read(142))

# At the end, the file must be closed.
# f1.close()

# Taking into account the requirements of the reviewers,
# the code has been corrected as follows:
with open("file.txt", encoding="utf-8") as f1:
    data = f1.read()

# +
# f2: TextIO = open("/content/train.csv")
with open("/content/train.csv", encoding="utf-8") as f2:

    # Let's go through our object in a
    # for loop and create an index in parallel.
    for i, line in enumerate(f2):

        # display lines without service characters at the edges
        print(line.strip())

        # When we reach the fourth line, we will pause.
        if i == 3:
            break

# Let's not forget to close the file.
# f2.close()
# -

# Let's tell Python: "Open the file and name it f3."
with open("/content/test.csv", encoding="utf-8") as f3:

    # "go through the lines without service characters"
    for i, line in enumerate(f3):
        print(line.strip())

        # and "break on the fourth line"
        if i == 3:
            break

# Apply the read_csv() function and examine
# the first three records of the train.csv file.
train: pd.DataFrame = pd.read_csv("/content/train.csv")
train.head(3)

# Let's do the same with the test.csv file.
test: pd.DataFrame = pd.read_csv("/content/test.csv")
test.head(3)

# +
# The sample file can be downloaded from the
# Internet rather than from a local computer.
host = "https://www.dmitrymakarov.ru/"
url = host + "wp-content/uploads/2021/11/titanic_example.csv"

# just put its URL into the read_csv() function
example = pd.read_csv(url)
example.head(3)
# -

# Create a new file result.csv using to_csv(),
# removing the index in the process.
# result.to_csv('result.csv', index = False)
# The file will be saved, and if everything goes well
# we will display the following text:
print("The file has been successfully saved to session storage!")

# +
# apply the .download() method of the files object
# files.download("/content/result.csv")
