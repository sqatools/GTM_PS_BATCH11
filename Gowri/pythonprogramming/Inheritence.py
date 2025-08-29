### single inheritence ####
#### Example 1 ###
# class A():
#     def m1(self):
#         print("m1 is the object of class A")
# class B(A):
#     def m2(self):
#         print("m2 is the object of class B")
# obj=B()
# obj.m2()
# obj.m1()


#### Example 2####
# class A():
#     x,y= 20,35
#     def add(self):
#         print(self.x+self.y)
# class B(A):
#     a ,b = 200,20
#     def sub(self):
#         print(self.a-self.b)
# obj=B()
# obj.sub()
# obj.add()

## multi level inheritence
#
# class A():
#     x,y=10,30
#     def add(self):
#         print(self.x+self.y)
# class B(A):
#     a,b=200,100
#     def sub(self):
#         print(self.a-self.b)
# class C(B):
#     c,d=10,20
#     def mul(self):
#         print(self.c*self.d)
# obj=C()
# obj.mul()
# obj.sub()
# obj.add()
#
#
# ## Hierarchy inheritance ###
# # class A():
# #     x,y=10,30
# #     def add(self):
# #         print(self.x+self.y)
# # class B(A):
# #     a,b=200,100
# #     def sub(self):
# #         print(self.a-self.b)
# # class C(A):
# #     c,d=10,20
# #     def mul(self):
# #         print(self.c*self.d)
# # obj=C()
# # obj.mul()
# # obj.add()
# #
# # obj2=B()
# # obj2.add()
# # obj2.sub()
#


# ## multiple inheritence ####
# class A():
#     x,y=10,30
#     def add(self):
#         print(self.x+self.y)
# class B():
#     a,b=200,100
#     def sub(self):
#         print(self.a-self.b)
# class C(A,B):
#     c,d=10,20
#     def mul(self):
#         print(self.c*self.d)
# obj=C()
# obj.mul()
# obj.add()
# obj.sub()


#### Example ###  Override methods

# class A():
#     def cool(self):
#         print("This is the method of class A")
#
# class B(A):
#     def cool(self):
#         print("This is the method of Class B")
#         super().cool()
# obj=B()
# obj.cool()


###### Example #####

# class A():
#     a,b=10,20
#
# class B(A):
#     x,y=133,400
#     def mul(self,c,d):
#         print(c*d)
#         print(self.y-self.x)
#         print(self.a+self.b)
# obj=B()
# obj.mul(5,5)


#### Example ###### override variables

# class parent():
#     name="Success"
#
# class child(parent):
#     name="consistent"
#     def test(self):
#         print(super().name)
#
#
# obj=child()
# print(obj.name)
# obj.test()

#### override methods #####


### polymorphism overloading method #####

# class Human():
#     def sayhello(self,name=None):
#         if name is not None:
#             print("Hello" + name)
#         else:
#             print("hello")
# obj=Human()
# obj.sayhello("Consistency")
# obj.sayhello()
