#Example 1

#Datatype in python

#Numbers
#1.Integer
#2.float
#3.Complex Numbers

#1.Integer
n3=50
print(n3,type(n3))

n2=20
print("n2", n2 , type(n2))

n3=30
print(n3,type(n3))

#Numbers

#2.float
n4=50.2
print(n4,type(n4))

#SEQUENTIAL
#1.string

s="silji"
print(s,type(s))
str='ebin'
print(str,type(str))
string='''
hei hello
python
'''
print(string,type(string))

#        0  1  2  3  4  5
str_a = "p  y  t  h  o  n"
#       -1 -2 -3 -4 -5  -6
# print("value:",str_a[0])
print(str_a[5])  #n
# space also will consider

#List
List8=[5,6,7,8]
List8.append(50) #append is insert method
print(List8)
print(List8[1])

List9=[5,6,7,[100,200,300],8]
print(List9)
print(List9[3][1])


#Tuple
T1= [5,"hello",-7,(1,2,3),[10,11,12]]
print(T1) #[5, 'hello', -7, (1, 2, 3), [10, 11, 12]]
print(T1[1]) #hello
print(T1[3][-2]) #2

#Dictionary

dic={'a':1,  #a is the key and 1 is the value
      5:9.9,
      55:(33.2),
         (8,7,9):[44,55,66],
          True:{555,111}
    }
print(dic)
#{'a': 1, 5: 9.9, 55: 33.2, (8, 7, 9): [44, 55, 66], True: {555, 111}}
#cannot define list as a key

#get value from key
print(dic['a']) #1
print(dic[55])
print(dic[8,7,9])
print(dic[8,7,9][1])
print(dic.keys())
print(dic.values())


#set #Mutable
set1={4,5,5.6,"hello",(8,9,10),True,None,4,5}
print(set1)

set1.add(500)
print(set1)