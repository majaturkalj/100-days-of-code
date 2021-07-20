# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
number_height = float(height)
number_weight = float(weight)
BMI = round(number_weight / (number_height * number_height),2)

if BMI < 18.5:
    print (f"Your BMI is {BMI}, you are underweight.")
elif BMI > 18.5 and BMI < 25:
    print(f"Your BMI is {BMI}, you have normal weight.")    
elif BMI > 25 and BMI < 30:
    print (f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI > 30 and BMI < 35:
    print (f"Your BMI is {BMI}, you are obese.")
else:
    print (f"Your BMI is {BMI}, you are clinically obese.")