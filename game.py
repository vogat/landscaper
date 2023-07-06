total = 0
day = 0

tools = [
    {
        'name': 'teeth',
        'owned': True,
        'equipped': True,
        'cost': 0,
        'income': 1
    },
    {
        'name': 'rusty scissors',
        'owned': False,
        'equipped': False,
        'cost': 5,
        'income': 5
    },
    {
        'name': 'push lawnmower',
        'owned': False,
        'equipped': False,
        'cost': 25,
        'income': 50
    },
    {
        'name': 'battery-powered lawnmower',
        'owned': False,
        'equipped': False,
        'cost': 250,
        'income': 100
    },
    {
        'name': 'starving students',
        'owned': False,
        'equipped': False,
        'cost': 500,
        'income': 250
    },
]


print('LANDSCAPER')
print('You start off with your teeth and make $1 a day.')
print('To win you need to own starving students and have $1000')
print()

def equip(idx):
    eq = int(input('Would you like to equip this item? (1 = Yes, 0 = No): '))
    while eq != 0 and eq != 1:
        eq = int(input('Invalid, please choose 1 or 0: '))
    if eq == 1:
        for tool in tools:
            tool['equipped'] = False
        tools[idx]['equipped'] = True

def userInput():
    choice = int(input('Enter 1 to cut grass, 2 to access the store, or 3 to access your inventory: '))
    return choice

def cut(total):
    for tool in tools:
        if tool['equipped'] == True:
            total = total + tool['income']
    return total

def store(total):
    print()
    for idx, tool in enumerate(tools):
        if tool['owned'] == False:
            print(f"{idx}| {tool['name']}, cost: {tool['cost']}")
    print('5| Exit')
    print()
    selection = int(input('Please enter your selection: '))

    while selection != 1 and selection != 2 and selection != 3 and selection != 4 and selection != 5:
        selection = int(input('Not a correct selection, please try again'))

    if selection != 5:
        if selection == 1:
            for idx, tool in enumerate(tools):
                if tool['name'] == 'rusty scissors':
                    if total >= tool['cost']:
                        tool['owned'] = True
                        total -= tool['cost']
                        equip(idx)
                        return total
                    else:
                        print('Not enough money!')
                        store(total)
        elif selection == 2:
            for idx, tool in enumerate(tools):
                if tool['name'] == 'push lawnmower':
                    if total >= tool['cost']:
                        tool['owned'] = True
                        total -= tool['cost']
                        equip(idx)
                        return total
                    else:
                        print('Not enough money!')
                        store(total)
        elif selection == 3:
            for idx, tool in enumerate(tools):
                if tool['name'] == 'battery-powered lawnmower':
                    if total >= tool['cost']:
                        tool['owned'] = True
                        total -= tool['cost']
                        equip(idx)
                        return total
                    else:
                        print()
                        print('Not enough money!')
                        store(total)
        elif selection == 4:
            for idx, tool in enumerate(tools):
                if tool['name'] == 'starving students':
                    if total >= tool['cost']:
                        tool['owned'] = True
                        total -= tool['cost']
                        equip(idx)
                        return total
                    else:
                        print('Not enough money!')
                        store(total)
        else:
            print('How did you get here?')
        


def inventory():
    print()
    for idx, tool in enumerate(tools):
        if tool['owned'] == True:
            print(f"{idx}| {tool['name']}")
    print('5| Exit')
    print()
    selection = int(input('Please enter your selection: '))

    while selection != 0 and selection != 1 and selection != 2 and selection != 3 and selection != 4 and selection != 5:
        selection = int(input('Not a correct selection, please try again: '))

    if selection != 5:
        if selection == 0:
            for idx, tool in enumerate(tools):
                if tool['name'] == 'teeth':
                        equip(idx)

        elif selection == 1:
            for idx, tool in enumerate(tools):
                if tool['name'] == 'rusty scissors':
                        equip(idx)

        elif selection == 2:
            for idx, tool in enumerate(tools):
                if tool['name'] == 'push lawnmower':
                    equip(idx)
        elif selection == 3:
            for idx, tool in enumerate(tools):
                if tool['name'] == 'battery-powered lawnmower':
                    equip(idx)
        elif selection == 4:
            for idx, tool in enumerate(tools):
                if tool['name'] == 'starving students':
                    equip(idx)
        else:
            print('How did you get here?')

def cont():
    for tool in tools:
        if tool['name'] == 'starving students' and tool['owned'] == False:
            return 1

c = cont()

while (c == 1 and total < 1000):
    choice = userInput()

    if choice == 1:
        total = cut(total)
        day += 1
        print()
        print(f'Total money: {total}     Day: {day}')
        print()
    elif choice == 2:
        store(total)
    elif choice == 3:
        inventory()
    else:
        while choice != 1 and choice != 2 and choice != 3:
            choice = int(input('Not a correct input, please try again: '))

print('Congratulations!')
print('You won!')