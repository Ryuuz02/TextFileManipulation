"""The open function returns a file (the one specified in the parameters) that can be interfaced with according to the
mode parameter.
"r" is read only, "w" is for writing, "a" is for appending to the file
You can do multiple with +
"r+" can read and write
"w+" can also read and write (they seem to be the same)
"a+" can read and append
open("file_name", "mode")
"""

"""
Many times, files will be used with a with statement
for example
with open("file_name", "mode") as f:
    f.function()
When used this way, they automatically close and are self contained
"""

"""
With a file, there are many things you can do, the specifics (read, write, etc.) are in their associated directory
In general, there is close(), which closes the file (used to stop it from consuming memory, leaving one open can also 
corrupt the file
"""

"""
You can truncate a file (Basically shorten it)
f.truncate(10) shortens a file f to the first 10 characters
"""

"""
To access the internal number of the file, use fileno
f.fileno() returns the system number of the file
"""

"""
You can use seek to move where the "cursor" of the file is.
Basically the seek() function takes two parameters
The first is in relation to the second, so we can explain that one to begin with
The second parameter is the from_what argument
This one determines where in the file to put the cursor
0 is at the beginning of the file
1 is the current file location
2 is the end
This value defaults to 0
Then, we can use the first parameter, offset, to tell it how much to move from that spot
So, we can say seek(5, 0) to put the reference point to the 5th character in the file
seek(5) would do the exact same since the default from_what is 0
Similarly, we can say seek(5, 1). This will skip 5 spots in the file to end up 5 from where it was before the seek
You can not use negative input when reading as text
So the only real usage of seeking with from_what of 2 is to get to the end, you cannot use it with a negative offset 
to go back spaces
You can use negative offset when reading as binary however
"""

"""
In order to tell where the reference point currently is at, we can use tell()
For example
if we use f.read(10), then f.tell(), the tell will return 10
"""
