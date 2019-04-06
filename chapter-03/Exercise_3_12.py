# Exercise 3.12

weight = input("Please enter your weight(kg): ")
height = input("Please enter your height(m): ")
BMI = float(weight) / height ** 2
if BMI < 19:
    comment = "Too thin!"
elif BMI >= 19 and BMI < 25:
    comment = "Normal!"
elif BMI >= 25 and BMI < 28:
    comment = "Overweight!"
else:
    comment = "Obesity!"
print "Your BMI Quantity is", str(BMI) + ",", comment

