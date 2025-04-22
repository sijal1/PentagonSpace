a=[]
v=[]
print("enter points for ajay")
a=[int(input()) for i in range(3)]
print("enter points for vijay")

v=[int(input()) for i in range(3)]
ap=0
vp=0
for i in range(0,2+1,1):
    if(a[i]>v[i]):
        ap=ap+1
    if(v[i]>a[i]):
        vp=vp+1
if(ap>vp):
    print("ajay won")
elif(vp>ap):
    print("vijay won")
else:
    print("draw")                    