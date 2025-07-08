# 14). Python function program to access a function inside a function.
def outer_function():
    print("This is the outer function.")

    def inner_function():
        print("This is the inner function.")

    # Call inner function from outer
    inner_function()

# Call the outer function
outer_function()