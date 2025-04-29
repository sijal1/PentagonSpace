def main():
    str="pentagon"
    return str

def outer(arg):
    print("inside OUTER fn")

    def inner():
        print("entering inner")
        ptr=arg()
        ans=ptr.upper()
        print(ans)
    return inner

ref = outer(main)
ref()    
