"""
global variable: The variable that we declare outside of the functions is known as global variable
                ->  global variable scope is acoss the entire module, it means all the function can
                    access global variable
                ->  If we want to update the global variable value inside the function, then we
                    have to user global keyword and mention variable name. e.g.
                    global var_x
                    var_x = 500
local variable: When we declare a variable inside the function, then it is called local variable
                -> local variable scope is limited to the function, we can not access it outside of the function.


nonlocal variable: when we define any variable in outer function and the that variable is accessible for all
                   the inner function then it is called non-local variable
                   -> non-local variable scope is limited to outer function as well as all inner function only
                      can not use outside of the outer function.

                   ->  If we want to update the value of nonlocal variable inside the inner function, then we
                       have to use nonlocal keyword. eg.
                       nonlocal var_q
                       var_q = 2500
"""
# global variable
var_x = 100

def function1():
    print("------- Function1 -------")
    global var_x
    var_y = 200 # local variable
    var_x = 500
    print("global variable var_x :", var_x)
    print("local variable var_y:", var_y)


def function2():
    print("------- Function2 -------")
    var_z = 300 # local variable
    print("global variable var_x :", var_x)
    print("local variable var_z:", var_z)


#function2()
#function1()
#function2()
"""
------- Function2 -------
global variable var_x : 100
local variable var_z: 300

------- Function1 -------
global variable var_x : 500
local variable var_y: 200

------- Function2 -------
global variable var_x : 500
local variable var_z: 300


"""

################# nonlocal variable ###########

var_p = 1000 # global variable
def outer_function():
    var_q = 2000 # nonlocal variable

    def inner_fun1():
        print("\n ----- inner function1 ----- \n")
        global var_p
        nonlocal var_q
        var_p = 1500
        var_q = 2500
        var_r = 500 # local variable
        print("global variable var_p:",var_p)
        print("nonlocal variable var_q:", var_q)
        print("local variable var_r :", var_r)


    def inner_fun2():
        print("\n----- inner function2 ----- \n")
        var_s = 800 # local variable
        print("global variable var_p:",var_p)
        print("nonlocal variable var_q:", var_q)
        print("local variable var_s :", var_s)

    inner_fun2()
    inner_fun1()
    inner_fun2()

outer_function()



