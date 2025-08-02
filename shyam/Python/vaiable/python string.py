"""
Slicing Home Work
str1 = Virat is Great India Batsman
# repeat first and last character three times
op1 = VVVirat is Great India Batsmannn
 print(op1)
# repeat first and last character 2 times of each word.
op2 = VViratt iiss GGreatt IIndiaa BBatsmann

# replace first and last character each word from given string
op3 = tiraV si treaG andiI natsmaB

# repeat each vowels 2 times in given string
op4 = Viiraat iis Greeaat IIndiiaa Baatsmaan

"""
"""
# repeat first and last character three times
str1 = "Virat is Great India Batsman"
#op1 = VVVirat is Great India Batsmannn
w1='virat'
c1=(w1[0]*2+w1)
w2='Batsman'
c2=(w2+w2[6]*2)
print(f"{c1} {c2}")

# repeat first and last character 2 times of each word.
str2 ="Virat is Great India Batsman"
w1='virat'
ch1=(w1[0]*1+w1+w1[4]*1)
w2='is'
ch2=(w2[0]*1+w2+w2[1]*1)
w3='great'
ch3=(w3[0]*1+w3+w3[4]*1)
w4='india'
ch4=(w4[0]*1+w4+w4[4]*1)
w5='batsman'
ch5=(w5[0]*1+w5+w5[6]*1)
print(f"{ch1} {ch2} {ch3} {ch4} {ch5}")

"""
"""
# replace first and last character each word from given string
#op3 = tiraV si treaG andiI natsmaB
str2 ="Virat is Great India Batsman"
w1='virat'
char1=(w1[-5])
print(char1)
char2=(w1[4])
print(char2)
cha3=(w1[1:4])
print(cha3)

print(f"{char2}{cha3}{char1}")
"""
# repeat each vowels 2 times in given string
#op4 = Viiraat iis Greeaat IIndiiaa Baatsmaan
str4 ="Virat is Great India Batsman"
vowels = "aeiouAEIOU"
if vowels in str4:
     print(vowels*2,str4)
else:
      print("not found")
