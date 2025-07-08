# Q2 :  write a python function to get fabonacci serise till 10 values return as list

def fibonacci_series(n):
    fib_list = []
    a, b = 0, 1
    for i in range(n):
        fib_list.append(a)
        a, b = b, a + b
    return fib_list


result = fibonacci_series(10)
print(result)

def fibonacci_series(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Print first 10 Fibonacci numbers
fibonacci_series(10)







