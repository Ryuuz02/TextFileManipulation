"""
with open("text.txt", "r") as f:
    print(f.readlines())
Performs everything inside the indented with block using the open file as the variable f
When the program leaves the with function, it will automatically close the open file
Can do the exact same things as assigning it to a global variable
"""