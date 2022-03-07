cuboid = {"height" : 25/7, "width" : 25/2, "length": 35}
h = cuboid["height"]
w = cuboid ["width"]
l = cuboid ["length"]

cone = {"height" : 10, "base_radius" : 3}
h2 = cone["height"]
r = cone["base_radius"]

#cuboid volume = l x w x h
cuboid_v = l * w * h
#print(cuboid_v)
format_float_cv = "{:.2f}".format(cuboid_v)
#print(format_float_cv)

#cuboid surface area = 2(lw + lh + hw)
lw = l * w
lh = l * h
hw = h * w
cuboid_sa = 2*(lw + lh + hw)
#print(cuboid_sa)
format_float_csa = "{:.2f}".format(cuboid_sa) #round to 2dp
#print(format_float_csa)
print("The volume of cuboid is ", format_float_cv, "and the surface area is", format_float_csa)

#cone volume = pir^2h/3

import math
from re import A #import maths library
#print(math.pi) #print value of pi

cone_v = math.pi * r**2 * (h2/3)
#print(cone_v)
format_float_cov = "{:.2f}".format(cone_v)

#cone surface area = pi*r(r+sqrt(h^2+r^2))
cone_sa = math.pi * (r*(r + math.sqrt(h2**2 + r**2))) #sqrt returns square root of any number
#print(cone_sa)
format_float_cosa = "{:.2f}".format(cone_sa)

print("The volume of cone is ", format_float_cov, "and the surface area is", format_float_cosa)

##############
a = 5
#a +=1
#a +=a #equivalent to writing a = 2 * a
#a*=a #equivalent to writing a = a ** 2
#a/=a #answer is 1 but printed as 1.0
#a//=a #answer is printed as 1

print(a)

print("Hello World".split()) #returns a list
print("Hello"+"World")

#####
#str_test = "This Assessment Is Taking Forever"
#print(str_test.endswith("r")) #True
#print(str_test.startswith("t")) #False
#print(str_test.istitle()) #True
#print(str_test.isalpha()) #False
#print(str_test.replace(' ','').isalpha()) #True
#print("This" in str_test) #True

#print ("A">"a") #False
#print("Yes">"No") #True    