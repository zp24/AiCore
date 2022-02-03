
#convert input to float otherwise there wil be an error
height = float(input("please enter your height (m): "))
weight = float(input("please enter your weight (kg): "))

kg = weight
m = height
bmi = kg / m**2 #bmi formula - weight x height^2

format_float = float("{:.2f}".format(bmi))
#print(format_float)

x = format_float

if x < 18.5:
    print(f"Your BMI is {x}. You're in the underweight range.")
elif 18.5 < x < 24.9: #< x < means between numbers on either side
                      # can also use <= x <=
    print(f"Your BMI is {x}. You're in the healthy weight range")
elif 25  < x < 29:
    print(f"Your BMI is {x}. You're in the overweight range")
elif 30 < x < 39.9:
    print(f"You're BMI is {x}. You're in the obese range")
else:
    print("BMI not calculated")
