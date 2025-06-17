
"""
Slicing Home Work
"""
"""
str1 = Virat is Great India Batsman
# repeat first and last character three times
op1 = VVVirat is Great India Batsmannn
"""

strhm1 = "Virat is Great India Batsman"
first_char = strhm1[0]
last_char = strhm1[-1]

print(first_char * 3 + strhm1[1:-1] + last_char * 3)


# repeat first and last character 2 times of each word.
# op2 = VViratt iiss GGreatt IIndiaa BBatsmann

strhm2 = "Virat is Great India Batsman"
first_char1 = strhm2[0:1]
first_char2 = strhm2[4:5]
second_char1 = strhm2[6:8]
third_char1 = strhm2[9:10]
fourth_char1 = strhm2[13:14]
fifth_char1 = strhm2[15:16]
sixth_char1 = strhm2[19:20]
seventh_char1 = strhm2[21:22]
Eight_char1 = strhm2[27:28]

print(first_char,first_char2,second_char1,third_char1,fourth_char1,fifth_char1,sixth_char1,seventh_char1,Eight_char1)

print(first_char1 * 2 + strhm2[1:4] +  first_char2 * 2 + " " + second_char1 * 2 + " " + third_char1 * 2 + strhm2 [10:13] + fourth_char1 * 2 +
     " " + fifth_char1 * 2 + strhm2[16:19] + sixth_char1 * 2 + " " + seventh_char1 * 2 + strhm2[22:27] + Eight_char1 * 2)



# replace first and last character each word from given string
# op3 = tiraV si treaG andiI natsmaB
second_char2 = strhm2[-21:-23:-1]
print(second_char2)

print(first_char2 + strhm2[1:4] +  first_char1 + " " + second_char2 + " " + fourth_char1 + strhm2 [10:13] + third_char1 +
     " " + sixth_char1 + strhm2[16:19] + fifth_char1 + " " + Eight_char1 + strhm2[22:27] + seventh_char1)



# repeat each vowels 2 times in given string
# op4 = Viiraat iis Greeaat IIndiiaa Baatsmaan

strhm3 = "Virat is Great India Batsman"
vowels = "AEIOUaeiou"

result=""
for ch in strhm3:
    if ch in vowels:
        result += ch * 2
    else:
        result += ch

print(result)