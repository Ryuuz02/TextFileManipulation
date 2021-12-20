"""
Prints out the beginning text
file_reader = open("text.txt", "r")
print("Beginning contents of file: \n" + file_reader.read())
"""

"""
using the write() function, we can overwrite all of the content in the text file and replace it with what we input
with open("text.txt", "w") as f:
    f.write("Hey guys, scarce here")
"""

"""
If we use writelines(), we can give it a list of strings and it will replace the contents of the file with the strings
with open("text.txt", "w") as f:
    f.writelines(["So ", "guys,\n", "we did it"])
"""


"""
Resets back to the beginning and prints out everything in the file
file_reader.seek(0)
print("Ending contents of file: \n" + file_reader.read())
"""
