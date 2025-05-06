class car:
    def __init__(self):
        self.__brand=""
    def setter(self,value):
        self.__brand=value
    def getter(self):
        return self.__brand
    getset=property(getter,setter) #property fn

c1=car()
c1.getset="bmw"
res=c1.getset
print(res)