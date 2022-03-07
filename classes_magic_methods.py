import math

#Vector class
class Vector:
    def __init__(self, vector1, vector2):
        #self.vector1, self.vector2 = vector1, vector2 #can declare them at the same time
        self.vector1 = vector1
        #vector1 = [] #first vector instance

        self.vector2 = vector2
        #vector2 = []
        self.coords = [vector1, vector2]

    def __repr__(self): #convert data to string
        #need 2 pairs of () for this to work
        return repr((self.vector1, self.vector2))

    def __add__(self, other): #Equivalent of + operation
        #need to include other for each variable/vector otherwise it will not work
        return Vector(self.vector1 + other.vector1, self.vector2 + other.vector2)

    def __neg__(self):
        #Negation of the vector (invert through origin.)
        return Vector(-self.vector1, -self.vector2)

    #def __getitem__(self, i):
       # return Vector(self.vector1[i], self.vector2[i])
    
    def __getitem__(self, n):
        #index vectors
        #return Vector(self.coords[n],[n])
        return self.coords[n]
    
    #def __iter__(self, i):
     #   return Vector(self.vector1[i], self.vector2[i])
    #def __index__(self, n):
     #   return (self.coords(n))
    
    def __pow__(self, other):
        return (self.vector1 ** other)

    def __lt__(self, other):
        if isinstance(other, square_root):
            return (self.vector1 ** other + self.vector1 ** other > self.vector2 ** other + self.vector2 ** other,
            self.vector2 ** other + self.vector2 ** other > self.vector1 ** other + self.vector1 ** other)
        else:
            return False   
    
#declare all the methods in the class THEN declare variables and call methods - makes it easier
if __name__ == '__main__':
    vector1 = Vector(2, 4)
    vector2 = Vector(3, 5)
    test_vector = [vector1, vector2]


print("vector1: ", vector1)
print('-vector1 (invert vector1): ', -vector1)
print('add vectors together:', vector1 + vector2)
print('double vector1:', vector1 + vector1)

print(type(vector1))
print(type(vector2))
print(test_vector[0]) #(2,4)
print(test_vector[0][1]) #(4, [1])
print(test_vector[1]) #(3,5)
print(test_vector[1][1]) #(5, [1])
print("Power of vector1:", (vector1[0]**2, vector1[1]**2))
print("Power of vector2: ", (vector2[0]**2, vector2[1]**2))
print("Power of test_vector: ", (test_vector[0][0]**2, test_vector[0][1] **2))
#print("test pythag theorem for vector1: ", math.sqrt(vector1[0]**2 + vector1[1]**2))
#print("test pythag theorem for vector2: ", math.sqrt(vector2[0]**2 + vector2[1]**2))

a = vector1[0]
b = vector1[1]
c = math.sqrt(a ** 2 + b ** 2)
c = "{:.2f}".format(c)
print("Vector1 pythagoras theorem: ", c) #4.47

a1 = vector2[0]
b1 = vector2[1]
c1 = math.sqrt(a1 ** 2 + b1 ** 2)
c1 = "{:.2f}".format(c1)
print("Vector2 pythagoras theorem: ", c1) #5.83

print(c1 > c)
'''if c > c1:
    print(f"{c} of vector1 is bigger than {c1} of vector2")
else:
    print(f"{c1} of vector2 is bigger than {c} of vector1")
'''    