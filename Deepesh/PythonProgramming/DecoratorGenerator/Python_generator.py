def greetings():
    return 'Hello good morning'
    return 'Good evening'

var1 = greetings()
print(var1)


# write a function with generator
def greeting_gen():
    yield 'Good Morning'
    yield 'Good Evening'
    yield 'Learning Python'
    yield 'India lost the Test Match with 22 Run'

output = greeting_gen()
print(output)
# print(next(output))
# print(next(output))
# print(next(output))
# print(next(output))
for val in output:
    print(val)



def get_square_of_list(list1):
    for val in list1:
        yield val**2


list2 = [3, 5, 7]*1000
output = get_square_of_list(list2)

for val in output:
    print(val)