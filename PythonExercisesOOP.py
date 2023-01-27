# Ex 1.

from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def setRadius(self, radius):
        self.radius = radius
    def getRadius(self):
        return self.radius


    def getArea(self):
        return pi * self.radius ** 2
    def getPerimeter(self):
        return 2 * pi * self.radius

    
circle1 = Circle(3)
print(circle1.getRadius())
circle1.setRadius(5)
print(circle1.getRadius())
print(circle1.getArea())
print(circle1.getPerimeter())


# Ex 2.
class BasicPlan:
    can_stream = True
    can_download = True
    has_SD = True
    has_HD = False
    has_UHD = False
    num_of_devices = 1
    price = 8.99

class StandardPlan(BasicPlan):
    has_HD = True
    num_of_devices = BasicPlan.num_of_devices + 1
    price = BasicPlan.price + 4
class PremiumPlan(StandardPlan):
    has_UHD = True
    num_of_devices = StandardPlan.num_of_devices + 2
    price = StandardPlan.price + 3

basic = BasicPlan()
print(basic.price)

standard = StandardPlan()
print(standard.price)

premium = PremiumPlan()
print(premium.price)
print(premium.has_SD)
print(premium.has_HD)
print(premium.has_UHD)
