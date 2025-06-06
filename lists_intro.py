
#menu = [ ['Egg Sandwich', 'Bagel', 'Coffee',
#          'BLT', 'PB&J', 'Turkey & Cheese Sandwich',
#          'Tea', 'Ceasar Salad', 'Taco']]

#print(menu[0][7])

menus = { 'Breakfast' : ['Egg Sandwich', 'Bagel', 'Coffee'],
          'Lunch' : ['BLT', 'PB&J', 'Turkey & Cheese Sandwich'],
          'Dinner' : ['Ceasar Salad', 'Spaghetti', 'Taco']}

#print('Breakfast Menu:\t' , menus['Breakfast'])
#print('Lunch Menu:\t' , menus['Lunch'])
#print('Dinner Menu:\t' , menus['Dinner'])

#for meal, items in menus.items():
#    print(meal + ' Menu:\t', items)

for name, menu in menus.items():
    print(name, ' : ', menu)
