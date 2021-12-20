"""
Opens a file object of text.txt of a reading type
file_reader = open("text.txt", "r")
"""

"""
print(file_reader.read())
Returns all of the file as one long string (new lines will have \n so that it will still print matching the file format)
prints:
Gamering Gamers
Game
Games
"""

"""
print(file_reader.read(5))
For every read type (readline, readlines, read) you can use a parameter to determine how many characters to read
prints:
Gamer
"""

"""print(file_reader.readline())
Returns the next unread line as a string
prints:
Gamering Gamers
"""

"""print(file_reader.readlines())
Converts all of the contents of the file to a list
prints:
["Gamering "Gamers\n", "Game\n", "Games"]
"""

"""
file_reader.close()
"""
