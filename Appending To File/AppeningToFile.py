"""
Appending rather than writing is pretty much the exact same thing, except instead of replacing everything currently in
the file, it will instead just add it to the end of the file, fitting the same as a list using .append()
with open("text.txt", "a+") as f:
    f.write("\nComing and they don't stop")
    f.seek(0)
    print(f.read())
"""

"""
It can also use writelines(), This does the exact same thing as the above .write version
with open("text.txt", "a+") as f:
    f.writelines(["\nComing", " and they don't stop"])
    f.seek(0)
    print(f.read())
"""

