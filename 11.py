space = 9
star = 1
for i in range(1, 20, 1):
    if i < 10 :
        print(space * ' ', '*' * star)
        star = star + 1
    elif i == 10:
        print('*' * 20)
    elif i > 10:
        space  = i - 11
        star = star - 1
        print(space * ' ', '*' * star)








