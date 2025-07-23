str1 = "Hello we are Learning Python"
#output2 = {"Ho": "HHeelllloo", "we": "wwee", "ae": "aarree", "Lg": "LLeeaarrnniinngg", "Pn": "PPyytthhoonn"}

str1 = "Hello we are Learning Python"
words = str1.split()

output2 = {}

for word in words:
    key = word[0] + word[-1]
    value = ''.join([ch * 2 for ch in word])
    output2[key] = value

print(output2)