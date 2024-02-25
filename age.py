# برنامه چاپ رده سنی
age = int(input('Enter your age: '))
if 0 < age < 10:
    print('Child')
if 10 <= age < 20:
    print('Teenager')
if 20 <= age < 40:
    print('Young')
if 40 <= age < 150:
    print('Adult')
if age >= 150:
    print('Error')
