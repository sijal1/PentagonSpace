# @property decorator in encapsulation

class student:
    def __init__(self):
        self.__name=""

    @property    
    def dataAccess(self):
        return self.__name

    @dataAccess.setter
    def dataAccess(self,value):
        self.__name=value

s1=student()
s1.dataAccess="sijal"    
res=s1.dataAccess
print(res)