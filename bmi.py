weight = float(input('Enter your weight (Kg): '))
height = float(input('Enter your height (Meter): '))
bmi = round(weight / (height ** 2), 2)
minimum_weight = round(18.5 * (height ** 2), 2)
maximum_weight = round(25 * (height ** 2), 2)
print('BMI :', bmi)
if bmi < 18.5:
    print('Underweight!!')
    print('You should be between :', minimum_weight, 'and', maximum_weight)
if 18.5 <= bmi < 25:
    print('Good job! your weight is normal')
if bmi > 25:
    print('Overweight!!')
    print('You should be between :', minimum_weight, 'and', maximum_weight)
