# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from random import randrange

print("Battleboard Game")
print("Welcome to Battleships!")

def check_ok(boat):

    boat.sort()
    for i in range(len(boat)):
        num = boat[i]
        if num < 0 or num > 99:
            boat = [-1]
            break



#this is the function to check if the boat is in the right place.
def check_boat(b,start,dirn):

    boat = []
    #this is the variable for the length of the boat.

    if dirn == 1:
        for i in range(b):
            boat.append(start - i*10)
    elif dirn == 2:
        for i in range(b):
            boat.append(start + i)
    elif dirn == 3:
        for i in range(b):
            boat.append(start + i*10)
    elif dirn == 4:
        for i in range(b):
            boat.append(start - i)
    boat = check_ok(boat)   
    return boat     

#this is the function to create the boats.
def create_boats(boats):

    ships = []
    boats = [4,4,3,3,2]
    #this is the for loop to create the boats.
    for b in boats:
        boat = [-1]
        while boat[0] == -1:
            boat_start = randrange(99)
            boat_direction = randrange(1,4)
            print(b, boat_start, boat_direction)
            boat = check_boat(b,boat_start,boat_direction)
        ships.append(boat)
        print(ships)


#this is the function to show the board.
def show_board(hit, miss, comp):
    print("     0  1  2  3  4  5  6  7  8  9")

    #this is the variable for the place on the board.
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
                #this is the symbol signifying a ship has been sunk.
                ch = " D "        
            row = row + ch
            place = place + 1

        print(x, " ",row)

#this is the function to check if the shot is a hit or a miss or comp.
def check_shot(boat1, boat2, boat3, shot, hit, miss, comp):
    if shot in boat1:
        print("You have hit a ship!")
        boat1.remove(shot)
        if len(boat1) > 0:
            hit.append(shot)
        else:
            comp.append(shot)
            print("You have sunk a ship!")
    #this is the same as above but for boat2.
    elif shot in boat2:
        print("You have hit a ship!")
        boat2.remove(shot)
        if len(boat2) > 0:
            hit.append(shot)
        else:
            comp.append(shot)
            print("You have sunk a ship!")
    #this is the same as above but for boat3.        
    elif shot in boat3:
        print("You have hit a ship!")
        boat3.remove(shot)
        if len(boat3) > 0:
            hit.append(shot)
        else:
            comp.append(shot)
            print("You have sunk a ship!")        
    else:
        print("You have missed!")
        miss.append(shot)   

    return boat1, boat2, hit, miss, comp

#this is the function that verifies the users input.
def user_shot(guesses):

    ok = "n"
    while ok == "n":
        try: 
            #this is the input that requests the users shot.
            shot = input("Enter the coordinates of where you want to fire your shot: ")
            shot = int(shot)
            if shot < 0 or shot > 99:
                #this is to check if the shot is within the range of the board.
                print("Invalid shot, try again.")
            elif shot in guesses:
                #this is to check if the shot has already been fired in this tile.
                print("You have already fired at this location, try again.")
            else:
                ok = "y"
                break
        except:
            #this is to check if the shot is a integer.
            print("Invalid entry, try again.")
            
    return shot

# this is the main program that runs the game.
boat1 = [23,24,25]
boat2 = [34,35,36]
boat3 = [1,11,21]

hit = []
miss = []
comp = []

# this is the for loop that runs the game and determines how many turns the user has.
for i in range(20):
    guesses = hit + miss + comp
    shot = user_shot(guesses)
    boat1, boat2, boat3, hit, miss, comp = check_shot(boat1, boat2, boat3, shot, hit, miss, comp)
    show_board(hit, miss, comp)

    # this is the if statement that determines if the user has won or lost.
    if len(boat1) < 1 and len(boat2) < 1:
        print("You have won!")
        break



    