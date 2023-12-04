# This while loop allows the user to play the game again.
play_again = 'yes'
while play_again.lower() == 'yes':

    # These are the instructions for the game.
    print("Welcome to Battleships!")
    print('''Instructions:
            1.) You have 15 shots to sink the three ships hidden on the board.
            2.) The ships are 3 tiles long, placed horizontally or vertically.
            3.) Enter the coordinates of where you want to fire your shot.
            4.) Coordinates are entered as a single number between 0 and 99.
            5.) The first digit is the row number.
            6.) The second digit is the column number.
            7.) For example, 0 is the top left and 99 is the bottom right.
            8.) If you hit a ship, you will be told that you have hit a ship.
            9.) You will be told if you have hit or missed after each shot.
            10.) If all tiles of a ship are hit, the ship is sunk.
            11.) When you have sunk all three ships, you will win the game.
            12.) If you run out of shots, you will lose the game.
                                 Good luck!
        ''')

# This is adapted from Dr. Codie's Battleship game.
# Linked here: https://drcodie.com/battleships-game-in-python/

    # this is the function to show the board.
    def display_board(hit, miss, destroy):
        print("     0  1  2  3  4  5  6  7  8  9")

        # Create a list of strings representing each row on the board
        board_rows = []
        for x in range(10):
            row = ""
            for y in range(10):
                place = x * 10 + y
                ch = " _ "
                if place in miss:
                    ch = " x "
                elif place in hit:
                    ch = " o "
                elif place in destroy:
                    ch = " D "
                row += ch
            board_rows.append(row)

        # Print each row with its corresponding number
        for i, row in enumerate(board_rows):
            print(i, " ", row)

    # this is the function to check if the shot is a hit or a miss or destroy.
    def check_shot(ship1, ship2, ship3, shot, hit, miss, destroy):
        if shot in ship1:
            print("You have hit a ship!")
            ship1.remove(shot)
            if len(ship1) > 0:
                hit.append(shot)
            else:
                destroy.append(shot)
                print("You have sunk a ship!")

        # this is the same as above but for ship2.
        elif shot in ship2:
            print("You have hit a ship!")
            ship2.remove(shot)
            if len(ship2) > 0:
                hit.append(shot)
            else:
                destroy.append(shot)
                print("You have sunk a ship!")

        # this is the same as above but for ship3.
        elif shot in ship3:
            print("You have hit a ship!")
            ship3.remove(shot)
            if len(ship3) > 0:
                hit.append(shot)
            else:
                destroy.append(shot)
                print("You have sunk a ship!")
        else:
            print("You have missed!")
            miss.append(shot)

        return ship1, ship2, ship3, hit, miss, destroy

    # this is the function that verifies the users input.
    def user_shot(guesses):
        while True:
            try:
                shot = int(input("Enter coordinates to fire a shot:"))
                if shot < 0 or shot > 99:
                    print("Invalid shot, try again.")
                elif shot in guesses:
                    print("Already fired at this location, try again.")
                else:
                    return shot
            except Exception:
                print("Invalid entry, try again.")

    # These are the pre-selected coordinates for the ships.
    ship1 = [23, 24, 25]
    ship2 = [67, 77, 87]
    ship3 = [00, 10, 20]

    hit = []
    miss = []
    destroy = []

    # this for loop runs the game and determines how many turns the user has.
    for i in range(15):
        turns_remaining = 15 - i
        print(f"Turn {i+1}. Turns remaining: {turns_remaining}")
        guesses = hit + miss + destroy
        shot = user_shot(guesses)
        ship1, ship2, ship3, hit, miss, destroy = \
            check_shot(ship1, ship2, ship3, shot, hit, miss, destroy)
        display_board(hit, miss, destroy)

        # this is the if statement that determines if the user has won or lost.
        print(i)
        if i == 14:
            print("You have lost!")
            break

        elif len(ship1) < 1 and len(ship2) < 1 and len(ship3) < 1:
            print("Congratulations! You have won!")
            break

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == 'no':
        print("Thanks for playing!")
        break
    else:
        print("Let's play again!")
        continue
