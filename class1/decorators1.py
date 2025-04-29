def main():
    print("main function")

def outer(arg):
    print("inside OUTER fn")

    def inner():
        print("entering inner")
        ptr=arg
        ptr()
        print("leaving inner")

    return inner
ref = outer(main)
ref()    
