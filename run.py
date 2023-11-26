# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
print("Battleships")
print("Welcome to Battleships!")
print("You will be playing against the computer.")
print("The aim of the game is to sink all of the computer's ships before it sinks yours.")
print("You will be asked to enter the coordinates of where you want to fire your shot.")
print("The computer will then fire a shot at a random location.")
print("If you hit a ship, you will be told that you have hit a ship.")
print("If you miss, you will be told that you have missed.")
print("If you sink a ship, you will be told that you have sunk a ship.")
print("If the computer sinks one of your ships, you will be told that the computer has sunk one of your ships.")
print("The game will end when either you or the computer has sunk all of the other's ships.")
print("Good luck!")
print("You will now be asked to place your ships.")
print("You will be asked to enter the coordinates of where you want to place your ships.")
print("You will be asked to enter the coordinates of the front of the ship.")
print("You will then be asked to enter the coordinates of the back of the ship.")
print("The computer will then place its ships.")
print("The computer will randomly generate the coordinates of the front of the ship.")
print("The computer will then randomly generate the coordinates of the back of the ship.")
print("The computer will then check if the ship is in a valid position.")

def user_shot(guesses):

    ok = "n"
    while ok == "n":
        try: 
            shot = input("Enter the coordinates of where you want to fire your shot: ")
            shot = int(shot)
            if shot < 0 or shot > 99:
                print("Invalid shot, try again.")
            elif shot in guesses:
                print("You have already fired at this location, try again.")
            else:
                ok = "y"
                break
        except:
            print("Invalid entry, try again.")   
    return shot

def show_board(hit, miss, comp):
    print("     0  1  2  3  4  5  6  7  8  9")
    place = 0
    #outside for loop prints each row, number of row and the string of dashes.
    for x in range(10):
        row = ""
        #inside for loop creates the row of dashes.
        for y in range(10):
            ch = " _ "
            if place in miss:
                ch = " x "
            elif place in hit:
                ch = " o "
            elif place in comp:
                ch = " O "        
            row = row + ch
            place = place + 1
        print(x, " ",row)

def check_shot(boat1, shot, hit, miss, comp):
    if shot in boat1:
        print("You have hit a ship!")
        hit.append(shot)
        boat1.remove(shot)
        if len(boat1) == 0:
            print("You have sunk a ship!")
            print("You have sunk all of the computer's ships!")
            print("You have won!")
    else:
        print("You have missed!")
        miss.append(shot)

    return boat1, hit, miss, comp


boat1 = [45,46,47]
hit = []
miss = []
comp = []

guesses = hit + miss + comp

shot = user_shot(guesses)
hit, miss, comp = check_shot(boat1, shot, hit, miss, comp)
show_board(hit, miss, comp)