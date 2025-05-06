class TV():
    def __init__(self):
        self.brand="sony"
        self.cost=15000
    def on(self):
        print("tv is on")
    @staticmethod
    def display():
        print("tv is running")
    @classmethod    
    def off(cls):
        print("tv is off")
    
t1=TV()
t1.on()
t1.display()# not the standart way to call static and class method 
t1.off()    # but will give output

TV.display() # standard method
TV.off()  