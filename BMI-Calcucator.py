name = input ("Enter your name: ")
weight = int(input("Enter your weight in pounds: "))
height = int(input("Enter your height in inches: "))
BMI = round((weight * 703) /(height ** 2),2)
print(BMI)
if(BMI > 0 ):
    if (BMI >= 40):
        print(f'{BMI} is Morbidly Obese.')
    elif (BMI >= 35 and BMI <= 39.9):
        print(f'{BMI} is Severely Obese.')
    elif (BMI>= 30 and BMI <=34.9):
        print(f'{BMI} is Obese.')
    elif (BMI>= 25 and BMI <= 29.9):
        print(f'{BMI} is Overweight.')
    elif (BMI>= 18.5 and BMI <=24.9):
        print(f'{BMI} is Normal Weight.')
    else:
        print(f'{BMI} is Underweight.') 
else:
    print('Enter valid input') 