class calci():
    def math(self,a,b):
        c1=a+b
        c2=a-b
        c3=a*b
        c4=a/b
        return c1,c2,c3,c4
c=calci()
x=10
y=20
res=c.math(x,y)
print(res) #tuple o/p
r1,r2,r3,r4=c.math(x,y)
print(r1)
print(r2)
print(r3)
print(r4)