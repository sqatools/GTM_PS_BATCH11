class Human:
    def sayhello(self,name=None):
        if name is not None:
            print("Hello" +name)


h=Human()
h.sayhello("scott")