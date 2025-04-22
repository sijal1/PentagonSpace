def fun1():
    print("insde fun1")
def fun2(Arg):
    print("entering fun2")
    Arg()
    print("leavinf fun2")
fun1()
fun2(fun1)        