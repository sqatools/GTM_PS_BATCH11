str1 = "Hello we are Learning Python"
# output = {"Hello": 5, "we": 2, "are": 3, "Learning": 8, "Python": 6}

string = "Hello we are Learning Python"
words = string.split()

output = {}

for word in words:
    output[word] = len(word)

print(output)

