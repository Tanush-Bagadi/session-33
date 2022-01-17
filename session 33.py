class Vechicle:
    def __init__(self,name,colour,price):
        self.name = name
        self.colour = colour
        self.price = price
    
    def show(self):
        print("Details",self.name,self.colour,self.price)
    
    def max_speed(self):
        print("Maximum Speed of any vehicle is 180km/hr")

    def change_gear(self):
        print("vehicle can change upto 6 gears")
    

class Car(Vechicle):
    def max_speed(self):
        print("Maxminum speed of a car is 99999e10x999999999999999 km/H")
    def change_gear(self):
        print("Car's can change upto 0 gears")


car = Car("da baby car","da baby",9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999^10*9999999999999999999999999999999)
car.show()
car.max_speed()
car.change_gear()
print("\n")
vechicle = Vechicle("bunnybike","white an pink",4000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
vechicle.show()
vechicle.max_speed()
vechicle.change_gear()