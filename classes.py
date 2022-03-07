import math

#Cylinder class
class Cylinder:
    
    #class constructor
    def __init__(self, height = 1, radius = 1):
        #attributes
        self.height = height
        self.radius = radius
        
        self.surface_area = None
        self.volume = None
    
    #methods
    def get_surface_area(self):
    #surface area = 2πrh+2πr^2
        surface_area = (2 * math.pi * self.radius * self.height) + (2 * math.pi * self.radius **2)
        surface_area = float("{:.2f}".format(surface_area)) #round to 2dp
        return surface_area
    
    def get_volume(self): 
    #volume = πr^2h
        volume = math.pi * (self.radius **2) * self.height
        volume = float("{:.2f}".format(volume)) #round to 2dp
        return volume 

cyl1 = Cylinder() #call class - no need to define parameter values if already defined
print("Surface area ", cyl1.get_surface_area())
print("Volume: ", cyl1.get_volume())

#########

#Car class
class Car:
    def __init__(self, model, year = 2022):
        self.model = model
        #model = "Tesla"

        self.year = year
        #year = 2022

        self.miles_driven = 0
        #miles_driven = 0

    def drive(self):
           #print("Vroom")
            #add to the miles_driven until it reaches 1000 - too restrictive for the end user
            ''' for miles in range(1001):
             if miles < 1000:
                self.miles_driven +=1
                print("Miles driven: ", self.miles_driven)
                continue
             else:
                print("Broken!")
                break'''
            #add a limit but do not make it restrictive
            if self.miles_driven >= 10:
                print ("Broken")
            else:
                print ("Vroom!")
                self.miles_driven +=1

            
    def info(self):
            print("Miles driven: ", self.miles_driven,  ", Model: ", self.model, ", Year: ", self.year)


carClass = Car(model = "Tesla")

for miles in range(20): #add a range outside of the class to prevent restrictions earlier in the code
    print(carClass.drive())

print(carClass.drive(), carClass.info())

####
'''
#Vector class
class Vector:
    def __init__(self, vector_list):
        self.vector_list = vector_list
        vector_list = []

        #self.v1 = v1
        #self.v2 = v2


    def __add__(self, other): #Equivalent of + operation
    #v3 = [v + v1 for v, v1 in zip(self.v + self.v1)]
    #print (v3)
        v4 = self.v1.__repr__() + self.v2.__repr__()
        return v3

vClass = Vector

v1 = Vector(2)
print("Vector 1: ", v1.__repr__()) #special method used to represent a class’s objects as a string
#need to add __repr__() otherwise memory address of object will be printed

v2 = Vector(1)
print("Vector 2: ", v2.__repr__())

v3 = v1 + v2 # adds the two vectors together into one
print("Vector 3: ", v3.__repr__())

print(vClass) #<class '__main__.Vector'>
print (v1 + v2)
'''