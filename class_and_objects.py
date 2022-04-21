class work:
    name = "saad"

    def printOut(self):
        print("This is a message inside class!")
    
user1 = work()
user2 = work()
user2.name = "zorin"

print(user1.name)
print(user2.name)



class NumberHolder:
    def __init__(self, number):
        self.number = number