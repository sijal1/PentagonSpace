class a:
    def __init__(self):
        self.a=10
class b(a):
    def __init__(self):
        #a.__init__(self)
        super().__init__()
        self.b=20
class c(b):
    def __init__(self):
        #b.__init__(self)
        super().__init__()

        self.c=30
c1=c()
print(c1.c)
print(c1.b)
print(c1.a)
