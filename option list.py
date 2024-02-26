option = 1
sm = 0
co = 0
while option != 0:
    print("1)Add")
    print("2)Sum")
    print("3)cont")
    print("4)Average")
    print("0)Exit")
    print('--------------------')
    option = int(input("Enter option: "))
    print('--------------------')
    match option:
    #اگر if و elif هایی داشه باشیم که مریوط به یک مغیر باشد و علامت عمه آنها == باشد میتوان از match case استفاده کنیم
        # Add
        case 1:
            x = int(input('Add Number: '))
            co = co + 1
            sm = sm + x
            print('Number Added')
        # sum
        case 2:
            print('Sum: ', sm)
        # cont
        case 3:
            print('cont: ', co)
        # Average
        case 4:
            avg = sm / co
            print('Average: ', avg)
        # Exit
        case 0:
            print('Goodbye!')
        # else
        case _:
            print('Invalid')
    print('--------------------')
