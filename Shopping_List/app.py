'''
This is a script that creates a shopping list
and returns information about that list to its user.
'''


# Initialize shopping list
shopping_list = []


# Functions
def show():
    print('Your list right now:')
    for item in shopping_list:

        if (item == 'SHOW' or item == 'DONE' or
                item == 'HELP' or item == 'REMOVE'):
            continue
        print(item)


def help():
    print('''
At the prompt ('>'), enter your item to add.
To show your list, type 'SHOW', 'REMOVE' to remove an item,
and to view this help message at any time, type 'HELP\'
''')


def remove_item():
    show()
    item_to_remove = input('Which item would you like to remove? ')
    shopping_list.remove(item_to_remove)
    print(item_to_remove, 'removed from your list.')

# Let user know how to use the script
print('To begin, simply type the name of the item you\'d like to add.')
print('Type \'HELP\' for information about this app, and type \'SHOW\'' +
      'to see the current state of your list. Enjoy!')
print('To quit, type \'DONE\'')

while True:
    # Get item
    if len(shopping_list) == 0:
        item_to_add = input('What would you like to add? ')
    else:
        item_to_add = input('> ')

    # Add item to list
    shopping_list.append(item_to_add)

    # Show help message to user
    if 'HELP' in shopping_list:
        help()
        shopping_list.remove('HELP')

    # Show current state of list
    if 'SHOW' in shopping_list:
        show()
        shopping_list.remove('SHOW')

    # Remove item(s)
    if 'REMOVE' in shopping_list:
        remove_item()
        shopping_list.remove('REMOVE')

    # Quit based on user input
    if 'DONE' in shopping_list:

        print('Your completed list:')

        for item in shopping_list:

            # Prevent DONE from printing
            if item == 'DONE':
                continue

            # Print itemized list
            print(item)

        break
