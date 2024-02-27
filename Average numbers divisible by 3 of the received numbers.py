sm = 0
count = 0
while True:
    number = int(input('Enter Number: '))
    if number == 0:
        break
    if number % 3 == 0:
        sm = sm + number
        count = count + 1
print('-------------------')
average = sm / count
print('Average =', average)
