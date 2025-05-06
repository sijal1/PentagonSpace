class Heroine:
    def __init__(self):
        self.name="ramya"
        self.age=48
        self.numOfMovies=35
    def act(self):
        print("ramya is a versatile actress")
h1=Heroine()
print(h1.name)
print(h1.age)
print(h1.numOfMovies)
h1.act()
h1.height=5.5
print(h1.height)
h1.age=50
print(h1.age)
del h1.height
# print(h1.height)  throws error since height is deleted            