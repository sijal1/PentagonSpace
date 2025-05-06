#public method to privsate method

class dog:
    def __init__(self):
        self.name="dog"

    def __bark(self):
        print("dog is barking")

    def helper(self):
        self.__bark()    
d1=dog()
print(d1.name)
d1.helper()            