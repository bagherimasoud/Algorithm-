space = 8
star = 1
for i in range(1, 20, 1):
    if i < 10:
        print(space * ' ', '*' * star)
        space = space - 1
        star  = star + 1
    elif i == 10:
        print('*' * 20)
    elif i > 10:
        space = 9
        star = star - 1
        print(space * ' ', '*' * star)

