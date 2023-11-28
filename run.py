# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
print("Battleships")
print("Welcome to Battleships!")

def user_shot(guesses):

    ok = "n"
    while ok == "n":
        try: 
            #this is the input for the user to enter their shot.
            shot = input("Enter the coordinates of where you want to fire your shot: ")
            shot = int(shot)
            if shot < 0 or shot > 99:
                #this is to check if the shot is within the range of the board.
                print("Invalid shot, try again.")
            elif shot in guesses:
                #this is to check if the shot has already been fired.
                print("You have already fired at this location, try again.")
            else:
                ok = "y"
                break
        except:
            #this is to check if the shot is an integer.
            print("Invalid entry, try again.")   
    return shot

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
                ch = " O "        
            row = row + ch
            place = place + 1
        print(x, " ",row)

def check_shot(boat1, shot, hit, miss, comp):
    if shot in boat1:
        #remove the shot from the boat1 list.
        print("You have hit a ship!")
        boat1.remove(shot)
        #if the length of boat1 is greater than 0, then the ship has not been sunk.
        if len(boat1) > 0:
            hit.append(shot)
        else:
            comp.append(shot)
            print("You have sunk a ship!") 
    else:
        print("You have missed!")
        miss.append(shot)

    return boat1, hit, miss, comp

#this is the main program that calls the functions.
boat1 = [45,46,47]
hit = []
miss = []
comp = []

for i in range(10):
    guesses = hit + miss + comp
    shot = user_shot(guesses)
    boat1, hit, miss, comp = check_shot(boat1, shot, hit, miss, comp)
    show_board(hit, miss, comp)
    