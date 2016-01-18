'''
This is a script that creates a shopping list
and returns information about that list to its user.
'''


# Initialize shopping list
shopping_list = []


# Functions
def clean_list():
    for item in shopping_list:
        if (item == 'SHOW' or item == 'DONE' or
                item == 'HELP' or item == 'REMOVE' or item == 'COUNT'):
            shopping_list.remove(item)


def show_list():
    clean_list()
    for item in shopping_list:
        print(item)


def get_help():
    print('''
At the prompt ('>'), enter your item to add.
To show your list, type 'SHOW', 'REMOVE' to remove an item,
'COUNT' to show the number of items in your list, and to view
this help message at any time, type 'HELP\'
''')


def remove_item():
    show_list()
    item_to_remove = input('Which item would you like to remove? ')
    try:
        shopping_list.remove(item_to_remove)
        print(item_to_remove, 'removed from your list.')
    except ValueError:
        print('Item not found.')


def get_item_count():
    clean_list()
    print('Your list has {} items'.format(len(shopping_list)))

# Let user know how to use the script
print('To begin, simply type the name of the item you\'d like to add.')
print('Type \'HELP\' for information about this app, and type \'SHOW\'' +
      ' to see the current state of your list. Enjoy!')
print('To quit, type \'DONE\'')

while True:
    # Get item
    if len(shopping_list) == 0:
        print('What would you like to add?')
        item_to_add = input('> ')
    else:
        item_to_add = input('> ')

    # Add item to list
    shopping_list.append(item_to_add)

    # Show help message to user
    if item_to_add == 'HELP':
        get_help()
        shopping_list.remove(item_to_add)
        continue
    # Show current state of list
    elif item_to_add == 'SHOW':
        print('Your current list:')
        show_list()
        continue
    # Remove item(s)
    elif item_to_add == 'REMOVE':
        remove_item()
        continue
    elif item_to_add == 'COUNT':
        get_item_count()
        continue
    # Quit based on user input
    elif item_to_add == 'DONE':
        print('Your completed list:')
        show_list()
        break
