# Ultimate Battleships

def print_ships_to_be_placed():
    print("Ships to be placed:", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Ships to be placed: ")


# elem expected to be a single list element of a primitive type.
def print_single_element(elem):
    print(str(elem), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write(str(elem) + " ")


def print_empty_line():
    print()
    if FILE_OUTPUT_FLAG:
        f.write("\n")


# n expected to be str or int.
def print_player_turn_to_place(n):
    print("It is Player {}'s turn to place their ships.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to place their ships.\n".format(n))


def print_to_place_ships():
    print("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) : \n")
        # There is a \n because we want the board to start printing on the next line.


def print_incorrect_input_format():
    print("Input is in incorrect format, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Input is in incorrect format, please try again.\n")


def print_incorrect_coordinates():
    print("Incorrect coordinates given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect coordinates given, please try again.\n")


def print_incorrect_ship_name():
    print("Incorrect ship name given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect ship name given, please try again.\n")


def print_incorrect_orientation():
    print("Incorrect orientation given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect orientation given, please try again.\n")


# ship expected to be str.
def print_ship_is_already_placed(ship):
    print(ship, "is already placed, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " is already placed, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_outside(ship):
    print(ship, "cannot be placed outside the board, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed outside the board, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_occupied(ship):
    print(ship, "cannot be placed to an already occupied space, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed to an already occupied space, please try again.\n")


def print_confirm_placement():
    print("Confirm placement Y/N :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Confirm placement Y/N : \n")


# n expected to be str or int.
def print_player_turn_to_strike(n):
    print("It is Player {}'s turn to strike.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to strike.\n".format(n))


def print_choose_target_coordinates():
    print("Choose target coordinates :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Choose target coordinates : ")


def print_miss():
    print("Miss.")
    if FILE_OUTPUT_FLAG:
        f.write("Miss.\n")


# n expected to be str or int.
def print_type_done_to_yield(n):
    print("Type done to yield your turn to player {} :".format(n), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Type done to yield your turn to player {} : \n".format(n))


def print_tile_already_struck():
    print("That tile has already been struck. Choose another target.")
    if FILE_OUTPUT_FLAG:
        f.write("That tile has already been struck. Choose another target.\n")


def print_hit():
    print("Hit!")
    if FILE_OUTPUT_FLAG:
        f.write("Hit!\n")


# n expected to be str or int.
def print_player_won(n):
    print("Player {} has won!".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("Player {} has won!\n".format(n))


def print_thanks_for_playing():
    print("Thanks for playing.")
    if FILE_OUTPUT_FLAG:
        f.write("Thanks for playing.\n")


# my_list expected to be a 3-dimensional list, formed from two 2-dimensional lists containing the boards of each player.
def print_3d_list(my_list):
    first_d = len(my_list[0])
    for row_ind in range(first_d):
        second_d = len(my_list[0][row_ind])
        print("{:<2}".format(row_ind + 1), end=' ')
        for col_ind in range(second_d):
            print(my_list[0][row_ind][col_ind], end=' ')
        print("\t\t\t", end='')
        print("{:<2}".format(row_ind + 1), end=' ')
        for col_ind in range(second_d):
            print(my_list[1][row_ind][col_ind], end=' ')
        print()
    print("", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\t\t", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\nPlayer 1\t\t\t\t\t\tPlayer 2")
    print()

    if FILE_OUTPUT_FLAG:
        first_d = len(my_list[0])
        for row_ind in range(first_d):
            second_d = len(my_list[0][row_ind])
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[0][row_ind][col_ind] + " ")
            f.write("\t\t\t")
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[1][row_ind][col_ind] + " ")
            f.write("\n")
        f.write("   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\t\t   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\nPlayer 1\t\t\t\t\t\tPlayer 2\n")
        f.write("\n")


def print_rules():
    print("Welcome to Ultimate Battleships")
    print("This is a game for 2 people, to be played on two 10x10 boards.")
    print(
        "There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).")
    print(
        "First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.")
    print(
        "Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.")
    print("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.")
    print("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.")
    print(
        "Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.")
    print("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.")
    print("The last player to have an unsunk ship wins.")
    print("Have fun!")
    print()

    if FILE_OUTPUT_FLAG:
        f.write("Welcome to Ultimate Battleships\n")
        f.write("This is a game for 2 people, to be played on two 10x10 boards.\n")
        f.write(
            "There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).\n")
        f.write(
            "First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.\n")
        f.write(
            "Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.\n")
        f.write(
            "If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.\n")
        f.write(
            "If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.\n")
        f.write(
            "Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.\n")
        f.write("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.\n")
        f.write("The last player to have an unsunk ship wins.\n")
        f.write("Have fun!\n")
        f.write("\n")


# Create the game
board_size = 10
f = open('UltimateBattleships.txt', 'w')
FILE_OUTPUT_FLAG = True  # You can change this to True to also output to a file so that you can check your outputs with diff.

print_rules()

# Remember to use list comprehensions at all possible times.
# If we see you populate a list that could be done with list comprehensions using for loops, append/extend/insert etc. you will lose points.

# Make sure to put comments in your code explaining your approach and the execution.

# We defined all the functions above for your use so that you can focus only on your code and not the formatting.
# You need to call them in your code to use them of course.

# If you have questions related to this homework, direct them to utku.bozdogan@boun.edu.tr please.

# Do not wait until the last day or two to start doing this homework, it requires serious effort.

try:  # The entire code is in this try block, if there ever is an error during execution, we can safely close the file.
    # DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

    placement_phase = True
    placement_phase_2 = True
    player_1_list = None
    player_2_list = None
    # I use while loop to initialize placement phase
    while placement_phase:
        # First I define lists by using list comprehension and print a blank list
        blank_list = [[["-" for i in range(board_size)] for j in range(board_size)] for k in range(board_size)]
        print_3d_list(blank_list)
        player_1_list = [[["-" for i in range(board_size)] for j in range(board_size)] for k in range(board_size)]
        # Defining ships as a list and lowercase ship names in another list
        list_of_ships = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
        list_of_ships_2 = [k.lower() for k in list_of_ships]
        # I check errors and place ships using another while loop
        input_phase = True
        while input_phase:
            # Using a dictionary to define length of ships
            dict_of_ships = {"carrier": 5, "battleship": 4, "cruiser": 3, "submarine": 3, "destroyer": 2}
            # Printing list of ships and which player's turn
            n = 1
            print_ships_to_be_placed()
            for ship in list_of_ships:
                print_single_element(ship)
            print_empty_line()
            print_player_turn_to_place(n)
            print_to_place_ships()
            # Taking input from the user to define ship and ship's place
            # Using lower to make input case insensitive and strip to avoid any space in input
            ship_input = input().lower().strip()
            # Listing input strings
            input_list = ship_input.split()
            # When input list doesn't contain enough number of input and coordinates aren't integers, printing input format error
            if len(input_list) < 4:
                print_incorrect_input_format()
                print_3d_list(player_1_list)
                continue
            try:
                int(input_list[1])
                int(input_list[2])
            except:
                print_incorrect_input_format()
                print_3d_list(player_1_list)
                continue
            # When coordinates aren't in board, printing coordinate error
            if int(input_list[1]) > 10 or int(input_list[1]) < 1 or int(input_list[2]) > 10 or int(input_list[2]) < 1:
                print_incorrect_coordinates()
                print_3d_list(player_1_list)
                continue
            # Defining a variable to remove used ships from the list of remaining ships
            x = input_list[0]
            if x == "carrier":
                x = "Carrier"
            if x == "battleship":
                x = "Battleship"
            if x == "cruiser":
                x = "Cruiser"
            if x == "submarine":
                x = "Submarine"
            if x == "destroyer":
                x = "Destroyer"
            # Checking ship name and when the first word of input not a ship name, printing ship name error
            if input_list[0] != "carrier":
                if input_list[0] != "battleship":
                    if input_list[0] != "submarine":
                        if input_list[0] != "cruiser":
                            if input_list[0] != "destroyer":
                                print_incorrect_ship_name()
                                print_3d_list(player_1_list)
                                continue
            # When orientation of the ship is wrong, printing orientation error
            if input_list[3] != "h":
                if input_list[3] != "v":
                    print_incorrect_orientation()
                    print_3d_list(player_1_list)
                    continue
            # When a ship is placed and user want to place it again, printing ship is already placed error
            if input_list[0] not in list_of_ships_2:
                if input_list[0] == "carrier" or "battleship" or "submarine" or "cruiser" or "destroyer":
                    ship = x
                    print_ship_is_already_placed(ship)
                    print_3d_list(player_1_list)
                    continue

            count = 0
            if input_list[0] in list_of_ships_2:
                # To place a ship horizontally, using an if
                if input_list[3] == "h":
                    # When a part of ship is outside the board, printing ship can not be placed outside
                    if dict_of_ships[input_list[0]] + int(input_list[1]) > 11:
                        ship = x
                        print_ship_cannot_be_placed_outside(ship)
                        print_3d_list(player_1_list)
                        continue
                    # To determine if a part of ship to be placed overlaps any of the placed ships I use a for loop
                    # When it overlaps count is not 0 and then the program can print error
                    for blank in range(dict_of_ships[input_list[0]]):
                        if player_1_list[0][int(input_list[2]) - 1][int(input_list[1]) - 1 + blank] == "#":
                            count += 1
                    # If it overlaps, printing ship cannot be placed occupied
                    if count > 0:
                        ship = x
                        print_ship_cannot_be_placed_occupied(ship)
                        print_3d_list(player_1_list)
                        continue
                    # If it doesn't overlap, placing the ship to the given coordinates by changing the list of player 1
                    # When the change in player 1's board I change 0th index of list of board, when it is in player 2's list I change 1st index
                    # And according to the orientation of ship I change different parts of list.
                    if count == 0:
                        for blank in range(dict_of_ships[input_list[0]]):
                            player_1_list[0][int(input_list[2]) - 1][int(input_list[1]) - 1 + blank] = "#"
                        # And removing placed ships from the ship lists
                        list_of_ships_2.remove(input_list[0])
                        list_of_ships.remove(x)

                # To place a ship vertically, using an if
                if input_list[3] == "v":
                    # When a part of ship is outside the board, printing ship can not be placed outside
                    if dict_of_ships[input_list[0]] + int(input_list[2]) > 11:
                        ship = x
                        print_ship_cannot_be_placed_outside(ship)
                        print_3d_list(player_1_list)
                        continue
                    # To determine if a part of ship to be placed overlaps any of the placed ships, using a for loop
                    for blank in range(dict_of_ships[input_list[0]]):
                        if player_1_list[0][int(input_list[2]) - 1 + blank][int(input_list[1]) - 1] == "#":
                            count += 1
                    # If it overlaps, printing ship cannot be placed occupied
                    if count > 0:
                        ship = x
                        print_ship_cannot_be_placed_occupied(ship)
                        print_3d_list(player_1_list)
                        continue
                    # If it doesn't overlap, placing the ship to the given coordinates by changing the list of player 1
                    if count == 0:
                        for blank in range(dict_of_ships[input_list[0]]):
                            player_1_list[0][int(input_list[2]) - 1 + blank][int(input_list[1]) - 1] = "#"
                        # And removing placed ships from the ship lists
                        list_of_ships_2.remove(input_list[0])
                        list_of_ships.remove(x)

            print_3d_list(player_1_list)
            # When all ships are placed while loop turns false
            if len(list_of_ships) == 0:
                input_phase = False
        # Using another while to confirmation
        confirmation_1 = True
        while confirmation_1:
            print_confirm_placement()
            conf = input().lower().strip()
            # When confirmation input not in correct form, asking again until it becomes correct form
            if conf != "n":
                if conf != "y":
                    pass
            # If user wants to place again the program returns to top of the while loop
            if conf == "n":
                confirmation_1 = False
            # If user confirms placement second user can start placement
            if conf == "y":
                confirmation_1 = False
                # I use while loop to initialize placement phase of second user
                while placement_phase_2:
                    # Defining second player list and printing it
                    blank_list = [[["-" for i in range(board_size)] for j in range(board_size)] for k in range(board_size)]
                    print_3d_list(blank_list)
                    player_2_list = [[["-" for i in range(board_size)] for j in range(board_size)] for k in range(board_size)]
                    # Defining second user's list of ships
                    list_of_ships = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
                    list_of_ships_2 = [k.lower() for k in list_of_ships]

                    input_phase_2 = True
                    # I check errors and place ships using another while loop
                    while input_phase_2:
                        # Again defining length of ships
                        dict_of_ships = {"carrier": 5, "battleship": 4, "cruiser": 3, "submarine": 3, "destroyer": 2}
                        # Printing list of ships and which player's turn
                        n = 2
                        print_ships_to_be_placed()
                        for ship in list_of_ships:
                            print_single_element(ship)
                        print_empty_line()
                        print_player_turn_to_place(n)
                        print_to_place_ships()
                        # Taking input from the user to define ship and ship's place
                        # Using lower to make input case insensitive and strip to avoid any space in input
                        ship_input = input().lower().strip()
                        # Listing input strings
                        input_list = ship_input.split()
                        # When input list doesn't contain enough number of input and coordinates aren't integers, printing input format error
                        if len(input_list) < 4:
                            print_incorrect_input_format()
                            print_3d_list(player_2_list)
                            continue
                        try:
                            int(input_list[1])
                            int(input_list[2])
                        except:
                            print_incorrect_input_format()
                            print_3d_list(player_2_list)
                            continue
                        # When coordinates aren't in board, printing coordinate error
                        if int(input_list[1]) > 10 or int(input_list[1]) < 1 or int(input_list[2]) > 10 or int(input_list[2]) < 1:
                            print_incorrect_coordinates()
                            print_3d_list(player_2_list)
                            continue
                        # Defining a variable to remove used ships from the second user's list of remaining ships
                        x = input_list[0]
                        if x == "carrier":
                            x = "Carrier"
                        if x == "battleship":
                            x = "Battleship"
                        if x == "cruiser":
                            x = "Cruiser"
                        if x == "submarine":
                            x = "Submarine"
                        if x == "destroyer":
                            x = "Destroyer"
                        # Checking ship name and when the first word of input not a ship name, printing ship name error
                        if input_list[0] != "carrier":
                            if input_list[0] != "battleship":
                                if input_list[0] != "submarine":
                                    if input_list[0] != "cruiser":
                                        if input_list[0] != "destroyer":
                                            print_incorrect_ship_name()
                                            print_3d_list(player_2_list)
                                            continue
                        # When orientation of the ship is wrong, printing orientation error
                        if input_list[3] != "h":
                            if input_list[3] != "v":
                                print_incorrect_orientation()
                                print_3d_list(player_2_list)
                                continue
                        # When a ship is placed and user want to place it again, printing ship is already placed error
                        if input_list[0] not in list_of_ships_2:
                            if input_list[0] == "carrier" or "battleship" or "submarine" or "cruiser" or "destroyer":
                                ship = x
                                print_ship_is_already_placed(ship)
                                print_3d_list(player_2_list)
                                continue

                        count = 0
                        if input_list[0] in list_of_ships_2:
                            # To place a ship horizontally, using an if
                            if input_list[3] == "h":
                                # When a part of ship is outside the board, printing ship can not be placed outside
                                if dict_of_ships[input_list[0]] + int(input_list[1]) > 11:
                                    ship = x
                                    print_ship_cannot_be_placed_outside(ship)
                                    print_3d_list(player_2_list)
                                    continue
                                # To determine if a part of ship to be placed overlaps any of the placed ships, using a for loop
                                for blank in range(dict_of_ships[input_list[0]]):
                                    if player_2_list[1][int(input_list[2]) - 1][int(input_list[1]) - 1 + blank] == "#":
                                        count += 1
                                # If it overlaps, printing ship cannot be placed occupied
                                if count > 0:
                                    ship = x
                                    print_ship_cannot_be_placed_occupied(ship)
                                    print_3d_list(player_2_list)
                                    continue
                                # If it doesn't overlap, placing the ship to the given coordinates by changing the list of player 2
                                if count == 0:
                                    for blank in range(dict_of_ships[input_list[0]]):
                                        player_2_list[1][int(input_list[2]) - 1][int(input_list[1]) - 1 + blank] = "#"
                                    list_of_ships_2.remove(input_list[0])
                                    list_of_ships.remove(x)

                            if input_list[3] == "v":
                                # To place a ship vertically, using an if
                                if dict_of_ships[input_list[0]] + int(input_list[2]) > 11:
                                    ship = x
                                    print_ship_cannot_be_placed_outside(ship)
                                    print_3d_list(player_2_list)
                                    continue
                                # To determine if a part of ship to be placed overlaps any of the placed ships, using a for loop
                                for blank in range(dict_of_ships[input_list[0]]):
                                    if player_2_list[1][int(input_list[2]) - 1 + blank][int(input_list[1]) - 1] == "#":
                                        count += 1
                                # If it overlaps, printing ship cannot be placed occupied
                                if count > 0:
                                    ship = x
                                    print_ship_cannot_be_placed_occupied(ship)
                                    print_3d_list(player_2_list)
                                    continue
                                # If it doesn't overlap, placing the ship to the given coordinates by changing the list of player 2
                                if count == 0:
                                    for blank in range(dict_of_ships[input_list[0]]):
                                        player_2_list[1][int(input_list[2]) - 1 + blank][int(input_list[1]) - 1] = "#"
                                    list_of_ships_2.remove(input_list[0])
                                    list_of_ships.remove(x)


                        print_3d_list(player_2_list)
                        # When all ships are placed while loop turns false
                        if len(list_of_ships) == 0:
                            input_phase_2 = False
                    # Using another while to confirmation
                    confirmation_2 = True
                    while confirmation_2:
                        print_confirm_placement()
                        conf = input().lower().strip()
                        # When confirmation input not in correct form, asking again until it becomes correct form
                        if conf != "y":
                            if conf != "n":
                                pass
                        # If user wants to place again the program returns to top of the while
                        if conf == "n":
                            confirmation_2 = False
                        # If second user confirms placement all while loops are closed and battle phase starts
                        if conf == "y":
                            placement_phase_2 = False
                            placement_phase = False
                            confirmation_2 = False

    # Another while loop for the battle phase
    battle_phase = True
    # Using counts to finish the game when all ships are hit
    count_of_1_hit = 0
    count_of_2_hit = 0
    while battle_phase:

        target_1 = True
        target_2 = False
        # Another while for player 1's strike
        while target_1:
            print_3d_list(player_1_list)
            n = 1
            print_player_turn_to_strike(n)
            print_choose_target_coordinates()
            # Taking strike coordinates from the user and striping the input to avoid space problems
            target_coor = input().strip()
            target_list = list(target_coor.split())
            # When coordinates aren't in correct format, printing input format error
            if len(target_list) < 2:
                print_incorrect_input_format()
                continue
            try:
                int(target_list[0])
                int(target_list[1])
            except:
                print_incorrect_input_format()
                continue
            # When coordinates aren't in board, printing coordinate error
            if int(target_list[0]) > 10 or int(target_list[0]) < 1 or int(target_list[1]) > 10 or int(target_list[1]) < 1:
                print_incorrect_coordinates()
                continue
            # When coordinates are already given before this turn, printing tile already struck
            if player_2_list[1][int(target_list[1]) - 1][int(target_list[0]) - 1] == "!":
                print_tile_already_struck()
                continue
            if player_2_list[1][int(target_list[1]) - 1][int(target_list[0]) - 1] == "O":
                print_tile_already_struck()
                continue
            # If the first time to strike a tile I change the player 1's list according to hit or miss
            if player_2_list[1][int(target_list[1]) - 1][int(target_list[0]) - 1] == "#":
                player_1_list[1][int(target_list[1]) - 1][int(target_list[0]) - 1] = "!"
                # Player 2's list should also change to see where the player 1 attacked
                player_2_list[1][int(target_list[1]) - 1][int(target_list[0]) - 1] = "!"

                print_hit()
                count_of_1_hit += 1
                # When a player hit the ships 17 times (because all ships have 17 length) the game finishes
                if count_of_1_hit == 17:
                    print_3d_list(player_1_list)
                    print_player_won(n)
                    battle_phase = False
                    break
                else:
                    continue
            # When a tile that doesn't have a part of ships it converts into O
            if player_2_list[1][int(target_list[1]) - 1][int(target_list[0]) - 1] == "-":
                player_1_list[1][int(target_list[1]) - 1][int(target_list[0]) - 1] = "O"
                # Player 2's list also changes
                player_2_list[1][int(target_list[1]) - 1][int(target_list[0]) - 1] = "O"

                print_miss()
                n = 2
                # If a player miss the shot, asking to write done to player
                done = True
                while done:
                    print_type_done_to_yield(n)
                    type_done = input().lower().strip()
                    if type_done != "done":
                        pass
                    if type_done == "done":
                        done = False
                target_1 = False
                target_2 = True
        # Another while for player 2's strike
        while target_2:
            print_3d_list(player_2_list)
            n = 2
            print_player_turn_to_strike(n)
            print_choose_target_coordinates()
            # Taking strike coordinates from the user and striping the input to avoid space problems
            target_coor = input().strip()
            target_list = list(target_coor.split())
            # When coordinates aren't in correct format, printing input format error
            if len(target_list) < 2:
                print_incorrect_input_format()
                continue
            try:
                int(target_list[0])
                int(target_list[1])
            except:
                print_incorrect_input_format()
                continue
            # When coordinates aren't in board, printing coordinate error
            if int(target_list[0]) > 10 or int(target_list[0]) < 1 or int(target_list[1]) > 10 or int(target_list[1]) < 1:
                print_incorrect_coordinates()
                continue
            # When coordinates are already given before this turn, printing tile already struck
            if player_1_list[0][int(target_list[1]) - 1][int(target_list[0]) - 1] == "!":
                print_tile_already_struck()
                continue
            if player_1_list[0][int(target_list[1]) - 1][int(target_list[0]) - 1] == "O":
                print_tile_already_struck()
                continue
            # If the first time to strike a tile I change the player 2's list according to hit or miss
            if player_1_list[0][int(target_list[1]) - 1][int(target_list[0]) - 1] == "#":
                player_2_list[0][int(target_list[1]) - 1][int(target_list[0]) - 1] = "!"
                # Player 1 list also changes
                player_1_list[0][int(target_list[1]) - 1][int(target_list[0]) - 1] = "!"

                print_hit()
                count_of_2_hit += 1
                # When a player hit the ships 17 times (because all ships have 17 length) the game finishes
                if count_of_2_hit == 17:
                    print_3d_list(player_2_list)
                    print_player_won(n)
                    battle_phase = False
                    break
                else:
                    continue
            # When a tile that doesn't have a part of ships it converts into O
            if player_1_list[0][int(target_list[1]) - 1][int(target_list[0]) - 1] == "-":
                player_2_list[0][int(target_list[1]) - 1][int(target_list[0]) - 1] = "O"
                # Player 1 list also changes
                player_1_list[0][int(target_list[1]) - 1][int(target_list[0]) - 1] = "O"

                print_miss()
                n = 1
                # If a player miss the shot, asking to write done to player
                done = True
                while done:
                    print_type_done_to_yield(n)
                    type_done = input().lower().strip()
                    if type_done != "done":
                        pass
                    if type_done == "done":
                        done = False

                target_2 = False

    # Printing thanks for playing
    print_thanks_for_playing()

    # DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
except:
    f.close()
