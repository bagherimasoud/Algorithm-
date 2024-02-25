# برنامه دریافت مجوز ساخت
length = float(input('Enter the length (Meter): '))
width = float(input('Enter the width (Meter): '))
area = round(length * width, 2)
print('The area of your land is:', area, 'Square meter')
if 0 < area <= 100:
    print('You can get license')
elif 100 < area:
    print("you can not get license")
