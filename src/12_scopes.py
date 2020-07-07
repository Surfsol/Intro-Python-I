# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# When you use a variable in a function, it's local in scope to the function.
x = 12

def change_x():
    x = 99

change_x()
x = 99

   

# This prints 12. What do we have to modify in change_x() to get it to print 99?
print(x)


# This nested function has a similar problem.

def outer():
    y = 120

def inner():
    y = 999

    inner()

    # This prints 120. What do we have to change in inner() to get it to print
    # 999?
    # Note: Google "python nested function scope".
    print(y)


outer()


#local, enclosing, global, built in

#local
x = 1
y = 2

def mmm(x):
    y = 3
    print(x, y)

mmm(10)
print(x, y)

x = 100

def my_outer(x):
    y = 50

    def inner():
        print(x,y)
    inner()

my_outer(75)


#last scope to be searched Builtin
print(pow(2, 3))

#see builtin variables

#puts a variable in global scope
def vus():
    global x 
    x = 100

vus()
print(x)