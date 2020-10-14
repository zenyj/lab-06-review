import sys
print("BMI:Body Mass Index Calculator")
userweight = input("Enter your weight (in pounds):")
userheight = input("Enter your height (in inches):")

bmi= (703 * float(userweight)) / (float(userheight) * float(userheight))
print("Your body mass index (BMI) is: " + str(bmi) + "%")