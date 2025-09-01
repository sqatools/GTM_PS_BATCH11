## declaring global variable

# xy = 100
#
# def func():
#     xy = 300
#     print(xy)
#
# func()
#
# print(xy)

## changing global variable value inside the func
# xy = 100
#
# def func():
#     global xy
#     xy = 300
#     print(xy)
#
# func()

# print(xy)

##################

# def cool():
#     global y
#     y = 35
#     print(y)
# cool()
# print(y)


########################## positional arguments

# def cool(i,j):
#     print(i,j)
#
# cool(10,20)

############## keyword arguments

# def cool(i,j=40):
#     print(i,j)
#
# cool(20)


### combination of positional and key arguments #####

# def hot(a,b,c):
#     print(a,b,c)
#
# hot(10,30,50)
# hot(10,30,c=40)
# hot(30,b=50,c=20)
# hot(a=30,20,50) ###SyntaxError: positional argument follows keyword argument

###########largest number
#
# def largest(a,b):
#     if a>b:
#         print("a is largest")
#     else:
#         print("b is the largest")
#
# largest(50,40)

