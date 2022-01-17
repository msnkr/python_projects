# height = float(input('What is your height?: '))
# weight = float(input('What is your weight?: '))

# bmi = float(weight / (height ** 2))

bmi = int(input('bmi '))

if bmi < 18.5:
    print(f'Your BMI is {round(bmi)}. You are slightly underweight. ')
elif bmi < 18.5 <= 25:
    print(f'Your BMI is {round(bmi)}. You have normal weight.')
elif bmi > 25 <= 30:
    print(f'Your BMI is {round(bmi)}. You are slightly overweight.')
elif bmi > 30 < 35:
    print(f'Your BMI is {round(bmi)}. You are obese.')
else:
    print(f'Your BMI is {round(bmi)}. You are clinically obese')
