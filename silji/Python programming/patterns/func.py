# def fun(i,j=100):
#     print(i,j)
#
# fun(300,200)

# def cal(a,b):
#     return (a+b)
#
# sum=cal(300,200)
# print(sum)

def largest(a,b):
    if a>b:
        return a,b
    else:
        return b,a
res=largest(50,90)
print(res)