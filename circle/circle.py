class Circle:
    Pi = 3.141592653589

    def __init__(self, r = 1):
        self.radius = r

    def __setattr__(self, name, value):
        if name == "radius":
            if value < 0:
                raise ValueError("Radius cannot be negative")
            self.__dict__["radius"] = value
            self.__dict__["diameter"] = 2 * value
            self.__dict__["area"] = Circle.Pi * value * value
        elif name == "diameter":
            if value < 0:
                raise ValueError("Diameter cannot be negative")
            self.__dict__["radius"] = value / 2
            self.__dict__["diameter"] = value
            self.__dict__["area"] = Circle.Pi * value * value / 4
        elif name == "area":
            raise AttributeError("can't set attribute")

    def __repr__(self):
        return "Circle(" + str(self.radius) + ")"

c = Circle()
print(c, c.radius, c.diameter, c.area)
c = Circle(5)
print(c, c.radius, c.diameter, c.area)
c = Circle()
c.radius = 10
print(c, c.radius, c.diameter, c.area)
c = Circle()
c.diameter = 10
print(c, c.radius, c.diameter, c.area)
c = Circle()
#c.radius = -1
print(c, c.radius, c.diameter, c.area)
c = Circle()
c.area = 10
print(c, c.radius, c.diameter, c.area)


