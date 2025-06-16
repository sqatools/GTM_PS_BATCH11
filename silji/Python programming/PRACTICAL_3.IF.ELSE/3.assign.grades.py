#If else program to assign grades as per total marks.

# marks > 40: Fail
# marks 40 – 50: grade C
# marks 50 – 60: grade B
# marks 60 – 70: grade A
# marks 70 – 80: grade A+
# marks 80 – 90: grade A++
# marks 90 – 100: grade Excellent
# marks > 100: Invalid marks

marks =50
if marks<40:
    print("fail")
elif marks>=40 and marks<=50:
    print("Grade c")
elif marks >=51   and marks <=60:
    print("Grade b")
elif marks>=61 and marks<=70:
    print("Grade A")
elif marks>=71 and marks<=80:
    print("Grade A+")
elif marks>=81 and marks<=90:
    print("Grade A++")
elif marks>=91 and marks<=100:
    print("Grade Excellent")
elif marks>100:
    print("Invalid")
else:
    print("Non valid")



