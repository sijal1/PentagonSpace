def add(num):
    return num+10

l=[1,2,3,4,5]
res=list(map(add,l))
print(res)

#mapping with lambda

l=[1,2,3,4,5]
res1=list(map(lambda num:num+10,l))
print(res1)