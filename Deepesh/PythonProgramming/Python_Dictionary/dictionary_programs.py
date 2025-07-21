str1 = "Hello we are Learning Python"
#output = {"Hello": 5, "we": 2, "are": 3, "Learning": 8, "Python": 6}

#output2 = {"Ho": "HHeelllloo", "we": "wwee", "ae": "aarree", "Lg": "LLeeaarrnniinngg", "Pn": "PPyytthhoonn"}

result = {}
for word in str1.split():
    result[word] = len(word)

print(result)
# {'Hello': 5, 'we': 2, 'are': 3, 'Learning': 8, 'Python': 6}

