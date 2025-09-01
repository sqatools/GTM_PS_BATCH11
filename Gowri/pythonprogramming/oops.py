### Example 1 ###

# class myclass():
#     def myfunc(self,name):
#         print(name)
#
# mc = myclass()
# mc.myfunc("discipline")

#### Example 2 ####
# class myclass():
#     def myfunc(self,a):
#         print(a)
#     @staticmethod
#     def ins(self,d,c,s):
#         print(d,c,s)
#
# mc=myclass()
# mc.myfunc(35)
#
# mc.ins(10,45,35,57)
# myclass.ins(10,454,36,7)


##### example 3 #####

# class myclass():
#     a,b = 30,40
#     def myfunc(self,a,b):
#         print(self.a+self.b)
#         print(a+b)
# mc=myclass()
# mc.myfunc(10,30)

### Example 4 #####
# x,y = 30,45
# class myclass():
#     x,y = 24,67
#     def myfunc(self,x,y):
#         print(self.x+self.y)
#         print(x+y)
#         print(globals()['x']+globals()['y'])
#
# mc= myclass()
# mc.myfunc(10,30)


#### Example 5 ####

# class myclass():
#     def myfunc(self,name):
#         print(name+" "+"is Consistent enough to achieve a goal")
# obj1 =myclass()
# obj2 = myclass()
# obj1.myfunc("Spandana")
# obj1.myfunc("Gowri")


#### Constructor ###
# class myclass():
#     def __init__(self,a,b):
#         print(a,b)
# mc = myclass(20,35)
# mc.__init__(10,30)

### Example of class variable

# class myclass():
#     name = "Consistency"
#     def __init__(self,name):
#         print(name)
#         print(self.name)
#
# mc= myclass("discipline")


##### Example 8 ###

## constructor:self.eid=eid, self.ename=ename,self.sal=sal
#      display :print eid,ename,sal
# class myclass():
#     def __init__(self,eid,ename,sal):
#         self.eid=eid
#         self.ename=ename
#         self.sal=sal
#     def display(self):
#         print(self.eid,self.ename,self.sal)
# mc1=myclass(101,"Spandana",100000)
# mc1.display()
# mc2=myclass(102,"consistency",140000)
# mc2.display()

##### Example 9 ####
## constructor: self.eid=eid, self.ename=ename,self.sal=sal
#      constructor :print eid,ename,sal

# class myclass():
#     def __init__(self,ename,eid,sal):
#         self.ename=ename
#         self.eid=eid
#         self.sal=sal
#
#     def __str__(self):
#         return(self.ename)
# mc=myclass("Discipline",1343,156000)
# print(mc)
