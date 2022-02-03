
#altitude = 90
#airspeed = 125

#altitude = 25000
#airspeed = 300

altitude = 50001
airspeed = 250

x = altitude
y = airspeed

#results of safe or unsafe flying
unsafe_flying = f"Unsafe flying - altitude is {x}ft and airspeed is {y}knots"
safe_flying = f"Safe flying - altitude is {x}ft and airspeed is {y}knots"

if x < 100 and y < 60 or x > 50000 and y > 5000:
    print(unsafe_flying)
elif x < 100 and y > 5000 | x > 50000 and y < 60:
    print (unsafe_flying)
elif x < 100 or x > 50000 or y < 60 or y > 5000:
    print (unsafe_flying)
else:
    print(safe_flying)