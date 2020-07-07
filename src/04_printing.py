"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
x = 10
y = 2.25
z = "I like turtles!"
print("I am %d, I have %f dollars and %s" %(x, y, z))
# Use the 'format' string method to print the same thing
print("I am {}, I have {} dollars and {}".format(10, 2.25, "I like turtles!") )
# Finally, print the same thing using an f-string
print("I am {0}, I have {1} dollars and {said}".format(10, 2.25, said= "I like turtles!") )