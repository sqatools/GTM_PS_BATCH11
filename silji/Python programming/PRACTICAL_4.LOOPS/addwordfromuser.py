# Python Loops program that will add the word from the user to the empty string using python.
# Input: “python”
# Output : “python”

# Input from the user
word = input("Enter the word: ")

# Initialize empty string
result = ""

# Loop to add each character to result
for ch in word:
    result +=ch

# Output the final result
print("Output:", result)