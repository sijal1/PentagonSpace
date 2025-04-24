# WAP to collect 5 integer values and store it  in a list

""" n=0
a=[]
while(n!=5):
    i=int(input("enter elem : "))
    a.append(i)
    n+=1
print(a) """

""" l=[]
i=0
while i<=4:
    print('enter a value ')
    num = int(input())
    l.insert(i,num)
    i=i+1
print(l)    """ 

l=[]
for i in range(5):
    print('enter elem')
    num = int(input())
    l.insert(i,num)
print(l)    