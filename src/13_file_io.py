"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

# YOUR CODE HERE
#f = open('foo.txt', 'r')
with open('foo.txt') as f:
    read_data = f.read()
    print(read_data)

file_open = open("foo.txt", 'r')
print(file_open)
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
f=open("bar.txt", "w+")

for i in range(3):
    #f.write("This is line %d\r\n" % (i+1))
    #f and {} goes together, f = .format
    f.write(f"This is line {i+1}\r\n")