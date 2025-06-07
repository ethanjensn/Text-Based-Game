# dictionary of rooms
rooms = {
        'Living Room': {'South': 'Basement', 'East': 'Bathroom', 'North': 'Bedrooms', 'West': 'Kitchen'},
        'Kitchen': {'East': 'Living Room', 'item': 'Beans'},
        'Bedrooms': {'South': 'Living Room', 'East': 'Attic', 'item': 'Water'},
        'Attic': {'West': 'Bedrooms', 'item': 'Zombie'},
        'Bathroom': {'West': 'Living Room', 'North': 'Laundry Room', 'item': 'Bandages'},
        'Laundry Room': {'South': 'Bathroom', 'item': 'Soap'},
        'Basement': {'North': 'Living Room', 'East': 'Hidden Room', 'item': 'Bat'},
        'Hidden Room': {'West': 'Basement', 'item': 'Gun'},
    }

def show_instructions():#shows instructions
   #print a main menu and the commands
   print("Dragon Text Adventure Game")
   print("Collect 6 items to win the game, or be eaten by the dragon.")
   print("Move commands: go South, go North, go East, go West")
   print("Add to Inventory: get 'item name'")

show_instructions()

inventory = []

current_room = 'Living Room'
print('You are currently in', current_room)


while True: #loop forever(game loop)
    where_to = input('Enter your move').split(' ') #get input

    if len(where_to) != 2 or where_to[0] != 'go':#if input is not the length of 2 words or does not have go, its invalid
        print("Invalid input, use 'go'")
        continue

    direction = where_to[1] #makes index a variable

    if direction in rooms[current_room]:#look through dict to see if move is in key:value pair
        current_room = rooms[current_room][direction]

        if current_room == 'Attic': #if in attic, game ends
            print('You Died to a Zombie!')
            exit()

        if 'item' in rooms[current_room]: #if items in the current room, add or don't add to inventory
            current_item = rooms[current_room]['item']
            if current_item not in inventory:
                print('You see {}'.format(current_item))
                get_item = input("Enter your move (e.g., 'get Beans'): ").split(' ')

                if (len(get_item) == 2 and get_item[0].lower() == 'get'
                    and get_item[1] == current_item):
                    inventory.append(current_item)
                    print(f"{current_item} added to inventory!")

                elif (len(get_item) != 2 or get_item[0].lower() != 'get'
                    or get_item[1] == current_item):
                    print('Can not find {}'.format(get_item[1]))
                    continue


    print('Inventory is', inventory) #print what we have so far
    print('-'*20)
    print('You are in the', current_room)

    if len(inventory) == 6:#if the list adds up to all the items, you win
        print('You Won!! You found all of the items without finding the Zombie.')
        exit()
