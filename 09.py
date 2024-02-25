space = 9
for i in range(1, 20, 2):
    print(' ' * space, '*' * i)
    space = space - 1
space = 1
for i in range(17, 0, -2):
    print(' ' * space, '*' * i)
    space = space + 1
