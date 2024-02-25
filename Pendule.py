position = 'right'
direction = 'left'

for i in range(1, 20, 1):
    if position == 'right':
        print('      <<')
        position = 'center'
        direction = 'left'

    elif position == 'center':
        print('   ^^')
        if direction == 'right':
            position = 'right'
        if direction == 'left':
            position = 'left'
    elif position == 'left':
        print('>>')
        position = 'center'
        direction = 'right'
