""" class farmer:
    def __init__(self, p, t, r):
        self.principle = p
        self.time = t
        self.rate = r

    def loan(self):
        si = (self.principle * self.time * self.rate) / 100
        print(si)

f1 = farmer(200000,3,2.5)
f2 = farmer(500000,7,2.5)
f1.loan()
f2.loan() """

# with static(rate) value 
class farmer:
    
    r=2.5  #static var
    def __init__(self, p, t):
        self.principle = p
        self.time = t

    def loan(self):
        si = (self.principle * self.time * farmer.r) / 100
        print(si)

f1 = farmer(200000,3)
f2 = farmer(500000,7)
f1.loan()
f2.loan()
print(farmer.r) #accessing static variable