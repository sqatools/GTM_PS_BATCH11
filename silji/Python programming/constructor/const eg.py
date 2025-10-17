class Emp:
    def __init__(self,eid,ename,sal):
        self.eid=eid
        self.ename=ename
        self.sal=sal
    def display(self):
      print(self.eid,self.ename,self.sal)

    def __str__(self):
         return(self.ename)


e1=Emp(101,"john",50000)
print(e1)

# e2=Emp(102,"scott",70000)
# e2.display()