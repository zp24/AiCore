
class Shape: #super/parent class

    def __init__(self, num_sides, tesselates):

        self.num_sides = num_sides
        #num_sides = int
        self.tesselates = tesselates #a shape that can create a pattern with itself without leaving any gaps (rectangle, square, equilateral triangle and regular hexagon)
        #tesselates = ""
        
        #raise error if number_sides is 0
        try:
           x =  num_sides > 0, "this shape has more than 0 sides"
        except:
           x = "needs a number of sides"
        print(x)


    def get_info(self):
        raise NotImplementedError("not yet implemented")
        if self.tesselates == "yes":
            return f"This shape has {self.num_sides} sides and tesselates"
        else:
            return f"This shape has {self.num_sides} sides and does not tesselate"

    def __add__(self, other):
        return self.num_sides + other.num_sides, self.num_sides + other.num_sides

    def __str__(self): 
       return self.get_info()
        

##################        
class Circle(Shape): #Circle is the child class of Shape
    def __init__(self, num_sides, tesselates):
        super().__init__(num_sides, tesselates) #call superclass (Shape) and its initialiser function (call parameters in ())
    
    def get_num_sides(self):
        return self.num_sides
    
    def get_info(self): #overwrites get_info() in parent class
        if self.tesselates == "does tesselate":
            return f"This shape has {self.num_sides} sides and {self.tesselates}"
        else:
            return f"This shape has {self.num_sides} sides and {self.tesselates}"

class Triangle(Shape):
    def __init__(self, num_sides, tesselates):
        super().__init__(num_sides, tesselates)
    
    def get_info(self):
       if self.tesselates == "does tesselate":
            return f"This shape has {self.num_sides} sides and {self.tesselates}"
       else:
            return f"This shape has {self.num_sides} sides and {self.tesselates}"

class Square(Shape):
    def __init__(self, num_sides, tesselates):
        super().__init__(num_sides, tesselates)
    
    def get_info(self):
        if self.tesselates == "does tesselate":
            return f"This shape has {self.num_sides} sides and {self.tesselates}"
        else:
            return f"This shape has {self.num_sides} sides and {self.tesselates}"

class Pentagon(Shape):
    def __init__(self, num_sides, tesselates):
        super().__init__(num_sides, tesselates)
    
    def get_info(self):
        if self.tesselates == "yes":
            return f"This shape has {self.num_sides} sides and {self.does_tesselate}"
        else:
            return f"This shape has {self.num_sides} sides and {self.does_not_tesselate}"

class Hexagon(Shape):
    def __init__(self, num_sides, tesselates):
        super().__init__(num_sides, tesselates)
    
    def get_info(self):
        if self.tesselates == "yes":
            return f"This shape has {self.num_sides} sides and {self.does_tesselate}"
        else:
            return f"This shape has {self.num_sides} sides and {self.does_not_tesselate}"

class ManySidedPolygon(Shape):
    def __init__(self, num_sides, tesselates):
        super().__init__(num_sides, tesselates)
    
    def get_info(self):
        if self.tesselates == "yes":
            return f"This shape has {self.num_sides} sides and {self.does_tesselate}"
        else:
            return f"This shape has {self.num_sides} sides and {self.does_not_tesselate}"

if __name__ == '__main__':
    circle = Circle(1,"does not tesselate")
    print(circle) #__call__ method will be called
    print("New shape by adding circle + circle has ", circle.num_sides + circle.num_sides, "sides")

    triangle = Triangle(3, "does tesselate")
    print(triangle)


    '''NotImplementedError is derived from RuntimeError. 
    In user defined base classes, abstract methods should raise this exception when they require derived classes to override the method, 
    or while the class is being developed to indicate that the real implementation still needs to be added.'''