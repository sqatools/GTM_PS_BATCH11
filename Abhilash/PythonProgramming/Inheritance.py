#Inheritance

# Inheritance :
# 1.Aquaring all the variables and methods from one class another class is called Inheritance.
# 2. we using for reusability
# 3. Avoid duplication
# super() -- To invoke the parent class method through the child class method

#
# Type of Inheritance:
#
# 1. single ---- only one parent and one child
# 2. multi level --- only one parent and have multi levels of child
# 3. Heirachy --- only one parent and can have any number of child
# 4. multiple ---- multipe parents and only one child
#
# In class mention upper case and in Variable lower.

# Example 1: single

# class A:              # parent
#     def m1(self):
#         print("this is m1 method from class A")
# class B(A):             # B is Child of A
#     def m2(self):
#         print("this is m2 method from class B")
#
# b = B()
# b.m1()   # this is m1 method from class A
# b.m2()   # this is m2 method from class B

# Example 2: single

# class A:              # parent
#     x, y = 10, 20
#     def m1(self):
#         print(self.x +self.y)
# class B(A):             # B is Child of A
#     a, b = 200, 100
#     def m2(self):
#         print(self.a-self.b)
#
# b = B()
# b.m1()   # 30
# b.m2()   # 100

#Example 3: Multilevel

# class A:              # parent
#     x, y = 10, 20
#     def m1(self):
#         print(self.x +self.y)
# class B(A):             # B is Child of A
#     a, b = 200, 100
#     def m2(self):
#         print(self.a-self.b)
# class C(B):
#     s,d = 10,2
#     def m3(self):
#         print(self.s * self.d)
# c= C()
# c.m1() # 30
# c.m2()  # 100
# c.m3()  # 20

# Example 4: Heirarchy
# class A:              # parent
#     x, y = 10, 20
#     def m1(self):
#         print(self.x +self.y)
# class B(A):
#     a, b = 200, 100
#     def m2(self):
#         print(self.a-self.b)
# class C(A):
#     s,d = 10,2
#     def m3(self):
#         print(self.s * self.d)
# b= B()
# b.m1() # 30
# b.m2() # 100
#
# c = C()
# c.m1() # 30
# c.m3() # 20

#Example 5: multiple

# class A:              # parent
#     x, y = 10, 20
#     def m1(self):
#         print(self.x +self.y)
# class B():             # Parent
#     a, b = 200, 100
#     def m2(self):
#         print(self.a-self.b)
# class C(A,B):
#     s,d = 10,2
#     def m3(self):
#         print(self.s * self.d)
#
# c=C()
# c.m1() # 30
# c.m2() #100
# c.m3() #20


# Example 6: calling parent class method using child class ( super() )

# class A:
#     def m1(self):
#         print("this is m1 method from class A")
# class B(A):
#     def m1(self):
#         print("this is m1 method from class B")
#         super().m1()
#
# obj = B()
# obj.m1()

# Example 7 :

# class A:
#     a,b = 10,20
#
# class B(A):
#     i, j = 100,400
#     def m1(self,x,y):
#         print(x + y)  # local Variable 50
#         print(self.i + self.j) # class Variable 500
#         print(self.a + self.b) # class Variable 30
#
# b=B()
# b.m1(20,30)

# Example 8: Overriding variables

# class parent:
#     name = "Abhi"
#
# class child(parent):
#     name = "Hi"
#     def test(self):
#         print(super().name)
#
# c = child()
# print(c.name) # Hi
# c.test() # Abhi

# Example 8: Overriding method












