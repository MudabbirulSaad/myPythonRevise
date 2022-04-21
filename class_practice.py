class Vehicle():
    name = ""
    kind = ""
    color = ""
    value = ""
    def description(self):
        desStr = "{} is a {} {} worth ${}.".format(self.name, self.color, self.kind, self.value)
        return desStr

car1 = Vehicle()
car2 = Vehicle()

car1.name = "Lamborghini"
car1.kind = "super car"
car1.color = "black"
car1.value = 100000.00

car2.name = "BMW"
car2.kind = "super car"
car2.color = "red"
car2.value = 150000.00

print(car1.description())
print(car2.description())